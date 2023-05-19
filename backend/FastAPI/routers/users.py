from fastapi import APIRouter, HTTPException
from pydantic import BaseModel


router = APIRouter(tags=["users"])

# Inicia el server: uvicorn users:app --reload

@router.get('/usersjson')
async def usersjson():
    return [{"name" : "UNO", "surname": "last name", "url" : "http://loquesea.com"},
            {"name" : "UNO 1", "surname": "last name 1", "url" : "http://loquesea1.com"},
            {"name" : "UNO 2", "surname": "last name 2", "url" : "http://loquesea2.com"}]

# Trabajando con la entidad User
# Para crear user como entidad, usamos BaseModel
class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int


users_list = [User(id=1, name="Virginia", surname="Porras", url="http://loquesea.com", age=44),
            User(id=2, name="Geraldine", surname="Astorga", url="http://www.loquesea.com", age=46),
            User(id=3, name="Antonio", surname="Lusick", url="http://loquesea.cl", age=34)]

# BaseModel permite manejar los elementos como un json

@router.get('/users')
async def users():
    return  users_list

# filtrando con parámetros:

# pasando parámetro id por el path
# se ejecuta 
# http://127.0.0.1:8000/user/1   por ejemplo
@router.get('/user/{id}')
async def user(id: int):
   return search_users(id)

# filtrando con parámetros la query
# se ejecuta con 
# http://127.0.0.1:8000/userquery/?id=1   por ejemplo
# @router.get('/userquery/')
# probando si se le asigna el mismo nombre del anterior
# pero llamando por query
@router.get('/user/')
async def user(id: int):
   return search_users(id) 



# Insertando un usuario
# desde la pestaña de ejecución,  se cambia el método
# a post y en el body de la petición
# se incluye un json con el dato a ingresar
"""
{
  "id": 4,
  "name": "Pedro",
  "surname": "Martinez",
  "url": "http://loquesea.com",
  "age": 44
}
"""
# @router.post("/user")
# si deseamos cambiar los códigos de la respuesta
# debemos indicarlo en la cabecera
# es decir, de la siguiente manera
# cambiamos @router.post("/user")
# por
# status_code = 201 ::: devuelve "created"
'''
@router.post("/user", status_code=201)

# recibe un objeto tipo User ya definido arriba
async def user(user:User):
    # si encuentra un usuario con el mismo id
    if type(search_users(user.id)) == User:
        # igualmente queremos que retorne una excepcióm y no
        # un mensaje cuando no ha podido insertar
        # entonces sustituímos 
        # return {"error" : "El usuario ya existe"}
        # por 
        # el raise propaga la exception
        raise HTTPException(status_code = 404, detail = "El usuario ya existe")
        # para la exception importar from fastapi import FastAPI, HTTPException
    else:
        # is no existe, lo inserta
        users_list.append(user)
        return user
'''

@router.post("/user", response_model=User, status_code=201)
async def user(user:User):
    # si encuentra un usuario con el mismo id
    if type(search_users(user.id)) == User:
        raise HTTPException(status_code = 404, detail = "El usuario ya existe")         
    else:
        # is no existe, lo inserta
        users_list.append(user)
        return user



# Actualizando:
@router.put("/user/")
async def user(user:User):
    found = False
    # buscamos el usuario 
    # pero necesitamos la posición en la que está el usuario
    # por eso usamos enumerate 
    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id :
            # en la posición index se guardar el user
            users_list[index] = user
            found = True
    
    if not found:
        return {"error": "No existe un registro con ese id"}
    else:
        return user
    

# Eliminar
@router.delete("/user/{id}")
async def user(id: int):
    found = False
    for index, saved_user in enumerate(users_list):
        if saved_user.id == id :
            # en la posición index se elimina
            del users_list[index]
            found = True

    if not found:
        return {"error" : "No se ha eliminado el usuario"}
    else:
        return users_list
    





def search_users(id: int):
    users = filter(lambda user: user.id == id, users_list)
    # validando que exista un resultado válido
    try:
        return  list(users)[0]
    except:
        return {"error": "No existe un registro con ese id"}
   