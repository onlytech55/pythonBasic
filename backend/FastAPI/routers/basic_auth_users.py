from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

router = APIRouter(prefix="/basicauth",
                   tags=["basicauth"],
                   responses={status.HTTP_404_NOT_FOUND: {"message" : "No encontrado"}})

oauth2 = OAuth2PasswordBearer(tokenUrl="login")


class User(BaseModel):
    username: str
    fullname: str
    email: str
    disabled: bool

class UserDB(User):
    password: str

users_db = {
    "mouredev" : {
        "username": "mouredev",
        "fullname": "Brais Moure",
        "email": "brais@mouredev.com",
        "disabled": False,
        "password": "123456"
    },
    "mouredev2" : {
        "username": "mouredev2",
        "fullname": "Brais Moure 2",
        "email": "bmoure@mouredev.com",
        "disabled": True,
        "password": "654321"
    },

}

def search_user_db(username: str):
    if username in users_db : 
        # se coloca ** antes de users_db para indicarle que lleva varios parámetros
        return UserDB(**users_db[username])
    

def search_user(username: str):
    if username in users_db : 
        # se coloca ** antes de users_db para indicarle que lleva varios parámetros
        return User(**users_db[username])
 

# creamos el criterio de dependencia
# que valide que user:User = Depends() corrresponde a un usuario autenticado
# no lleva @router.get porque esto no va a estar disponible como 'función' dentro del api
# buscamos que el token sea válido y exista Depends(oauth2)
async def current_user(token: str = Depends(oauth2)):
    # verificamos que el token sea válido
    user = search_user(token)
    if not user :
        # incluyendo la libreria status de fastAPI tenemos acceso a status
        # en status_code=status.HTTP_401_UNAUTHORIZED
        # donde se definen todos los códigos
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                            detail="Credenciales de autenticación inválidas",
                            headers={"WWW-Authenticate":"Bearer"})
    
    if user.disabled:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
                            detail="Usuario inactivo")
    
    
    return user   



@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db :
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El usuario no existe")
    

    user = search_user_db(form.username)
    if not form.password == user.password:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="La contraseña no es correcta")
    
    return {"access_token": user.username,
             "token_type" : "bearer"}


@router.get("/users/me")
async def me(user:User = Depends(current_user)):
    return user
