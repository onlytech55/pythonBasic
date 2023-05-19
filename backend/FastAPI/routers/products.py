from fastapi import APIRouter
from pydantic import BaseModel

# el prefijo definido aquí me permite quitar las rutas de 
# @router.get('/products')  y que solo sea @router.get('/')
# y de @router.get('/products/{id}')  por: @router.get('/{id}')



router = APIRouter(prefix="/products", 
                   tags=["products"],
                   responses={404: {'message':'No encontrado'}})

class Product(BaseModel):
    id: int
    name: str
    category: str
    stock: int

# Inicia el server: uvicorn products:app --reload

products_list = [Product(id=1, name="Producto 1", category="Tornillos", stock=100),
                Product(id=2, name="Producto 2", category="Clavos", stock=100),
                Product(id=3, name="Producto 3", category="Alicates", stock=100),]

# BaseModel permite manejar los elementos como un json

@router.get('/')
async def products():
    return  products_list



@router.get('/{id}')
async def products(id: int):
    return  search_products(id)


def search_products(id: int):
    product = filter(lambda product: product.id == id, products_list)
    # validando que exista un resultado válido
    try:
        return  list(product)[0]
    except:
        return {"error": "No existe un registro con ese id"}
   
