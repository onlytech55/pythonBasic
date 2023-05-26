### User model ###

from pydantic import BaseModel
from typing import Optional 

class User(BaseModel):
    id: Optional[str]   # para indicar que es opcional
    username: str
    email: str
    