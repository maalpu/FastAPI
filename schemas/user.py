from pydantic import BaseModel
from typing import Optional


class UserSch(BaseModel):
    id: Optional[int]
    name: str
    lastname: str
    email: str
    password: str
    active: bool = False
