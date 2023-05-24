from fastapi import FastAPI

app = FastAPI(version='0.1')

@app.get('/')
# siempre que se llama a un servidor, 
# la operación es asíncrona
# recordar: asíncrona es cuando se envían peticiones
# y el código continúa con la siguiente petición 
# sin esperar una respuesta de la anterior
async def root():
    return "¡Hola FastAPI!"

# url local: http://127.0.0.1:8000/url

@app.get('/url')
async def url():
    return {"url_curso" : "https://mouredev.com/python"}

# Inicia el server: uvicorn main:app --reload
# Detener el server: CTRL+C

# Documentación con Swagger: http://127.0.0.1:8000/docs
# Documentación con Redocly: http://127.0.0.1:8000/redoc


#  Ahora vamos a incluir los routers
# primero, importamos los router creados
# Routers
from routers import products, users, jwt_auth_users, basic_auth_users, users_db

# router en products.router hacer referencia a la línea 5 del archivo routers/products ---> router = APIRouter()
# una vez creadas ambas routers, solo se inicia el servidor con uvicorn main:app --reload
app.include_router(products.router)
app.include_router(users.router)

app.include_router(jwt_auth_users.router)
app.include_router(basic_auth_users.router)

app.include_router(users_db.router)




# para poder acceder a recursos estáticos
from fastapi.staticfiles import StaticFiles
app.mount("/static", StaticFiles(directory="static"), name="static")