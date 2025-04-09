import os
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

# Cargar modelo
modelo = load_model('modelo_perros_gatos.keras')

# Ruta de la carpeta con imágenes
carpeta = 'imagenes_prueba'

# Tamaño que espera el modelo
img_size = (150, 150)

# Leer todas las imágenes
for nombre in os.listdir(carpeta):
    ruta = os.path.join(carpeta, nombre)
    try:
        img = image.load_img(ruta, target_size=img_size)
        img_array = image.img_to_array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)

        pred = modelo.predict(img_array)[0][0]

        clase = "🐶 Perro" if pred > 0.5 else "🐱 Gato"
        confianza = pred if pred > 0.5 else 1 - pred
        print(f"{nombre:<25} → {clase} ({confianza:.2%} de confianza)")
    except Exception as e:
        print(f"{nombre:<25} → ❌ Error: {str(e)}")