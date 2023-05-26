### Json Web Token Authentication ###

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from passlib.context import CryptContext

#importamos la libreria de manejo de tiempo para manipular el tiempo de validez del token
from datetime import datetime, timedelta

# definir el algoritmo de encriptación
# en éste método de autenticación debemos comprobar 
# que la contraseña esté encriptada

# DEFINIOS LOS PARAMETROS DE ENCRIPTAIÓN DEL TOKEN  
ALGORITHM = "HS256"
ACCESS_TOKEN_DURATION = 1
SECRET = "76f3e04e8a7306da92d9a2260a0452643c2f2e4b1759e13a8fe875d68dae8b98"

router = APIRouter(prefix="/jwtauth",
                   tags=["jwtauth"],
                   responses={status.HTTP_404_NOT_FOUND: {"message" : "No encontrado"}})

oauth2 = OAuth2PasswordBearer(tokenUrl="login")

# DEFINIR EL CONTEXTO DE ENCRIPTACIÓN

crypt = CryptContext(schemes=["bcrypt"])



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
        # encriptando 123456 con https://bcrypt-generator.com/
        "password": "$2a$12$51V2Bj/5E62rKuVEk9.sOu.O79QJNWG9eFSEFTqSWxpU8HSfKBoYa"
    },
    "mouredev2" : {
        "username": "mouredev2",
        "fullname": "Brais Moure 2",
        "email": "bmoure@mouredev.com",
        "disabled": True,
        # encriptando 654321 con https://bcrypt-generator.com/
        "password": "$2a$12$V71hSnT0OUNPKF6HZIQ9AuQt.NDH4DmpAqvoat0mQ8xgpjpnYN3vy"
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


# con respecto a la autenticación simple,
# ahora cambiamos la dependencia a un usuario autenticado
# ya el token no será el username

async def auth_user(token: str = Depends(oauth2)):
    # verificamos que el token sea válido
    exception =  HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                            detail="Credenciales de autenticación inválidas",
                            headers={"WWW-Authenticate":"Bearer"})
   
    try:
        username = jwt.decode(token, SECRET, algorithms=[ALGORITHM]).get("sub")
        if username is None:
            raise exception
        

    except JWTError:
           raise exception

    return search_user(username)

    
async def current_user(user: User = Depends(auth_user)):
    
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

    # agregamos la veirificación de la contraseña encriptada
    # crypt.verify(form.password, user.password)

    if not crypt.verify(form.password, user.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="La contraseña no es correcta")
    

    # calculamos en momento de expiración del token
    access_token_expiration = timedelta(minutes=ACCESS_TOKEN_DURATION)

    # fecha y hora de expiración del token
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_DURATION)

    # construimos el token agregando los datos que deseamos usar para esto
    # 
    access_token = {"sub": user.username, 
                    "exp":expire}

    #retorna el token encriptado
    return {"access_token": jwt.encode(access_token, SECRET, algorithm=ALGORITHM),
             "token_type" : "bearer"}


@router.get("/users/me")
async def me(user:User = Depends(current_user)):
    return user




