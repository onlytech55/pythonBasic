### MongoDB Client ###

# Módulo conexión MongoDB:pip install pymongo
# Ejecución: sudo mongod --dbpath "/path/a/la/base/de/datos/"
# Conexión: mongodb://localhost

from pymongo import MongoClient

# al instanciar MongoClient y no pasarle ningún parámetro
# automáticamente toma localhost como datos de conexión a la bbdd

# Base de datos local
# db_client = MongoClient().local

# Base de datos remota
# from pymongo.mongo_client import MongoClient
uri = "mongodb+srv://mari78viri78:6uDkOFtzyztGLOx0@cluster0.clzkhrz.mongodb.net/"
# Create a new client and connect to the server
db_client = MongoClient(uri).test
# Send a ping to confirm a successful connection

# try:
#     db_client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)
