from pydantic import BaseModel

class User(BaseModel):
    id: str | None   # para indicar que es opcional
    username: str
    email: str
    