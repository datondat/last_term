import mysql.connector

class connect:
    def __init__(self):
        self.db = mysql.connector.connect(
            user='root',
            password='',
            host='localhost',
            database='hotel'  # đúng là 'database', không phải 'name'
        )

    def get1(self, x, y):
        cur = self.db.cursor()
        cur.execute("SELECT * FROM users WHERE usn = %s and pass = %s", (x, y))
        result = cur.fetchone()
        return result is not None