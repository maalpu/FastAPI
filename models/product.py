import psycopg
from dotenv import load_dotenv
import os


class Product():
    conn = None

    def __init__(self):
        load_dotenv()

        DB_USER = os.getenv('DB_USER')
        DB_PASS = os.getenv("DB_PASSWORD")
        DB_HOST = os.getenv("DB_HOST")
        DB_PORT = os.getenv("DB_PORT")
        DB_DATABASE = os.getenv("DB_DATABASE")

        cad_conn = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}"

        try:
            self.conn = psycopg.connect(cad_conn)
        except psycopg.OperationalError as err:
            print(f"Error al conectar a la BD: {err}")
            self.conn = None

    def __def__(self):
        self.conn.close()

    def write(self, data):
        with self.conn.cursor() as cur:
            cur.execute("""
                INSERT INTO products(
                    codbar, 
                    name, 
                    description, 
                    id_categ, 
                    stock,
                    stock_min,
                    stock_ide, 
                    price1, 
                    price2,
                    img_s_url, 
                    img_m_url, 
                    img_l_url, 
                    active
                ) VALUES(
                    %(codbar)s,
                    %(name)s,
                    %(description)s,
                    %(id_categ)s,
                    %(stock)s,
                    %(stock_min)s,
                    %(stock_ide)s,
                    %(price1)s,
                    %(price2)s,
                    %(img_s_url)s,
                    %(img_m_url)s,
                    %(img_l_url)s,
                    %(active)s
                )
            """, data)
        self.conn.commit()

    def get_all(self):
        with self.conn.cursor() as cur:
            data = cur.execute("""
                SELECT * FROM products
            """)
            return data.fetchall()

    def get_one(self, id):
        with self.conn.cursor() as cur:
            data = cur.execute("""
                SELECT * FROM products WHERE id_prod = %s
            """, (id,))
            return data.fetchone()

    def delete(self, id):
        with self.conn.cursor() as cur:
            cur.execute("""
                DELETE FROM products WHERE id_prod = %s
            """, (id,))
            self.conn.commit()

    # def delete(self, data):
    #     with self.conn.cursor() as cur:
    #         cur.execute("""
    #             UPDATE products SET
    #                 deleted_at = CURRENT_TIMESTAMP,
    #                 active = False
    #             WHERE id_prod = %(id)s
    #         """, data)
    #         self.conn.commit()

    def update(self, data):
        with self.conn.cursor() as cur:
            cur.execute("""
                UPDATE productos SET 
                    codbar = %(codbar)s, 
                    name = %(name)s, 
                    description = %(description)s, 
                    id_categ = %(id_categ)s, 
                    stock = %(stock)s, 
                    stock_min = %(stock_min)s, 
                    stock_ide = %(stock_ide)s, 
                    price1 = %(price1)s, 
                    price2 = %(price2)s, 
                    img_s_url = %(img_s_url)s, 
                    img_m_url = %(img_m_url)s, 
                    img_l_url = %(img_l_url)s, 
                    active = True
                WHERE id_prod = %(id)s
            """, data)
            self.conn.commit()
