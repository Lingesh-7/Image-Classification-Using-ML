# 🏆 Celebrity Image Classification Using CNN  

## Overview  
This project utilizes **Convolutional Neural Networks (CNNs)** with **Transfer Learning** to classify images of celebrities. By leveraging deep learning, the model efficiently identifies and categorizes different celebrities based on image inputs, achieving **76% accuracy** on the test set.  

## Features  
- **CNN-based image classification** with a 6-layer architecture.  
- **Transfer Learning implementation** for enhanced accuracy.  
- **Data preprocessing & augmentation** to improve robustness.  
- **Flask-based deployment** for real-time image uploads & predictions.  

## Technologies Used  
- **CNN (Convolutional Neural Networks)** – Feature extraction & classification.  
- **Python & OpenCV** – Image processing.  
- **TensorFlow/Keras** – Deep learning framework.  
- **Flask** – Web-based deployment.  

## Installation  
```bash
git clone [https://github.com/Lingesh-7/Image-Classification-Using-ML]
cd Image-Classification-Using-ML
pip install -r requirements.txt
```

## Usage  
### 1. Training the Model  
```bash
python train.py --epochs 10 --batch_size 32
```

### 2. Running Image Classification  
```bash
python predict.py --image path/to/image.jpg
```

### 3. Web-Based Prediction (Flask App)  
```bash
python app.py
```
Visit `http://localhost:5000` to upload images for classification.  

## Results  
The model classifies **celebrity images** with **76% accuracy**, demonstrating effective feature extraction using CNNs.  

## Future Improvements  
- Fine-tune CNN layers for **higher accuracy**.  
- Optimize dataset preprocessing & augmentation.  
- Expand model deployment to **cloud-based applications**.  
