import cv2
import os
import random
import gradio as gr
import numpy as np
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model

model = load_model('covid-model.h5')
ex=['./examples/' + path for path in os.listdir('examples')]
random.shuffle(ex)

def predict_image(image_path):
    try:
        
        img = cv2.imread(image_path)
        img_array = img_to_array(img)
        img_resized = cv2.resize(img_array, (224, 224))
        prediction = model.predict(np.expand_dims(img_resized / 255.0, axis=0))
        prediction = 'Normal' if prediction >= 0.5 else 'Covid'
        return f'Prediction : {prediction}'
    except Exception as e:
        print(f"Error predicting image: {e}")

# Define the interface
def app():
    title = "COVID-19 Detection using X-Ray"

    gr.Interface(
        title=title,
        fn=predict_image,
        inputs=gr.Image(type="filepath"),
        outputs=gr.Textbox(),
        examples=ex,
    ).launch()

# Run the app
if __name__ == "__main__":
    app()