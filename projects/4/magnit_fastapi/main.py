# pip install "fastapi[all]"
# pip install "uvicorn[standard]"
# pip install psycopg2
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import psycopg2
import json

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


# ipconfig (192.168.0.128)
# uvicorn main:app --reload --host=0.0.0.0 --port=8000
# http://127.0.0.1:8000/

@app.get("/root")
async def root():
    return {"message": "Hello World"}


@app.get("/check")
async def check():
    return "Hello World"


@app.get("/check1")
async def check1():
    return "Hello World1"


# @app.get("/items/{id}", response_class=HTMLResponse)
# async def read_item(request: Request, id: str):
#     return templates.TemplateResponse("item.html", {"request": request, "id": id})


class Product:
    # def __init__(self, id_: int, title: str, price: float, count: int, type_measure: str, nomeklatura_id: str):
    #     self.id_ = id_
    #     self.title = title
    #     self.price = price
    #     self.count = count
    #     self.type_measure = type_measure
    #     self.nomeklatura_id = nomeklatura_id
    #
    # @staticmethod
    # def ph_create_product_from_row_from_db(row: tuple):
    #     Product(id_=row[0], title=row[1], price=row[2], count=row[3], type_measure=row[4], nomeklatura_id=row[5])
    #     # TODO
    #
    # @staticmethod
    # def ph_create_connection_to_products_db(query: str):
    #     with psycopg2.connect(user="pgs_usr", password="12345Qwerty!",
    #                           host="127.0.0.1", port="5432", dbname="pgs_db") as connection:
    #         with connection.cursor() as cursor:
    #             # SELECT * FROM products;
    #             return cursor

    @staticmethod
    def select_rows_query(query: str) -> list[tuple]:
        with psycopg2.connect(user="pgs_usr", password="12345Qwerty!",
                              host="127.0.0.1", port="5432", dbname="pgs_db") as connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                rows = cursor.fetchall()
                if rows is None:
                    raise Exception("not have objs")
                return rows


@app.post("/citys", response_class=HTMLResponse)
async def citys(request: Request):
    city: str = Form()
    print(city)

    city = request.get("city", None)
    if city == "Алматы":
        print("Яблоки")
    elif city == "Алматы":
        print("Байтерек")
    else:
        print("Другой город")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    # data = await request.body()
    # print(data)
    # data1 = await request.json()
    # print(data1)
    # city = request.get("city", None)
    # print(city)
    # if city == "Алматы":
    #     print("Яблоки")
    # elif city == "Алматы":
    #     print("Байтерек")
    # else:
    #     print("Другой город")

    # context = {"name": "Alema"}

    # obj = {"id": 1, "title": "Бананы", "price": 1200.75, "count": 50, "type_measure": "kg", "nomeklatura_id":
    # f"1_Бананы"}
    products = [
        {
            "id": x,
            "title": f"Бананы {x}",
            "price": round(1200.75 * x, 3),
            "count": round(20 / x, 3),
            "type_measure": "kg",
            "nomeklatura_id": f"{x}_Бананы_{x}"
        }
        for x in range(1, 30 + 1)
    ]
    products_list = []
    rows = Product.select_rows_query(
        "SELECT title, price, count, type_measure FROM products order by count desc, title asc;")
    # for row in rows:
    #     Product.create_product_from_row_from_db(row=row)

    print(rows, type(rows), type(rows[0]))

    products = [
        {
            "title": x[0],
            "price": x[1],
            "count": x[2],
            "type_measure": x[3],
        }
        for x in rows
    ]

    context = {"request": request, "products": products}
    return templates.TemplateResponse("ProductAll.html", context)


# return html-file
# return static(css / js)
# return full "ProductAll.html"
# create design (bootstrap 5)

# create new product from fastapi html form

def database():
    # cd C:\Program Files\PostgreSQL\15\bin>
    # cmd
    # psql -U postgres
    # \l
    # \d
    # CREATE USER pgs_usr WITH PASSWORD '12345Qwerty!';
    # CREATE DATABASE pgs_db OWNER pgs_usr;
    # \connect pgs_db
    # CREATE TABLE public.products ( id serial PRIMARY KEY, title VARCHAR(128) unique NOT NULL, price double precision DEFAULT 0.0, count INT default 0, type_measure VARCHAR(10) DEFAULT 'kg', nomeklatura_id VARCHAR(255) );
    # \d
    # GRANT ALL PRIVILEGES ON DATABASE pgs_db TO pgs_usr;
    # GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public to pgs_usr;
    # GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public to pgs_usr;
    # GRANT ALL PRIVILEGES ON ALL FUNCTIONS IN SCHEMA public to pgs_usr;

    # select * from products;
    # insert into products (title, price, count, type_measure, nomeklatura_id) VALUES ('Бананы', '1200.07', '60', 'kg', '3_Бананы');
    # insert into products (title, price, count, type_measure, nomeklatura_id) VALUES ('Olives', '3600.00', '7', 'kg', '5_Olive');
    # insert into products (title, price, count, type_measure, nomeklatura_id) VALUES ('Ananas', '6000.00', '0', 'kg', '666_Ananas');
    # select * from products;

    # delete from products where id=1;

    # \q
    pass
