from model import construir_modelo
from prepro_imagenes import preparar_directorios, crear_generadores
from tensorflow.keras.preprocessing import image
import numpy as np

# Preparar data (solo una vez)
# preparar_directorios()

# Crear generadores
train_gen, val_gen = crear_generadores()

# Crear y entrenar modelo
modelo = construir_modelo()
modelo.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
modelo.fit(train_gen, epochs=10, validation_data=val_gen)

# Guardar modelo
modelo.save('modelo_perros_gatos.keras')