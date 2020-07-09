import cv2
import pyzbar.pyzbar as pyzbar
import pybase64
import time
import pymysql

db = pymysql.connect(host="localhost", user="root", passwd="", database="student")
mycursor=db.cursor()

cap = cv2.VideoCapture(0)

li = []
def add(s):
    li.append(s)
    sq1 = "insert into presenty(name, presenty) value(%s, %s)" #we can add more columns
    b2 = (s, 'present')
    mycursor.execute(sq1, b2)
    db.commit()
        
def check(data):
    data = str(data)
    if data in li:
        print('already present')
    else:
        print('present')
        add(data)
    
while True:
    _,frame = cap.read()
    scanned = pyzbar.decode(frame)
    for obj in scanned:
        k = obj.data
        data = k.decode('utf-8')
        check(data)
        time.sleep(2)
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break
