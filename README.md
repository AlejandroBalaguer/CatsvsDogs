IA que permite diferencia a traves de imagenes entre perros y gatos.

Requisitos:

Descargar las imagenes de entrenamiento de perros y gatos en https://www.kaggle.com/competitions/dogs-vs-cats/data

Crear una carpeta en la raiz del directorio llamado "data" y extraer dentro la carpeta con las imagenes de entrenamiento

Quedara como /data/train/imagenes...

Y crear carpeta imagenes_prueba para poner imagenes que tenga que identificar la IA

Instalar requisitos pip:

En la consola del proyecto ejecutar "pip install -r requirements.txt"

Creacion de la IA:

Primero hay que preparar la data ya que la funcion que yo hice es ordenar las fotos de perros y gatos.

SOLO HAY QUE HACELO UNA VEZ

En el archivo main.py descomentar la linea # preparar_directorios()

La siguiente vez que lo ejecutes descomentalo ya que las fotos se abran organizado ya.

python main.py

Entrenara y creara a la IA, esto tardara unos minutos en terminar

Probar la IA:

Agregar fotos a imagenes_prueba de perros o gatos

python test.py
