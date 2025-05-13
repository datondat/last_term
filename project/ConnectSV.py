import mysql.connector
from mysql.connector import Error

class connect:
    def __init__(self):
        self.db = mysql.connector.connect(
            user='root',
            password='',
            host='localhost',
            database='hotel'
        )

    def get1(self, x, y):
        cur = self.db.cursor()
        cur.execute("SELECT * FROM users WHERE usn = %s and mk = %s", (x, y))
        result = cur.fetchone()
        return result is not None
    def get2(self,a,b,c,d,e):
        try:
            cur = self.db.cursor()
            if not all([a, b, e]):
                print("Thiếu thông tin bắt buộc!")
                return False
            cur.execute(
                "INSERT INTO users(usn, mk, mail, phone, cccd) VALUES (%s, %s, %s, %s, %s)",
                (a, b, c, d, e)
            )

            self.db.commit()
            return True
        except Error as x:
            print(f"loi {x}")
            print(a, b, c, d, e)
            return False

