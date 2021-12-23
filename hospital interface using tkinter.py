'''enter password in line-> 7'''
import tkinter.messagebox
from tkinter import  *
import mysql.connector as sqlcon
import random as rd

con=sqlcon.connect(host="sql6.freemysqlhosting.net",user="sql6460733",password="XvxjdKT12u")#connection to mysql 
cur=con.cursor()
cur = con.cursor(buffered=True)
cur.execute("create database if not exists sql6460733")
cur.execute("use hopital")
cur.execute("create table if not exists appointment"
            "("
            "idno varchar(12) primary key,"
            "name char(50),"
            "age char(3),"
            "gender char(1),"
            "phone varchar(10),"
            "bg varchar(3))")
cur.execute("create table if not exists appointment_details"
            "("
            "idno varchar(12) primary key,"
            "doctor varchar(50),"
            "date varchar(20),"
            "time varchar(20),"
            "appointment_no varchar(10))")

#  Message for registration
def entry():
    global e1,e2,e3,e4,e5,e6
    p1=e1.get()
    p2=e2.get()
    p3=e3.get()
    p4=e4.get()
    p5=e5.get()
    p6=e6.get()
        
    
    tkinter.messagebox.showinfo("DONE", "YOU HAVE BEEN REGISTERED")

#  For registration 
def register():
    global e1,e2,e3,e4,e5,e6
    root1=Tk()
    label=Label(root1,text="REGISTER YOURSELF",font='arial 25 bold')
    label.pack()
    frame=Frame(root1,height=500,width=200)
    frame.pack()
    l1=Label(root1,text="AADHAR CARD NO.")
    l1.place(x=10,y=130)
    e1=tkinter.Entry(root1)
    e1.place(x=100,y=130)
    l2=Label(root1,text="NAME")
    l2.place(x=10,y=170)
    e2=tkinter.Entry(root1)
    e2.place(x=100,y=170)
    l3=Label(root1,text="AGE")
    l3.place(x=10,y=210)
    e3=tkinter.Entry(root1)
    e3.place(x=100,y=210)
    l4=Label(root1,text="GENDER M\F")
    l4.place(x=10,y=250)
    e4=tkinter.Entry(root1)
    e4.place(x=100,y=250)
    l5=Label(root1,text="PHONE")
    l5.place(x=10,y=290)
    e5=tkinter.Entry(root1)
    e5.place(x=100,y=290)
    l6=Label(root1,text="BLOOD GROUP")
    l6.place(x=10,y=330)
    e6=tkinter.Entry(root1)
    e6.place(x=100,y=330)
    b1=Button(root1,text="SUBMIT",command=entry)
    b1.place(x=150,y=370)
    
    root.resizable(False,False)
    root1.mainloop()

#  Message for appointment
def apo_details():
    global x1,x2,h,p1,p2,p3,o,x4,x3
    p1=x2.get()
    p2=x3.get()
    p3=x4.get()
    if int(p1)==1:
        i=("Dr. sharma \nRoom no:- 10")
        j=("Dr. Verma \nRoom no:- 11")
        q=(i,j)
        h=rd.choice(q) 
        u=(23,34,12,67,53,72)
        o=rd.choice(u)
        det=("Your appointment is fixed with",h,
             "\nDate:-",p2,
             "\nTime:-",p3,
             '\nappointment no:-',o)

        query='insert into appointment_details values("{}", "{}", "{}", "{}", "{}")'.format(p1,h,p2,p3,o)
        cur.execute(query)
        tkinter.messagebox.showinfo("APPOINTMENT DETAILS",det)
     
    elif int(p1)==2:
        i=("Dr. Sidharth \nRoom no. 16")
        j=("Dr. Tendulkar \nRoom no. 17")
        q=(i,j)
        h=rd.choice(q) 
        u=(23,34,12,67,53,72)
        o=rd.choice(u)        
        det=("Your appointment is fixed with",h,
             "\nDate:-",p2,
             "\nTime:-",p3,
             '\nappointment no:-',o)
        query='insert into appointment_details values("{}", "{}", "{}", "{}", "{}")'.format(p1,h,p2,p3,o)
        cur.execute(query) 
        tkinter.messagebox.showinfo("APPOINTMENT DETAILS",det)
     
    elif int(p1)==3:
        i=("Dr. Kumar \nRoom no. 12")
        j=("Dr. Khan \nRoom no. 13")
        q=(i,j)
        h=rd.choice(q) 
        u=(23,34,12,67,53,72)
        o=rd.choice(u)        
        det=("Your appointment is fixed with",h,
             "\nDate:-",p2,
             "\nTime:-",p3,
             '\nappointment no:-',o)
        query='insert into appointment_details values("{}", "{}", "{}", "{}", "{}")'.format(p1,h,p2,p3,o)
        cur.execute(query) 
        tkinter.messagebox.showinfo("APPOINTMENT DETAILS",det)

    elif int(p1)==4:
        i=("Dr. Virat, \nRoom no. 18")
        j=("Dr. Leo \nRoom no. 19")
        q=(i,j)
        h=rd.choice(q) 
        u=(23,34,12,67,53,72)
        o=rd.choice(u)        
        det=("Your appointment is fixed with",h,
             "\nDate:-",p2,
             "\nTime:-",p3,
             '\nappointment no:-',o)
        query='insert into appointment_details values("{}", "{}", "{}", "{}", "{}")'.format(p1,h,p2,p3,o)
        cur.execute(query)
        tkinter.messagebox.showinfo("APPOINTMENT DETAILS",det)
    elif int(p1)==5:
        i=("Dr. Kohli \nRoom no. 14")
        j=("Dr. singh \nRoom no. 15")
        q=(i,j)
        h=rd.choice(q) 
        u=(23,34,12,67,53,72)
        o=rd.choice(u)        
        det=("Your appointment is fixed with",h,
             "\nDate:-",p2,
             "\nTime:-",p3,
             '\nappointment no:-',o)
        query='insert into appointment_details values("{}", "{}", "{}", "{}", "{}")'.format(p1,h,p2,p3,o)
        cur.execute(query)
        tkinter.messagebox.showinfo("APPOINTMENT DETAILS",det)   
    elif int(p1)==6:
        i=("Dr. Irfan \nRoom no. 001")
        j=("Dr. John \nRoom no. 002")
        k=("Dr. Sanjay \nRoom no. 003")
        l=("Dr. Shahid \nRoom no. 004")
        q=(i,j,k,l)
        h=rd.choice(q) 
        u=(23,34,12,67,53,72)
        o=rd.choice(u)        
        det=("Your appointment is fixed with",h,
             "\nDate:-",p2,
             "\nTime:-",p3,
             '\nappointment no:-',o)
        query='insert into appointment_details values("{}", "{}", "{}", "{}", "{}")'.format(p1,h,p2,p3,o)
        cur.execute(query)
        tkinter.messagebox.showinfo("APPOINTMENT DETAILS",det)   
    else:
        tkinter.messagebox.showwarning('WRONG INPUT','PLEASE ENTER VALID VALUE')

#  For appointment
def get_apoint():
    global x1,x2,x3,x4
    p1=x1.get()  
    cur.execute('select * from appointment where idno=(%s)',(p1,))
    dat=cur.fetchall()
    a=[]
    for i in dat:
        a.append(i)   
    if len(a)==0:
        tkinter.messagebox.showwarning("ERROR", "NO DATA FOUND!!")
    else:
        root3=Tk()
        label=Label(root3,text="APPOINTMENT",font='arial 25 bold')
        label.pack()
        frame=Frame(root3,height=500,width=300)
        frame.pack()
        if i[3]=='M' or i[3]=='m':
                x="Mr."
                name2=Label(root3,text=i[1])
                name2.place(x=140,y=80)
        else:
                x="Mrs\Ms."
                name2=Label(root3,text=i[1])
                name2.place(x=170,y=80)
        for i in dat:
            name=Label(root3,text='WELCOME')
            name.place(x=50,y=80)
            name1=Label(root3,text=x)
            name1.place(x=120,y=80)
            age=Label(root3,text='AGE:-')
            age.place(x=50,y=100)
            age1=Label(root3,text=i[2])
            age1.place(x=100,y=100)
            phone=Label(root3,text='PHONE:-')
            phone.place(x=50,y=120)
            phone1=Label(root3,text=i[4])
            phone1.place(x=100,y=120)
            bg=Label(root3,text='BLOOD GROUP:-')
            bg.place(x=50,y=140)
            bg1=Label(root3,text=i[5])
            bg1.place(x=150,y=140)


        L=Label(root3,text='DEPARTMENTS')
        L.place(x=50,y=220)
        L1=Label(root3,text="1.Orthopaedic surgeon ")
        L1.place(x=50,y=250)
        L2=Label(root3,text='2.Physician')
        L2.place(x=50,y=270)
        L3=Label(root3,text='3.Nephrologist')
        L3.place(x=50,y=290)
        L4=Label(root3,text='4.Neurologist')
        L4.place(x=50,y=310)
        L5=Label(root3,text='5.Gynaecologist')
        L5.place(x=50,y=330)
        L6=Label(root3,text='6.X-ray')
        L6.place(x=50,y=350)
        L7=Label(root3,text='Enter your choice')
        L7.place(x=100,y=370)
        x2=tkinter.Entry(root3)
        x2.place(x=200,y=370)
        
        L7=Label(root3,text=('enter date')).place(x=100,y=400)
        x3=tkinter.Entry(root3)
        x3.place(x=200,y=400)

        L8=Label(root3,text=('enter time in 24 hour format')).place(x=48,y=430)
        x4=tkinter.Entry(root3)
        x4.place(x=200,y=430)
        
        B1=Button(root3,text='Submit',command=apo_details)
        B1.place(x=120,y=480)   
        root3.resizable(False,False)
        root3.mainloop()



#  For AADHAAR no input
def apoint():
    global x1
    root2=Tk()
    label=Label(root2,text="APPOINTMENT",font='arial 25 bold')
    label.pack()
    frame=Frame(root2,height=200,width=200)
    frame.pack()
    l1=Label(root2,text="AADHAAR NO.")
    l1.place(x=10,y=130)
    x1=tkinter.Entry(root2)
    x1.place(x=100,y=130)
    b1=Button(root2,text='Submit',command=get_apoint)
    b1.place(x=100,y=160)
    root2.resizable(False,False)
    root2.mainloop()
    
#  List of doctors
def lst_doc():
    root4=Tk()
    
    l=["Dr. sharma","Dr. Verma","Dr. Kumar","Dr. Khan","Dr. Kohli","Dr. singh","Dr. Sidharth","Dr. tendulkar","Dr. Virat","Dr. Leo",'Dr. Irfan','Dr. John',
       'Dr. Sanjay','Dr. Shahid']
    m=["Orthopaedic surgeon","Orthopaedic surgeon","Nephrologist","Nephrologist","Gynaecologist","Gynaecologist","Physician","Physician","Neurologist",
       "Neurologist",'X-ray','X-ray','X-ray','X-ray']
    n=[10,11,12,13,14,15,16,17,18,19,20,21,22,23]

    frame=Frame(root4,height=500,width=500)
    frame.pack()
    
    
    l1=Label(root4,text='NAME OF DOCTORS') 
    l1.place(x=20,y=10)
    count=20
    for i in l:
       count=count+20
       l=Label(root4,text=i)
       l.place(x=20,y=count)

    l2=Label(root4,text='DEPARTMENT')
    l2.place(x=140,y=10)
    count1=20
    for i in m:
       count1=count1+20
       l3=Label(root4,text=i)
       l3.place(x=140,y=count1)

    l4=Label(root4,text='ROOM NO')
    l4.place(x=260,y=10)
    count2=20
    for i in n:
       count2=count2+20
       l5=Label(root4,text=i)
       l5.place(x=260,y=count2)
    root.resizable(False,False)
    root4.mainloop()

def ser_avail():
    
    root5=Tk()
    frame=Frame(root5,height=500,width=500)
    frame.pack()
    l1=Label(root5,text='SERVICES AVAILABLE')
    l1.place(x=20,y=10)
    f=["ULTRASOUND","X-RAY","CT Scan","MRI","BLOOD COLLECTION","DIALYSIS","ECG","CHEMIST","LAB"]
    count1=20
    for i in f:
       count1=count1+20
       l3=Label(root5,text=i)
       l3.place(x=20,y=count1)
    l2=Label(root5,text='ROOM NO.')
    l2.place(x=140,y=10)
    g=[1,2,3,4,5,6,7,8,9]
    count2=20
    for i in g:
       count2=count2+20
       l4=Label(root5,text=i)
       l4.place(x=140,y=count2)
    l5=Label(root5,text='To avail any of these please contact on our no.:- 7042****55')
    l5.place(x=20,y=240)
    root5.resizable(False,False)
    root5.mainloop()

def modify():
    global x3,x4,choice,new,x5,root6
    p1=x3.get()
    cur.execute('select * from appointment where idno=(%s)',(p1,))
    
    dat=cur.fetchall()
    a=[]
    for i in dat:
        a.append(i)   
    if len(a)==0:
        tkinter.messagebox.showwarning("ERROR", "NO DATA FOUND!!")
    else: 
      root6=Tk()
      frame=Frame(root6,height=500,width=500)
      frame.pack()
      l1=Label(root6,text='DATA MODIFICATION',font="arial 15 bold")
      l1.place(x=75,y=10)
      l2=Label(root6,text='WHAT YOU WANT TO CHANGE')
      l2.place(x=50,y=200)
      l3=Label(root6,text='1.NAME')
      l3.place(x=50,y=220)
      l4=Label(root6,text='2.AGE')
      l4.place(x=50,y=240)
      l5=Label(root6,text='3.GENDER')
      l5.place(x=50,y=260)
      l6=Label(root6,text='4.PHONE')
      l6.place(x=50,y=280)
      l7=Label(root6,text='5.BLOOD GROUP')
      l7.place(x=50,y=300)
      x2=Label(root6,text='Enter')
      x2.place(x=50,y=330)
      x4=tkinter.Entry(root6)
      choice=x4.get()
      x4.place(x=100,y=330)
      for i in dat:
            name=Label(root6,text='NAME:-')
            name.place(x=50,y=80)
            name1=Label(root6,text=i[1])
            name1.place(x=150,y=80)
            age=Label(root6,text='AGE:-')
            age.place(x=50,y=100)
            age1=Label(root6,text=i[2])
            age1.place(x=150,y=100)
            gen=Label(root6,text='GENDER:-')
            gen.place(x=50,y=120)
            gen1=Label(root6,text=i[3])
            gen1.place(x=150,y=120)
            pho=Label(root6,text='PHONE:-')
            pho.place(x=50,y=140)
            pho1=Label(root6,text=i[4])
            pho1.place(x=150,y=140)
            bg=Label(root6,text='BLOOD GROUP:-')
            bg.place(x=50,y=160)
            bg1=Label(root6,text=i[5])
            bg1.place(x=150,y=160)
      b=Button(root6,text='Submit',command=do_modify)
      b.place(x=50,y=400)
      L1=Label(root6,text='OLD DETAILS')
      L1.place(x=50,y=50)
      L2=Label(root6,text='ENTER NEW DETAIL')
      L2.place(x=50,y=360)
      x5=tkinter.Entry(root6)
      new=x5.get()
      x5.place(x=160,y=360)

      root6.resizable(False,False)
      root6.mainloop()

def do_modify():
	global ad,x3,x4,x5
	ad=x3.get()
	choice=x4.get()
	new=x5.get()
	if choice=='1':
		cur.execute('update appointment set name={} where idno={}'.format(new,ad))
	elif choice=='2':
		cur.execute('update appointment set age={} where idno={}'.format(new,ad))		
	elif choice=='3':
		cur.execute('update appointment set gender={} where idno={}'.format(new,ad))
	elif choice=='4':
		cur.execute('update appointment set phone={} where idno={}'.format(new,ad))	
	elif choice=='5':
		cur.execute('update appointment set bg={} where idno={}'.format(new,ad))
	else:
		pass
	root6.destroy()
	tkinter.messagebox.showinfo("DONE", "YOUR DATA HAS BEEN MODIFIED")
	
choice=None
new=None	
ad=None
def mod_sub():
    global x3,ad
    root7=Tk()
    label=Label(root7,text="MODIFICATION",font='arial 25 bold')
    label.pack()
    frame=Frame(root7,height=200,width=200)
    frame.pack()
    l1=Label(root7,text="AADHAAR NO.")
    l1.place(x=10,y=130)
    x3=tkinter.Entry(root7)
    x3.place(x=100,y=130)
    ad=x3.get()
    b1=Button(root7,text='Submit',command=modify)
    b1.place(x=100,y=160)
    root7.resizable(False,False)
    root7.mainloop()     

def search_data():
    global x3,ad
    root7=Tk()
    label=Label(root7,text="SEARCH DATA",font='arial 25 bold')
    label.pack()
    frame=Frame(root7,height=200,width=200)
    frame.pack()
    l1=Label(root7,text="AADHAAR NO.")
    l1.place(x=10,y=130)
    x3=tkinter.Entry(root7)
    x3.place(x=100,y=130)
    ad=x3.get()
    b1=Button(root7,text='Submit',command=view_data)
    b1.place(x=100,y=160)
    root7.resizable(False,False)
    root7.mainloop()

def view_data():
    global p1
    p1=x3.get()
    cur.execute('select * from appointment_details where idno=(%s)',(p1,))
    
    dat=cur.fetchall()
    a=[]
    for i in dat:
        a.append(i)   
    if len(a)==0:
        tkinter.messagebox.showwarning("ERROR", "NO DATA FOUND!!")
    else:
        det=a
        tkinter.messagebox.showinfo("APPOINTMENT DETAILS",det)
        
   
root=Tk()
label=Label(root,text="KARAMCHAND HOSPITAL",font="arial 40 bold",bg='light blue')
b1=Button(text="Registration",font="arial 20 bold",bg='yellow',command=register)
b2=Button(text="Appointment",font="arial 20 bold",bg='yellow',command=apoint)
b3=Button(text="List of Doctors",font="arial 20 bold",bg='yellow',command=lst_doc)
b4=Button(text="Services available",font='arial 20 bold',bg='yellow',command=ser_avail)
b7=Button(text="View data",font='arial 20 bold',bg='yellow',command=search_data)
b5=Button(text="Modify existing data",font='arial 20 bold',bg='yellow',command=mod_sub)
b6=Button(text="Exit",font='arial 20 bold',command=root.destroy,bg='violet')
label.pack()
b1.pack(side=LEFT,padx=10)
b3.pack(side=LEFT,padx=10)
b4.pack(side=LEFT,padx=10)
b2.place(x=25,y=500)
b7.pack(side=LEFT,padx=10)
b5.place(x=350,y=500)
b6.place(x=800,y=500)
frame=Frame(root,height=600,width=50)
frame.pack()
root.resizable(False,False)
root.mainloop()
