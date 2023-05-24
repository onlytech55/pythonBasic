from pymongo import MongoClient

# al instanciar MongoClient y no pasarle ningún parámetro
# automáticamente toma localhost como datos de conexión a la bbdd
db_client = MongoClient()