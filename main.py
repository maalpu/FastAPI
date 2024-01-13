from fastapi import FastAPI, Response, status, HTTPException

# from models.product import Product
from models.user import User

# from schemas.product import ProductSch
from schemas.user import UserSch

app = FastAPI()
# connp = Product()
connu = User()


@app.get("/")
async def root():
    return {"greeting": "Hello, World!", "message": "Welcome to FastAPI!"}


# @app.get("/productos", status_code=status.HTTP_200_OK)
# def root():
#     items = []
#     for data in connp.get_all():
#         dicc = {}
#         dicc["id_prod"] = data[0]
#         dicc["codbar"] = data[1]
#         dicc["name"] = data[2]
#         dicc["description"] = data[3]
#         dicc["id_categ"] = data[4]
#         dicc["stock"] = data[5]
#         dicc["stock_min"] = data[6]
#         dicc["stock_ide"] = data[7]
#         dicc["price1"] = data[8]
#         dicc["price2"] = data[9]
#         dicc["img_s_url"] = data[10]
#         dicc["img_m_url"] = data[11]
#         dicc["img_l_url"] = data[12]
#         dicc["active"] = data[13]
#         items.append(dicc)
#     return items


@app.get("/users", status_code=status.HTTP_200_OK)
def get_users():
    items = []
    for data in connu.get_all():
        dicc = {}
        dicc["id"] = data[0]
        dicc["name"] = data[2]
        dicc["lastname"] = data[3]
        dicc["email"] = data[4]
        dicc["password"] = data[5]
        dicc["active"] = data[6]
        items.append(dicc)
    return items
