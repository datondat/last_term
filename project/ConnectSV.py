import mysql.connector
from mysql.connector import Error
import pandas as pd

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
    def get3(self,x):
        cur=self.db.cursor(dictionary=True)
        cur.execute("Select * from rooms where rs='%s'",
                    (x,)
        )
        a=cur.fetchone()
        if a:
            return f"Status: {a['sta']}\nBed: {a['bed']}\nType: {a['type']}\nCost: {a['cpd']} VND/Day"
        else:
            return "Room not found."
    def get4(self,x):
        cur = self.db.cursor(dictionary=True)
        cur.execute("Select sta from rooms where rs='%s'",
                    (x,)
                    )
        a = cur.fetchone()
        if a:
            return a['sta']
        else:
            return "Room not found."