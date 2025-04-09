import os
import shutil
from tensorflow.keras.preprocessing.image import ImageDataGenerator


def preparar_directorios():
    original_dir = 'data/train'
    base_dir = 'data/train_split'
    cats_dir = os.path.join(base_dir, 'cats')
    dogs_dir = os.path.join(base_dir, 'dogs')

    os.makedirs(cats_dir, exist_ok=True)
    os.makedirs(dogs_dir, exist_ok=True)

    for fname in os.listdir(original_dir):
        if fname.startswith('cat'):
            shutil.copy(os.path.join(original_dir, fname), os.path.join(cats_dir, fname))
        elif fname.startswith('dog'):
            shutil.copy(os.path.join(original_dir, fname), os.path.join(dogs_dir, fname))


def crear_generadores():
    datagen = ImageDataGenerator(rescale=1. / 255, validation_split=0.2)
    train_gen = datagen.flow_from_directory(
        'data/train_split',
        target_size=(150, 150),
        batch_size=32,
        class_mode='binary',
        subset='training'
    )
    val_gen = datagen.flow_from_directory(
        'data/train_split',
        target_size=(150, 150),
        batch_size=32,
        class_mode='binary',
        subset='validation'
    )
    return train_gen, val_gen
