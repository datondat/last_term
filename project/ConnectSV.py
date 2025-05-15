import mysql.connector
from mysql.connector import Error
import requests
import base64
from PIL import Image
from io import BytesIO
import common

c=None
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
        global c
        c=x

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
    def submit(self,ngay_den,ngay_di):
        cur = self.db.cursor()

        # Chèn dữ liệu vào MySQL
        phong=common.aaaa
        usn=c
        query = "INSERT INTO take(dayget, dayleave,usn, phong) VALUES (%s, %s,%s,%s)"
        values = (ngay_den, ngay_di,usn,phong,)
        cur.execute(query, values)

        cur.execute("UPDATE rooms SET sta = 'Hết' WHERE rs = %s", (phong,))
        self.db.commit()
        cur.execute("UPDATE take SET thanhtoan = 'Done' WHERE phong = %s", (phong,))
        self.db.commit()
        data = {
            "accountNo": "0363296445",
            "accountName": "NGUYEN QUOC DAT",
            "acqId": "970422",
            "amount": common.aaaa,
            "addInfo": "Thanh toan don hang 123x`",
            "format": "png"
        }

        response = requests.post("https://api.vietqr.io/v2/generate", json=data)
        print("API response:", response.status_code, response.json())
        if response.status_code == 200:
            qr_data = response.json()
            if qr_data["code"] == "00":
                qr_base64 = qr_data['data']['qrDataURL']
                if qr_base64:
                    qr_image_data = base64.b64decode(qr_base64.split(",")[1])
                    image = Image.open(BytesIO(qr_image_data))
                    image.show()
                else:
                    print("Lỗi: Không có ảnh QR được trả về.")
            else:
                print("API trả về lỗi:", qr_data["desc"])
        else:
            print("Lỗi kết nối API:", response.status_code)
        return "Đặt phòng thành công"
    def submit1(self,ngay_den,ngay_di):
        cur = self.db.cursor()

        # Chèn dữ liệu vào MySQL
        phong=common.aaaa
        usn=c
        cur.execute("DELETE FROM take WHERE usn = %s AND phong = %s", (usn, phong))
        cur.execute("UPDATE rooms SET sta = 'Trống' WHERE rs = %s", (phong,))
        self.db.commit()
        cur.execute("UPDATE take SET thanhtoan = 'not yet' WHERE phong = %s", (phong,))
        self.db.commit()
        return "Trả phòng thành công"


