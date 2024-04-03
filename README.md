# Documentación de la API de Detección de Tatuajes

La API de Detección de Tatuajes proporciona un servicio para predecir la presencia de tatuajes en imágenes utilizando un modelo de aprendizaje profundo. Este documento describe cómo utilizar la API para realizar predicciones y cómo integrarla en tus proyectos.

## Requisitos

- Python 3.x
- Bibliotecas requeridas: Flask, OpenCV (cv2), NumPy, requests, Keras (con TensorFlow)

## Instalación

1. Clona o descarga el repositorio que contiene el código de la API.
2. Instala las dependencias necesarias utilizando pip:

```bash
pip install flask opencv-python numpy requests tensorflow
```

## Uso de la API

### Iniciar el Servidor

Para iniciar el servidor de Flask y comenzar a utilizar la API, ejecuta el siguiente comando en la terminal dentro del directorio donde se encuentra el código de la API:

```bash
python APIServer.py runserver
```

## Enviar Imágenes para Predicción desde un cliente

Una vez que el servidor esté en funcionamiento, puedes enviar imágenes al servidor Flask para realizar predicciones de detección de tatuajes. Utiliza el siguiente código Python como ejemplo:

```python
import requests

# Rutas de las imágenes que deseas enviar al servidor Flask
image_paths = ["img/imageToTest.jpg", "img/imageToTest2.jpg", "img/imageToTest3.jpg"]

# Crear un diccionario vacío para almacenar las imágenes
files = {}

# Cargar las imágenes desde las rutas especificadas y agregarlas al diccionario
for i, image_path in enumerate(image_paths):
    with open(image_path, 'rb') as file:
        files[f'image{i + 1}'] = file.read()

# URL del servidor Flask
url = "http://127.0.0.1:5000/predict"

# Enviar la solicitud POST con las imágenes como archivos adjuntos
response = requests.post(url, files=files)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    # Obtener la predicción del cuerpo de la respuesta
    prediction = response.json()
    print(prediction)
else:
    print("Error:", response.text)
```

image_paths: Es una lista con las imágenes que queremos procesar.
    url: Será el URL del API
    prediction: Contendrá el JSON retornado por el API luego de la evaluación de la imagen

### Respuesta de la API

La API devuelve una lista de predicciones para cada imagen enviada. Cada predicción es una lista de valores que representan la probabilidad de que la imagen contenga un tatuaje.

Ejemplo de respuesta:

```json
[[[0.8717913031578064]], [[0.5577691793441772]], [[0.5490513443946838]]]
```

Cada valor corresponde al grado de posibilidad entre 0 y 1 de que la imagen contenga un tatuaje o no, y cada valor corresponde a cada una de las imágenes procesadas retornadas en su correspondiente orden.