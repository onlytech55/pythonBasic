### Users DB API ###

from fastapi import APIRouter, HTTPException, status
# importamos la entidad de la bbdd
from db.models.user import User
# importamos el cliente de la bbdd
from db.client import db_client
from db.schemas.user import user_schema, users_schema
from bson import ObjectId


router = APIRouter(prefix="/userdb",
                   tags=["userdb"],
                   responses={status.HTTP_404_NOT_FOUND: {"message" : "No encontrado"}})
# BaseModel permite manejar los elementos como un json

@router.get('/', response_model=list[User])
async def users():
    return  users_schema(db_client.local.users.find())

# filtrando con parámetros:

# pasando parámetro id por el path
# se ejecuta 
# http://127.0.0.1:8000/userdb/646e63bfc944b96804a892e5   por ejemplo
@router.get('/{id}')
async def user(id: str):
   return search_user("_id", ObjectId(id))

# filtrando con parámetros la query
# se ejecuta con 
# http://127.0.0.1:8000/userdb/?id=646e63bfc944b96804a892e5   por ejemplo
# probando si se le asigna el mismo nombre del anterior
# pero llamando por query
@router.get('/')
async def user(id: str):
   return search_user("_id", ObjectId(id))



@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
async def user(user:User):
    # si encuentra un usuario con el mismo id
    # if type(search_users_by_email(user.email)) == User:
    if type(search_user("email",user.email)) == User:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = "El usuario ya existe")         
    
    # el nombre de la base de datos ---> local
    # y el esquema ---> users
    # transformar la entidad user a json, para eso usamos dictionary
    user_dict = dict(user)
    # la entidad de user está definida incluyendole un campo id
    # pero éste debe ser un valor único para cada registro insertado
    # así que mongodb debería ser capaz de generar ese valor único
    # por lo tanto en nuesto modelo será opcional --> lo definimos como None y str (ya que así puede crear id mas grandes y únicos)
    # y debemos eliminarlo del json que va a insertar, por lo tanto:
    # debemos quitarlo del json para que no guarde como null el campo id ya que este no será recibido desde el from
    del user_dict["id"]
    
    id = db_client.local.users.insert_one(user_dict).inserted_id
    # comprobamos que existe en bbdd
    # OJO::: el nombre de la clave única que crea mongo es _id
    # transformamos la respuesta usando el schema definido
    new_user = user_schema(db_client.local.users.find_one({"_id":id}))
    
    return User(**new_user)



# Actualizando:
@router.put("/", response_model=User)
async def user(user:User):
    user_dict = dict(user)
    del user_dict["id"]
    try:
        db_client.local.users.find_one_and_replace({"_id": ObjectId(user.id)}, user_dict )
    except:
        return {"error": "No existe un registro con ese id"}
    else:
        return search_user("_id", ObjectId(user.id))
    

# Eliminar
# ejecutar con operación delete y url http://127.0.0.1:8000/userdb/646e63bfc944b96804a892e5 por ejemplo
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def user(id: str):
    found = db_client.local.users.find_one_and_delete({"_id": ObjectId(id)})
   
    if not found:
        return {"error" : "No se ha eliminado el usuario"}
  

def search_users_by_email(email: str):
    try:
        # print(email)
        # user = (db_client.local.user.find_one({"email":email}))  # ERROR, LA BASE DE DATOS SE LLAMA USERS NO USER!
        user = (db_client.local.users.find_one({"email":email}))  # ERROR, LA BASE DE DATOS SE LLAMA USERS NO USER!
        # print(user)
        return User(**user_schema(user))
    except:
        return {"error": "No existe un registro con ese id"}
   

# hacemos una búsqueda genérica
# puede recibir cualquiera de los campos
def search_user(field: str, key):
    try:
        user = (db_client.local.users.find_one({field:key}))  # ERROR, LA BASE DE DATOS SE LLAMA USERS NO USER!
        return User(**user_schema(user))
    except:
        return {"error": "No existe un registro con ese id"}
  