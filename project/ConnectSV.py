import mysql.connector
class connect:
    def conn(self):
        global db
        db = mysql.connector.connect(user='root',password='',host='localhos',name='hotel')
    def get(self):
        cur=db.cursor()
