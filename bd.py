from pymongo import MongoClient
from menu import nombre_usuario

# Conectar a la base de datos (o crearla si no existe)
cliente = MongoClient('mongodb+srv://jugador:1234@clusterfggv1.ozyn8t7.mongodb.net/?retryWrites=true&w=majority')  # Reemplaza con tu URL de conexión
base_datos = cliente['jugadores']
coleccion = base_datos['usersAndPoints']

# Insertar una puntuación en la base de datos
nombre_usuario
puntuacion = 100
coleccion.insert_one({'nombre_usuario': nombre_usuario, 'puntuacion': puntuacion})
