import os
import numpy as np
import cv2
import joblib
import tensorflow as tf
from flask import Flask, render_template, request, jsonify


app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


cnn_model_path = 'models/cnn.tflite'  
rfc_model_path = 'models/rfc2.pkl'
label_encoder_path = 'models/label_encoder.pkl'


interpreter = tf.lite.Interpreter(model_path=cnn_model_path)
interpreter.allocate_tensors()
print("CNN model loaded successfully.")

rf_classifier = joblib.load('models/rfc2.pkl')
print("Random Forest model loaded successfully.")

label_encoder = joblib.load('models/labels.pkl')
print("Label encoder loaded successfully.")

def preprocess_image(image_path, img_size=128):
    img = cv2.imread(image_path)
    img = cv2.resize(img, (img_size, img_size))  
    img = img / 255.0  
    img = np.expand_dims(img, axis=0)  
    return img


def predict_disease(image_path):
    img = preprocess_image(image_path)

    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

 
    interpreter.set_tensor(input_details[0]['index'], img.astype(np.float32))

    interpreter.invoke()

    features = interpreter.get_tensor(output_details[0]['index'])
 
    disease_prediction = rf_classifier.predict(features)

    disease_label = label_encoder.inverse_transform(disease_prediction)
    
    return disease_label[0]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
 
    image_path = os.path.join('static', file.filename)
    file.save(image_path)
    
    predicted_disease = predict_disease(image_path)
    
    return jsonify({'predicted_disease': predicted_disease})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
