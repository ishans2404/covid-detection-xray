from flask import Flask, render_template, request
import matplotlib.pyplot as plt
import numpy as np
import cv2
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model

app = Flask(__name__)

model = load_model('covid-model.h5')

def predict_image(image_path):
    img = cv2.imread(image_path)
    img_array = img_to_array(img)
    img_resized = cv2.resize(img_array, (224, 224))
    prediction = model.predict(np.expand_dims(img_resized / 255.0, axis=0))
    prediction = 'normal' if prediction >= 0.5 else 'covid'
    return prediction

@app.route("/", methods=['GET', 'POST'])
def homepage():
    return render_template("index.html")

@app.route("/about")
def about():
    return "working"

@app.route("/submit", methods=['POST'])
def submit_image():
    if request.method == 'POST':
        uploaded_image = request.files['imageFile']
        image_path = "static/" + uploaded_image.filename
        uploaded_image.save(image_path)
        prediction = predict_image(image_path)
        
    return render_template("index.html", prediction=prediction, image_path=image_path)

if __name__ == '__main__':
    app.run(debug=True)
