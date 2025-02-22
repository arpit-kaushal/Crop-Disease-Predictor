# Crop Disease Predictor

## Overview
Crop Disease Predictor is a web-based application that allows users to upload an image of a crop and predict the disease affecting it. The application utilizes a Convolutional Neural Network (CNN) model combined with a Random Forest Classifier to analyze the uploaded images and provide disease predictions.

## Features
- User-friendly interface for uploading crop images
- Image preview before submitting
- AI-powered disease prediction using deep learning and machine learning models
- Displays predicted disease name
- Responsive and interactive design

## Technologies Used
- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Flask (Python)
- **Machine Learning:** TensorFlow Lite, Random Forest Classifier
- **Libraries:** OpenCV, NumPy, Joblib
- **Storage:** Local file storage for uploaded images

## Project Structure
```
Crop-Disease-Predictor/
│── static/
│   ├── css/
│   │   ├── style.css
│   ├── js/
│   │   ├── script.js
│   ├── uploads/ (Stores uploaded images)
│── models/
│   ├── cnn.tflite
│   ├── rfc2.pkl
│   ├── label_encoder.pkl
│── templates/
│   ├── index.html
│── app.py
│── README.md
```

## Installation & Setup
### Prerequisites
Ensure you have Python installed (recommended version: 3.7+).

### Steps
1. **Clone the repository**
   ```bash
   git clone https://github.com/your-repo-url/crop-disease-predictor.git
   cd crop-disease-predictor
   ```
2. **Create a virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the application**
   ```bash
   python app.py
   ```
5. **Access the application**
   Open a web browser and go to `http://127.0.0.1:5000/`.

## Usage
1. Click on the "Browse" button to upload an image of the crop.
2. Click "Predict Disease" to get the prediction.
3. The predicted disease will be displayed on the screen.

## API Endpoints
- **GET `/`** - Renders the main webpage.
- **POST `/predict`** - Accepts an image upload and returns the predicted disease in JSON format.

## Model Details
- The CNN model extracts features from images.
- The extracted features are passed to a trained Random Forest Classifier.
- The classifier maps the features to a disease category using a label encoder.

## Troubleshooting
- Ensure all required dependencies are installed.
- Check if model files exist in the `models/` directory.
- If running on a server, update `host='0.0.0.0'` in `app.py`.

## Future Enhancements
- Improve accuracy with a more advanced deep-learning model.
- Add support for multiple crops.
- Deploy the model using cloud services.


