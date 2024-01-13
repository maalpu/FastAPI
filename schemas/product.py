from enum import Enum
from pydantic import BaseModel
from typing import Optional


class ProductSch(BaseModel):
    id_prod: Optional[int]
    codbar: str
    name: str
    description: str
    id_categ: Optional[int] = None
    stock: Optional[int] = None
    stock_min: Optional[int] = None
    stock_ide: Optional[int] = None
    price1: float
    price2: float
    img_s_url: str = None
    img_m_url: str = None
    img_l_url:  str = None
    active: bool = True
