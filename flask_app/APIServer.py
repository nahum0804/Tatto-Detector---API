import cv2
import numpy as np
from flask import Flask, request, jsonify
from keras.models import load_model

app = Flask(__name__)
model = load_model('./Model/tattoModel.h5')

def preprocess_image(image_data):
    img = cv2.imdecode(np.frombuffer(image_data, np.uint8), cv2.IMREAD_COLOR)
    img = cv2.resize(img, (100, 100))  # Redimensionar la imagen a un tamaño específico
    img = img / 255.0  # Normalizar los valores de píxeles
    return img

@app.route('/predict', methods=['POST'])
def predict():
    predictions = []
    print("Lenght data getted: ", len(request.files))
    for key, file_storage in request.files.items():
        image_data = file_storage.read()
        preprocessed_image = preprocess_image(image_data)
        prediction = model.predict(np.array([preprocessed_image]))
        predictions.append(prediction.tolist())

    print("Predictions: ", predictions)
    return jsonify(predictions)

# Función para ejecutar el servidor Flask
@app.cli.command()
def runserver():
    """Ejecutar el servidor de desarrollo de Flask."""
    app.run(port=5000)

if __name__ == '__main__':
    app.run(port=5000)
