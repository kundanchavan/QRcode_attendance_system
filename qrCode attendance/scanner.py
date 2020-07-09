from tkinter import *
import qrcode
import pymysql


def submit():
    name = e1.get()
    roll = e2.get()
    qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5
    )
    all = (f'name:{name} rollno:{roll}')
    data = all
    qr.add_data(data)
    qr.make(fit=True)
    img=qr.make_image(fill='black', back_color='white')
    img.save(f'{name}.png')
    db = pymysql.connect(host="localhost", user="root", passwd="", database="student")
    mycursor=db.cursor()
    sq = "insert into stud(Name, Rollno) values(%s, %s)"
    b1 = (name, roll)
    mycursor.execute(sq,b1)
    db.commit()
    e1.delete(0, 'end')
    e2.delete(0,'end ')

    

rot=Tk()
rot.geometry('500x500')
rot.title('form')
l1 = Label(rot, text='student Name'); l1.grid(row=0, column=0)
l2 = Label(rot, text='Roll No'); l2.grid(row=1, column=0)
namevalue=StringVar()
rollvalue=StringVar()
e1 = Entry(rot, textvariable=namevalue); e1.grid(row=0, column=1)
e2 = Entry(rot, textvariable=rollvalue); e2.grid(row=1, column=1)
b1 = Button(rot, text='generate QR code', command=submit); b1.grid(row=3, column=0)
rot.mainloop()
