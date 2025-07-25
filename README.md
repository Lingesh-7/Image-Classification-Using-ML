# 🏆 Celebrity Image Classification
## Overview  
This project utilizes **SVM Algorithm** to classify images of celebrities,the model efficiently identifies and categorizes different celebrities based on image inputs, achieving **76% accuracy** on the test set.  


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
python main.py.py
```
Visit `http://localhost:5000` to upload images for classification.  

## Results  
The model classifies **celebrity images** with **76% accuracy**
