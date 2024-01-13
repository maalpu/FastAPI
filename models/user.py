import psycopg
from dotenv import load_dotenv
import os


class User():
    conn = None

    def __init__(self):
        load_dotenv()

        DB_USER = os.getenv('DB_USER')
        DB_PASS = os.getenv("DB_PASSWORD")
        DB_HOST = os.getenv("DB_HOST")
        DB_PORT = os.getenv("DB_PORT")
        DB_DATABASE = os.getenv("DB_DATABASE")

        cad_conn = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}"
        print()
        print(cad_conn)
        print()
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
                INSERT INTO users(
                    name,
                    lastaname, 
                    email, 
                    password, 
                    active
                ) VALUES(
                    %(name)s,
                    %(lastname)s,
                    %(email)s,
                    %(password)s,
                    %(active)s
                )
            """, data)
        self.conn.commit()

    def get_all(self):
        with self.conn.cursor() as cur:
            data = cur.execute("""
                SELECT * FROM users
            """)
            return data.fetchall()

    def get_one(self, id):
        with self.conn.cursor() as cur:
            data = cur.execute("""
                SELECT * FROM users WHERE id = %s
            """, (id,))
            return data.fetchone()

    def delete(self, id):
        with self.conn.cursor() as cur:
            cur.execute("""
                DELETE FROM users WHERE id = %s
            """, (id,))
            self.conn.commit()

    # def delete(self, data):
    #     with self.conn.cursor() as cur:
    #         cur.execute("""
    #             UPDATE users SET
    #                 deleted_at = CURRENT_TIMESTAMP,
    #                 active = False
    #             WHERE id = %(id)s
    #         """, data)
    #         self.conn.commit()

    def update(self, data):
        with self.conn.cursor() as cur:
            cur.execute("""
                UPDATE users SET 
                    name = %(name)s, 
                    lastname = %(lastname)s, 
                    email = %(email)s, 
                    password = %(password)s, 
                    active = True
                WHERE id = %(id)s
            """, data)
            self.conn.commit()
