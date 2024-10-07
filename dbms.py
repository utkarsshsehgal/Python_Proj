import tkinter
from tkinter import *

import mysql.connector
db = mysql.connector.connect(host="localhost",user="root",password="mysql",database="UT")
cur = db.cursor()
cur.execute('create database if not exists UT')
cur.execute('use UT')
cur.execute('create table if not exists Cars(Carid int,Cname varchar(40),Type varchar(40),Price int, Insurance int,\
Average int,Custname varchar(40),Address varchar(40),Contactno varchar(30))')


def Update():
    id = Carid.get()
    carname = Carname.get()
    type = Type.get()
    price = Price.get()
    insurance = Insurance.get()
    average = Average.get()
    custname= Cname.get()
    address= Address.get()
    contactno = Contactno.get()
           
    cur.execute("update Cars set cname='{}',type='{}',price={},insurance={},average={},custname='{}',address='{}',contactno='{}' where carid = ({})".format(carname,type,price,insurance,average,custname,address,contactno,id))
    db.commit()
    
    print('Update Successfully')
    
def Save():
    id = Carid.get()
    name= Carname.get()
    type=Type.get()
    price=Price.get()
    insurance = Insurance.get()
    average = Average.get()
    custname= Cname.get()
    address= Address.get()
    contactno = Contactno.get()
    
    cur.execute("insert into Cars values({},'{}','{}',{},{},{},'{}','{}','{}')".format(id,name,type,price,insurance,average,custname,address,contactno))
    db.commit()
    print('Data Saved Successfully')
    
def Search():
    id = Carid.get()
    cur.execute("select * from Cars  where carid = ({})".format(id))
    data=cur.fetchone()
    if data is None:
        print('No Such Car exist............')
    else:        
        Carname.insert('end',data[1])
        Type.insert('end',data[2])
        Price.insert('end',data[3])
        Insurance.insert('end',data[4])
        Average.insert('end',data[5])
        Cname.insert('end',data[6])
        Address.insert('end',data[7])
        Contactno.insert('end',data[8])
             
# GUI Code
root = tkinter.Tk()
root.title('Cars Management System')
root.geometry('1380x900')
root.configure(bg = '#e6ffff')

msg = "Cars Management System"
text_box = Text(root,height=2,width=70, font=("Bahnschrift Condensed",26), bg='#e6ffff', borderwidth=0)
text_box.pack(expand=True)
text_box.insert('end', msg)
text_box.config(state='disabled')
text_box.place(x = 380, y = 10)


LCarid =  Label(root, text= "Car Id", bg='#e6ffff', borderwidth=0,font=("Times new roman",12,"bold"))
LCarid.place(x=80,y=80)
Carid = Entry(root,font=("Times new roman",10,"bold"),bd=5,relief=GROOVE)
Carid.place(x=300,y=80)

LCarname =  Label(root, text= "Car Name", bg='#e6ffff', borderwidth=0,font=("Times new roman",12,"bold"))
LCarname.place(x=80,y=120)
Carname = Entry(root,font=("Times new roman",10,"bold"),bd=5,relief=GROOVE)
Carname.place(x=300,y=120)

LType =  Label(root, text= "Car Type [First/Second]", bg='#e6ffff', borderwidth=0,font=("Times new roman",12,"bold"))
LType.place(x=80,y=160)
Type = Entry(root,font=("Times new roman",10,"bold"),bd=5,relief=GROOVE)
Type.place(x=300,y=160)

LPrice =  Label(root, text= "Car Price ", bg='#e6ffff', borderwidth=0,font=("Times new roman",12,"bold"))
LPrice.place(x=80,y=200)
Price = Entry(root,font=("Times new roman",10,"bold"),bd=5,relief=GROOVE)
Price.place(x=300,y=200)

LInsurance =  Label(root, text= "Insurance  ", bg='#e6ffff', borderwidth=0,font=("Times new roman",12,"bold"))
LInsurance.place(x=80,y=240)
Insurance = Entry(root,font=("Times new roman",10,"bold"),bd=5,relief=GROOVE)
Insurance.place(x=300,y=240)

LAverage =  Label(root, text= "Average ", bg='#e6ffff', borderwidth=0,font=("Times new roman",12,"bold"))
LAverage.place(x=80,y=280)
Average = Entry(root,font=("Times new roman",10,"bold"),bd=5,relief=GROOVE)
Average.place(x=300,y=280)

LCname =  Label(root, text= "Customer Name ", bg='#e6ffff', borderwidth=0,font=("Times new roman",12,"bold"))
LCname.place(x=80,y=320)
Cname = Entry(root,font=("Times new roman",10,"bold"),bd=5,relief=GROOVE)
Cname.place(x=300,y=320)

LCaddress =  Label(root, text= "Address ", bg='#e6ffff', borderwidth=0,font=("Times new roman",12,"bold"))
LCaddress.place(x=80,y=360)
Address = Entry(root,font=("Times new roman",10,"bold"),bd=5,relief=GROOVE)
Address.place(x=300,y=360)

LContactno =  Label(root, text= "Contact No ", bg='#e6ffff', borderwidth=0,font=("Times new roman",12,"bold"))
LContactno.place(x=80,y=400)
Contactno = Entry(root,font=("Times new roman",10,"bold"),bd=5,relief=GROOVE)
Contactno.place(x=300,y=400)


Save = tkinter.Button(root, text="Save",height = 3, width = 20, bg='white', command =Save)
Save.place(x=80, y=550)

Search = tkinter.Button(root, text="Search",height = 3, width = 20, bg='white', command = Search)
Search.place(x=550, y=550)

Update = tkinter.Button(root, text="Update",height = 3, width = 20, bg='white', command = Update)
Update.place(x=1000, y=550)

root.mainloop()