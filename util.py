import json
import numpy as np
import joblib
import cv2
import pywt
import base64
from sklearn import preprocessing
from io import BytesIO
from PIL import Image

__model = None
__class_name_to_number = {}
__class_number_to_name = {}

def load_saved_artifacts():
    global __model
    global __class_name_to_number
    global __class_number_to_name

    with open("model/class_dictionary.json", "r") as f:
        __class_name_to_number = json.load(f)
        __class_number_to_name = {v: k for k, v in __class_name_to_number.items()}

    __model = joblib.load("model/image_classification_model.pkl")

def get_cv2_image_from_bytes(image_bytes):
    pil_image = Image.open(BytesIO(image_bytes)).convert("RGB")
    return cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)

def wavelet_transform(img, mode='haar', level=1):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_gray = np.float32(img_gray)
    img_gray /= 255.0
    coeffs = pywt.wavedec2(img_gray, mode, level=level)
    coeffs_H = list(coeffs)
    coeffs_H[0] *= 0
    img_reconstructed = pywt.waverec2(coeffs_H, mode)
    img_reconstructed *= 255
    img_reconstructed = np.uint8(img_reconstructed)
    return img_reconstructed

def classify_image(image_bytes):
    img = get_cv2_image_from_bytes(image_bytes)
    scalled_raw_img = cv2.resize(img, (32, 32))
    img_har = wavelet_transform(img, 'db1', 5)
    scalled_img_har = cv2.resize(img_har, (32, 32))
    combined_img = np.vstack((scalled_raw_img.reshape(32*32*3, 1), scalled_img_har.reshape(32*32, 1))).reshape(1, -1)

    predicted_class_num = __model.predict(combined_img)[0]
    predicted_class_name = __class_number_to_name[predicted_class_num]

    prediction_proba = __model.predict_proba(combined_img)[0]
    class_probabilities = [round(prob * 100, 2) for prob in prediction_proba]

    response = [{
        "class": predicted_class_name,
        "class_probability": class_probabilities,
        "class_dictionary": __class_name_to_number
    }]
    return response
