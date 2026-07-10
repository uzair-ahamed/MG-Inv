from tkinter import *
import mysql.connector
import datetime as dt
from time import sleep
from threading import Thread
from tkinter import messagebox as msg
from tkinter import  simpledialog as sim
from tkinter import ttk
import datetime as d
import tkinter as tk
from tkcalendar import DateEntry
global a
global csi
global csn
global q
global n
global r
global i
global u

uz=Tk()
uz.geometry("1366x768+0+0")
uz.title("Modern Garments")

img1=PhotoImage(file="lpage.png")
img2=PhotoImage(file="user.png")
img3=PhotoImage(file="pass.png")
img4=PhotoImage(file="mail.png")
img5=PhotoImage(file="phone.png")
img6=PhotoImage(file="eye1.png")#show
img7=PhotoImage(file="eye2.png")#hide
img8=PhotoImage(file="optn.png")
img9=PhotoImage(file="exit.png")
img10=PhotoImage(file="hpage.png")
img11=PhotoImage(file="stk.png")
img12=PhotoImage(file="cus.png")
img13=PhotoImage(file="bro.png")
img14=PhotoImage(file="his.png")
img15=PhotoImage(file="hme.png")
img16=PhotoImage(file="prfl.png")
img17=PhotoImage(file="lgut.png")
img18=PhotoImage(file="bill.png")

#---------------------functions--------------------
def check_user():

    n=e1.get()
    p=e2.get()
    t=(n,p)
    con=mysql.connector.connect(host="localhost",user="root",password="12345678",database="uzair")
    cur=con.cursor()
    sql="select * from newuser where name=%s and pass=%s"
    cur.execute(sql,t)
    u=cur.fetchall()
    con.commit()
    
    if u==[]:
        msg.showwarning("Error","Invalid Login Details")
        
    else:
        msg.showinfo("Note","Login Success")
        con.close()
        lpage()
    
def lpage():
    uz0=Toplevel()
    uz0.geometry("1366x768+0+0")
    uz0.title("Load Page")
    uz0.config(bg="#a4a4a4")

    def load():
        for i in range (0,401):
            f2.config(width=i)
            sleep(0.0125)
            uz0.update()
                
    def loadtxt():
        for i in range (0,101):
            txt.config(text=str(i)+"%")
            sleep(0.05)
            uz0.update()
            if i==100:
                uz0.withdraw()
                mpage()

                
    f1=Frame(uz0,width=400,height=25,bg="white")
    f1.place(x=483,y=600)

    f2=Frame(f1,width=400,height=25,bg="black")
    f2.place(x=0,y=0)

    txt=Label(f2,text="",font=("times",14,"bold"),fg="white",bg="black")
    txt.place(x=180,y=0)

    t1=Thread(target=load)
    t2=Thread(target=loadtxt)

    t1.start()
    t2.start()

    uz0.mainloop()
    
#-----------------------------------------------------------

#----------------------signup page--------------------------
def sign():
    
    uz2=Toplevel()
    uz2.geometry("1366x768+0+0")
    uz2.title("Modern Garments")
    
    #------------------functions-------------
    def create_user():
        n=e1.get()
        p=e2.get()
        m=e3.get()
        ph=e4.get()
        t=(n,p,m,ph)
        con=mysql.connector.connect(host="localhost",user="root",password="12345678",database="uzair")
        cur=con.cursor()
        sql="insert into newuser (name,pass,mail,phno) values(%s,%s,%s,%s)"
        cur.execute(sql,t)
        con.commit()
        con.close()
        mpage()
        
    def backpg():
        uz2.destroy()
        uz.deiconify()
    #----------------------------------------
    l0=Label(uz2,image=img1)
    l0.place(x=0,y=0)

    l1=Label(uz2,image=img2,bg="#d7d7d7")
    l1.place(x=500,y=270)

    def e1del(u):
        e1.config(fg="black")
        e1.delete(0,END)
    def e1ins(u):
        if e1.get()=="":
            e1.config(fg="black")
            e1.insert (0,"User Name")
            
    e1=Entry(uz2,font=("times",24,"italic"),fg="#ffffff",bg="000000",bd=0)
    e1.place(x=570,y=270)
    e1.config(fg="white")
    e1.insert(0,"Enter Your User Name")
    e1.bind("<FocusIn>",e1del)
    e1.bind("<FocusOut>",e1ins)

    l2=Label(uz2,image=img3,bg="#e3e3e3")
    l2.place(x=500,y=370)
    
    def show(u):
        l6.place_forget()
        l7.place(x=925,y=375)
        e2.config(show="*")
    l6=Label(uz2,image=img7)
    l6.place(x=925,y=375)
    l6.bind("<Button-1>",show)

    def hide(u):
        l7.place_forget()
        l6.place(x=925,y=375)
        e2.config(show="")
    l7=Label(uz2,image=img6)
    l7.place(x=925,y=375)
    l7.bind("<Button-1>",hide)

  
    e2=Entry(uz2,font=("times",24,"italic"),fg="#ffffff",bg="000000",bd=0)
    e2.place(x=570,y=370)
    
    l3=Label(uz2,image=img4,bg="#d4d4d4")
    l3.place(x=500,y=470)

    def e3del(u):
        e3.config(fg="white")
        e3.delete(0,END)
    def e3ins(u):
        if e3.get()=="":
            e3.config(fg="white")
            e3.insert (0,"Enter Your User Name")
            
    e3=Entry(uz2,font=("times",24,"italic"),fg="#ffffff",bg="000000",bd=0)
    e3.place(x=570,y=470)
    e3.config(fg="white")
    e3.insert(0,"Enter Your Email")
    e3.bind("<FocusIn>",e3del)
    e3.bind("<FocusOut>",e3ins)

    l4=Label(uz2,image=img5,bg="#d4d4d4")
    l4.place(x=500,y=570)

    def e4del(u):
        e4.config(fg="white")
        e4.delete(0,END)
    def e4ins(u):
        if e4.get()=="":
            e4.config(fg="white")
            e4.insert (0,"Enter Your User Name")
    
    e4=Entry(uz2,font=("times",24,"italic"),fg="#ffffff",bg="000000",bd=0)
    e4.place(x=570,y=570)
    e4.config(fg="white")
    e4.insert(0,"Enter Your Phone")
    e4.bind("<FocusIn>",e4del)
    e4.bind("<FocusOut>",e4ins)

    b1=Button(uz2,text="Log In",font=("times",20,"italic"),bd=0,command=backpg)
    b1.place(x=550,y=645)

    b2=Button(uz2,text="Sign up",font=("times",20,"italic"),bd=0,command=create_user)
    b2.place(x=730,y=645)

    
#---------------------------------------------------------------

#------------------main page------------------------------------
def mpage():
    
    uz.withdraw()
    uz1=Toplevel()
    uz1.geometry("1366x768+0+0")
    uz1.title("Modern Garments")

    l1=Label(uz1,image=img10)
    l1.place(x=0,y=0)

    l2=Label(uz1,text="Modern Garments",font=("times",34,"bold"),bg="#ebebeb")
    l2.place(x=950,y=300)

    date=dt.datetime.now()
    format_date=f"{date:%a, %b %d %Y}"

    l3=Label(uz1, text=format_date, font=("times", 25),bg="#bebebe")
    l3.place(x=1120,y=690)

    l4=Label(uz1,image=img16,bg="#c2c2c2")
    l4.place(x=1200,y=5)

    l5=Label(uz1,text=e1.get(),font=("times",20,"bold"),bg="#bfbfbf")
    l5.place(x=1250,y=5)


    def clearall():
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)

#---------------------------Stocks-----------------------------------   
    def stocks():
        uz1st=Toplevel()
        uz1st.geometry("1366x768+0+0")
        uz1st.title("Modern Garments")
        uz1st.config(bg="#123")

        def clearall():
            e1.delete(0,END)
            e2.delete(0,END)
            e3.delete(0,END)
            e4.delete(0,END)

        def create():
            if (e1.get()=="" or e2.get()=="" or e3.get()=="" or e4.get()=="" ):
                msg.showwarning("Note","Please Enter All the Feils...!")
                
            else:
                i=e1.get()
                n=e2.get()
                q=e3.get()
                r=e4.get()
                t=(i,n,q,r)
                m="Stock Added"
                h=(i,n,q,r,m)

                con=mysql.connector.connect(host="localhost",user="root",
                                            password="12345678",database="uzair")
                cur=con.cursor()
                sql="insert into stk(id,name,qty,rte) values (%s,%s,%s,%s)"
                sqlh="insert into stkhis (id,name,qty,rate,chngs) values (%s,%s,%s,%s,%s)"
                cur.execute(sql,t)
                cur.execute(sqlh,h)
            
                con.commit()
                con.close()
                clearall()

        def update():
            i=e1.get()
            n=e2.get()
            q=e3.get()
            r=e4.get()
            t=(n,q,r)
            m="Stock Updated"
            h=(i,n,q,r,m)

            s=sim.askstring("Note","Enter Id to Update")

            con=mysql.connector.connect(host="localhost",user="root",
                                                password="12345678",database="uzair")
            cur=con.cursor()
            sql="update stk set name=%s,qty=%s,rte=%s where id="+s
            sqlh="insert into stkhis (id,name,qty,rate,chngs) values (%s,%s,%s,%s,%s)"
            cur.execute(sql,t)
            cur.execute(sqlh,h)
            con.commit()
            con.close()
            clearall()

        def read():
            clearall()
            r=sim.askstring("Note","Enter Your ID to view")
            con=mysql.connector.connect(host="localhost",user="root",
                                                password="12345678",database="uzair")
            cur=con.cursor()
            sql="select * from stk where id="+r
            cur.execute(sql)
            row=cur.fetchall()
            con.close()

            if row==[]:
                msg.showwarning("Warning",f"can't find user ID:{r}")
            else:
                def fun1 (a):
                    fun2(*a)
                def fun2 (a,b,c,d):
                    e1.insert(0,a)
                    e2.insert(0,b)
                    e3.insert(0,c)
                    e4.insert(0,d)
                fun1(*row)
                        
            
        def delete():
            s=sim.askstring("Note","Enter Id to Delete")
            t=(s,)
            i=e1.get()
            n=e2.get()
            q=e3.get()
            r=e4.get()
            m="Stock Deleted"
            h=(i,n,q,r,m)
            con=mysql.connector.connect(host="localhost",user="root",
                                            password="12345678",database="uzair")
            cur=con.cursor()
            sqlh="insert into stkhis (id,name,qty,rate,chngs) values (%s,%s,%s,%s,%s)"
            sql="delete from stk where id = %s"
            cur.execute(sqlh,h)
            cur.execute(sql,t)
            con.commit()
            con.close()
            e1.delete(0,END)
            e2.delete(0,END)
            e3.delete(0,END)
            e4.delete(0,END)

        def inv():
            uz1iv=Toplevel()
            uz1iv.geometry("1366x768+0+0")
            uz1iv.title("Modern Garments")
            uz1iv.config(bg="#123")

            con=mysql.connector.connect(host="localhost",user="root",
                                                password="12345678",database="uzair")
            cur=con.cursor()
            sql="select * from stk "
            cur.execute(sql)
            data=cur.fetchall()
            con.commit()
            con.close()

            sno=1

            mytree=ttk.Treeview(uz1iv,height=20)
            mytree["columns"]=("Sno","id","Name","Qty","Rte")
            mytree.column('#0',width=0,stretch='No')
            mytree.column('#1',width=100,anchor="center")
            mytree.column('#2',width=100,anchor="center")
            mytree.column('#3',width=300,anchor="center")
            mytree.column('#4',width=250,anchor="center")
            mytree.column('#5',width=250,anchor="center")

            mytree.heading('#0',text="")
            mytree.heading('#1',text="Sno")
            mytree.heading('#2',text="Id")
            mytree.heading('#3',text="Name")
            mytree.heading('#4',text="Quantity")
            mytree.heading('#5',text="Rate")
            mytree.place(x=183,y=150)
            s = ttk.Style()
            s.theme_use('clam')

            for i in data:
                mytree.insert("",index="end",values=(sno,i[0],i[1],i[2],i[3]))
                sno+=1

            b5=Button(uz1iv,image=img9,bd=0,bg="#123",fg="#fff",command=uz1iv.destroy)
            b5.place(x=25,y=25)
            
            
            
        l0=Label(uz1st,text="Product ID",font=("times",20,"italic"),bd=0,bg="#123",fg="white",width=14)
        l0.place(x=300,y=250)    
            
        l2=Label(uz1st,text="Product Name",font=("times",20,"italic"),bd=0,bg="#123",fg="white",width=14)
        l2.place(x=300,y=350)

        l3=Label(uz1st,text="Quatity",font=("times",20,"italic"),bd=0,bg="#123",fg="white",width=14)
        l3.place(x=300,y=450)

        l4=Label(uz1st,text="Rate",font=("times",20,"italic"),bd=0,bg="#123",fg="white",width=14)
        l4.place(x=300,y=550)

        e1=Entry(uz1st,font=("times",24,"italic"),fg="#000000",bd=0)
        e1.place(x=600,y=250)

        e2=Entry(uz1st,font=("times",24,"italic"),fg="#000000",bd=0)
        e2.place(x=600,y=350)

        e3=Entry(uz1st,font=("times",24,"italic"),fg="#000000",bd=0)
        e3.place(x=600,y=450)

        e4=Entry(uz1st,font=("times",24,"italic"),fg="#000000",bd=0)
        e4.place(x=600,y=550)

        bt1=Button(uz1st,command=create,text="Add item",font=("times",20,"italic"),bd=0,
                   bg="#123",fg="white",width=14)
        bt1.place(x=200,y=100)

        bt2=Button(uz1st,command=update,text="Update item",font=("times",20,"italic"),bd=0,
                   bg="#123",fg="white",width=14)
        bt2.place(x=400,y=100)

        bt3=Button(uz1st,command=delete,text="Delete item",font=("times",20,"italic"),bd=0,
                   bg="#123",fg="white",width=14)
        bt3.place(x=600,y=100)

        bt4=Button(uz1st,command=read,text="Read item",font=("times",20,"italic"),bd=0,
                   bg="#123",fg="white",width=14)
        bt4.place(x=800,y=100)

        bt5=Button(uz1st,command=inv,text="Stock Inventory",font=("times",20,"italic"),bd=0,
                   bg="#123",fg="white",width=14)
        bt5.place(x=1000,y=100)

        b5=Button(uz1st,image=img9,bd=0,bg="#123",command=uz1st.destroy)
        b5.place(x=25,y=25)

        b6=Button(uz1st,text="Clear All",font=("Times",20,"italic"),bd=0,bg="#123",fg="white",command=clearall,width=10)
        b6.place(x=580,y=650)
#---------------------------------Customers------------------------------------------
    def cus():
        uz1cu=Toplevel()
        uz1cu.geometry("1366x768+0+0")
        uz1cu.title("Modern Garments")
        uz1cu.config(bg="#123")

        def clearall():
            e1.delete(0,END)
            e2.delete(0,END)
            e3.delete(0,END)
            e4.delete(0,END)
            e5.delete(0,END)
        def checkempty():
            if(e1.get()==""):
                msg.showwarning("Note","Dont leave ID...!")
                return 1
            if(e2.get()==""):
                msg.showwarning("Note","Dont leave NAme...!")
                return 1
            if(e3.get()==""):
                msg.showwarning("Note","Dont leave Credit...!")
                return 1
            if(e4.get()==""):
                msg.showwarning("Note","Dont leave Debit...!")
                return 1
            if(e5.get()==""):
                msg.showwarning("Note","Dont leave Phone Number...!")
                return 1
            return 0
        def checkduplicate_user():
            uid=e1.get()
            con=mysql.connector.connect(host="localhost",user="root",
                                                password="12345678",database="uzair")
            cur=con.cursor()
            sql="select * from cus where id="+uid
            cur.execute(sql)
            row=cur.fetchall()
            if(row):
                msg.showwarning("Note","Id is already exists try different")
                return 1
            return 0
                           
        def add():
            if (checkempty()==0):
                i=e1.get()
                n=e2.get()
                c=e3.get()
                d=e4.get()
                p=e5.get()
                if(checkduplicate_user()==0):
                    m="Customer Created"
                    t=(i,n,c,d,p)
                    h=(i,n,c,d,p,m)
                    con=mysql.connector.connect(host="localhost",user="root",
                                                password="12345678",database="uzair")
                    cur=con.cursor()
                    sql="insert into cus(id,name,cre,deb,phno) values (%s,%s,%s,%s,%s)"
                    sqlh="insert into bchis (id,name,cre,deb,phno,chngs) values (%s,%s,%s,%s,%s,%s)"
                    cur.execute(sql,t)
                    cur.execute(sqlh,h)
                    msg.showinfo("Note","Record addedd Successfully")
                    con.commit()
                    con.close()
                    clearall()
            

        def update():
            i=e1.get()
            n=e2.get()
            c=e3.get()
            d=e4.get()
            p=e5.get()
            t=(n,c,d,p)
            m="Customer Updated"
            h=(i,n,c,d,p,m)

            s=sim.askstring("Note","Enter Id to Update")
            

            con=mysql.connector.connect(host="localhost",user="root",
                                                password="12345678",database="uzair")
            cur=con.cursor()
            sqlh="insert into bchis (id,name,cre,deb,phno,chngs) values (%s,%s,%s,%s,%s,%s)"
            sql="update cus set name=%s,cre=%s,deb=%s,phno=%s where id="+s
            cur.execute(sqlh,h)
            cur.execute(sql,t)
            con.commit()
            con.close()
            clearall()

        def read():
            clearall()
            r=sim.askstring("Note","Enter Your ID to view")
            con=mysql.connector.connect(host="localhost",user="root",
                                                password="12345678",database="uzair")
            cur=con.cursor()
            sql="select * from cus where id="+r
            cur.execute(sql)
            row=cur.fetchall()
            con.close()

            if row==[]:
                msg.showwarning("Warning",f"can't find user ID:{r}")
            else:
                def fun1 (a):
                    fun2(*a)
                def fun2 (a,b,c,d,e):
                    e1.insert(0,a)
                    e2.insert(0,b)
                    e3.insert(0,c)
                    e4.insert(0,d)
                    e5.insert(0,e)
                fun1(*row)

        def delete():
            s=sim.askstring("Note","Enter Id to Delete")
            i=e1.get()
            n=e2.get()
            c=e3.get()
            d=e4.get()
            p=e5.get()
            t=(s,)
            m="Customer Deleted"
            h=(i,n,c,d,p,m)
            con=mysql.connector.connect(host="localhost",user="root",
                                            password="12345678",database="uzair")
            cur=con.cursor()
            sqlh="insert into bchis (id,name,cre,deb,phno,chngs) values (%s,%s,%s,%s,%s,%s)"
            sql="delete from cus where id = %s"
            cur.execute(sql,t)
            cur.execute(sqlh,h)
            con.commit()
            con.close()
            clearall()

        def cdls():
            uz1cd=Toplevel()
            uz1cd.geometry("1366x768+0+0")
            uz1cd.title("Modern Garments")
            uz1cd.config(bg="#123")

            con=mysql.connector.connect(host="localhost",user="root",
                                                password="12345678",database="uzair")
            cur=con.cursor()
            sql="select * from cus "
            cur.execute(sql)
            data=cur.fetchall()
            con.commit()
            con.close()

            sno=1

            mytree=ttk.Treeview(uz1cd,height=20)
            mytree["columns"]=("Sno","id","Name","Deb","Cre","Phno")
            mytree.column('#0',width=0,stretch='No')
            mytree.column('#1',width=50,anchor="center")
            mytree.column('#2',width=50,anchor="center")
            mytree.column('#3',width=300,anchor="center")
            mytree.column('#4',width=150,anchor="center")
            mytree.column('#5',width=150,anchor="center")
            mytree.column('#6',width=200,anchor="center")

            mytree.heading('#0',text="")
            mytree.heading('#1',text="Sno")
            mytree.heading('#2',text="Id")
            mytree.heading('#3',text="Name")
            mytree.heading('#4',text="Debit")
            mytree.heading('#5',text="Credit")
            mytree.heading('#6',text="Phone No")
            mytree.place(x=233,y=150)
            s = ttk.Style()
            s.theme_use('clam')

            for i in data:
                mytree.insert("",index="end",values=(sno,i[0],i[1],i[2],i[3],i[4]))
                sno+=1

            b5=Button(uz1cd,image=img9,bd=0,bg="#123",fg="#fff",command=uz1cd.destroy)
            b5.place(x=25,y=25)
            

    

        l0=Label(uz1cu,text="Customer ID",font=("times",20,"italic"),bd=0,bg="#123",fg="white",width=14)
        l0.place(x=300,y=250)

        l1=Label(uz1cu,text="Customer Name",font=("times",20,"italic"),bd=0,bg="#123",fg="white",width=14)
        l1.place(x=300,y=350)

        l2=Label(uz1cu,text="credit",font=("times",20,"italic"),bd=0,bg="#123",fg="white",width=14)
        l2.place(x=300,y=450)

        l3=Label(uz1cu,text="debit",font=("times",20,"italic"),bd=0,bg="#123",fg="white",width=14)
        l3.place(x=300,y=550)

        l4=Label(uz1cu,text="Phone Number",font=("times",20,"italic"),bd=0,bg="#123",fg="white",width=14)
        l4.place(x=300,y=650)

        e1=Entry(uz1cu,font=("times",24,"italic"),fg="#000000",bd=0)
        e1.place(x=600,y=250)

        e2=Entry(uz1cu,font=("times",24,"italic"),fg="#000000",bd=0)
        e2.place(x=600,y=350)

        e3=Entry(uz1cu,font=("times",24,"italic"),fg="#000000",bd=0)
        e3.place(x=600,y=450)

        e4=Entry(uz1cu,font=("times",24,"italic"),fg="#000000",bd=0)
        e4.place(x=600,y=550)

        e5=Entry(uz1cu,font=("times",24,"italic"),fg="#000000",bd=0)
        e5.place(x=600,y=650)

        bt1=Button(uz1cu,command=add,text="Add",font=("times",20,"italic"),bd=0,
                   bg="#123",fg="white",width=14)
        bt1.place(x=200,y=100)

        bt2=Button(uz1cu,command=update,text="Update",font=("times",20,"italic"),bd=0,
                   bg="#123",fg="white",width=14)
        bt2.place(x=400,y=100)

        bt3=Button(uz1cu,command=delete,text="Delete",font=("times",20,"italic"),bd=0,
                   bg="#123",fg="white",width=14)
        bt3.place(x=600,y=100)

        bt4=Button(uz1cu,command=read,text="Read",font=("times",20,"italic"),bd=0,
                   bg="#123",fg="white",width=14)
        bt4.place(x=800,y=100)

        bt5=Button(uz1cu,command=cdls,text="Customer Details",font=("times",20,"italic"),bd=0,bg="#123",fg="white",width=14)
        bt5.place(x=1000,y=100)

        b5=Button(uz1cu,image=img9,bd=0,bg="#123",command=uz1cu.destroy)
        b5.place(x=25,y=25)

        b6=Button(uz1cu,text="Clear All",font=("Times",20,"italic"),bd=0,bg="#123",fg="white",command=clearall,width=10)
        b6.place(x=1050,y=440)
#---------------------------------Brokers--------------------------------
        
    def bro():
        uz1br=Toplevel()
        uz1br.geometry("1366x768+0+0")
        uz1br.title("Modern Garments")
        uz1br.config(bg="#123")

        def clearall():
            e1.delete(0,END)
            e2.delete(0,END)
            e3.delete(0,END)
            e4.delete(0,END)
            e5.delete(0,END)

        def add():
            if (e1.get()=="" or e2.get()=="" or e3.get()=="" or e4.get()=="" or e5.get()=="" ):
                msg.showwarning("Note","Please Enter All the Feils...!")
                
            else:
                i=e1.get()
                n=e2.get()
                c=e3.get()
                d=e4.get()
                p=e5.get()
                m="Broker Created"
                t=(i,n,c,d,p)
                h=(i,n,c,d,p,m)

                con=mysql.connector.connect(host="localhost",user="root",
                                            password="12345678",database="uzair")
                cur=con.cursor()
                sql="insert into bro(id,name,cre,deb,phno) values (%s,%s,%s,%s,%s)"
                sqlh="insert into bchis (id,name,cre,deb,phno,chngs) values (%s,%s,%s,%s,%s,%s)"
                cur.execute(sql,t)
                cur.execute(sqlh,h)
                con.commit()
                con.close()
                clearall()

        def update():
            i=e1.get()
            n=e2.get()
            c=e3.get()
            d=e4.get()
            p=e5.get()
            t=(n,c,d,p)
            m="Broker Updated"
            h=(i,n,c,d,p,m)

            s=sim.askstring("Note","Enter Id to Update")
            

            con=mysql.connector.connect(host="localhost",user="root",
                                                password="12345678",database="uzair")
            cur=con.cursor()
            sqlh="insert into bchis (id,name,cre,deb,phno,chngs) values (%s,%s,%s,%s,%s,%s)"
            sql="update bro set name=%s,cre=%s,deb=%s,phno=%s where id="+s
            cur.execute(sqlh,h)
            cur.execute(sql,t)
            con.commit()
            con.close()
            clearall()

        def read():
            clearall()
            r=sim.askstring("Note","Enter Your ID to view")
            con=mysql.connector.connect(host="localhost",user="root",
                                                password="12345678",database="uzair")
            cur=con.cursor()
            sql="select * from bro where id="+r
            cur.execute(sql)
            row=cur.fetchall()
            con.commit()
            con.close()

            if row==[]:
                msg.showwarning("Warning",f"can't find user ID:{r}")
            else:
                def fun1 (a):
                    fun2(*a)
                def fun2 (a,b,c,d,e):
                    e1.insert(0,a)
                    e2.insert(0,b)
                    e3.insert(0,c)
                    e4.insert(0,d)
                    e5.insert(0,e)
                fun1(*row)

        def delete():
            s=sim.askstring("Note","Enter Id to Delete")
            i=e1.get()
            n=e2.get()
            c=e3.get()
            d=e4.get()
            p=e5.get()
            t=(s,)
            m="Broker Deleted"
            h=(i,n,c,d,p,m)
            con=mysql.connector.connect(host="localhost",user="root",
                                            password="12345678",database="uzair")
            cur=con.cursor()
            sqlh="insert into bchis (id,name,cre,deb,phno,chngs) values (%s,%s,%s,%s,%s,%s)"
            sql="delete from bro where id = %s"
            cur.execute(sql,t)
            cur.execute(sqlh,h)
            con.commit()
            con.close()
            clearall()

        def bdls():
            uz1bd=Toplevel()
            uz1bd.geometry("1366x768+0+0")
            uz1bd.title("Modern Garments")
            uz1bd.config(bg="#123")

            con=mysql.connector.connect(host="localhost",user="root",
                                                password="12345678",database="uzair")
            cur=con.cursor()
            sql="select * from bro "
            cur.execute(sql)
            data=cur.fetchall()
            con.commit()
            con.close()

            sno=1

            mytree=ttk.Treeview(uz1bd,height=20)
            mytree["columns"]=("Sno","id","Name","Deb","Cre","Phno")
            mytree.column('#0',width=0,stretch='No')
            mytree.column('#1',width=50,anchor="center")
            mytree.column('#2',width=50,anchor="center")
            mytree.column('#3',width=300,anchor="center")
            mytree.column('#4',width=150,anchor="center")
            mytree.column('#5',width=150,anchor="center")
            mytree.column('#6',width=200,anchor="center")

            mytree.heading('#0',text="")
            mytree.heading('#1',text="Sno")
            mytree.heading('#2',text="Id")
            mytree.heading('#3',text="Name")
            mytree.heading('#4',text="Debit")
            mytree.heading('#5',text="Credit")
            mytree.heading('#6',text="Phone No")
            mytree.place(x=233,y=150)
            s = ttk.Style()
            s.theme_use('clam')

            for i in data:
                mytree.insert("",index="end",values=(sno,i[0],i[1],i[2],i[3],i[4]))
                sno+=1

            b5=Button(uz1bd,image=img9,bd=0,bg="#123",fg="#fff",command=uz1bd.destroy)
            b5.place(x=25,y=25)
            


        l0=Label(uz1br,text="Broker ID",font=("times",20,"italic"),bd=0,bg="#123",fg="white",width=14)
        l0.place(x=300,y=250)

        l1=Label(uz1br,text="Broker Name",font=("times",20,"italic"),bd=0,bg="#123",fg="white",width=14)
        l1.place(x=300,y=350)

        l2=Label(uz1br,text="credit",font=("times",20,"italic"),bd=0,bg="#123",fg="white",width=14)
        l2.place(x=300,y=450)

        l3=Label(uz1br,text="debit",font=("times",20,"italic"),bd=0,bg="#123",fg="white",width=14)
        l3.place(x=300,y=550)

        l4=Label(uz1br,text="Phone Number",font=("times",20,"italic"),bd=0,bg="#123",fg="white",width=14)
        l4.place(x=300,y=650)

        e1=Entry(uz1br,font=("times",24,"italic"),fg="#000000",bd=0)
        e1.place(x=600,y=250)

        e2=Entry(uz1br,font=("times",24,"italic"),fg="#000000",bd=0)
        e2.place(x=600,y=350)

        e3=Entry(uz1br,font=("times",24,"italic"),fg="#000000",bd=0)
        e3.place(x=600,y=450)

        e4=Entry(uz1br,font=("times",24,"italic"),fg="#000000",bd=0)
        e4.place(x=600,y=550)

        e5=Entry(uz1br,font=("times",24,"italic"),fg="#000000",bd=0)
        e5.place(x=600,y=650)

        bt1=Button(uz1br,command=add,text="Add",font=("times",20,"italic"),bd=0,
                   bg="#123",fg="white",width=14)
        bt1.place(x=200,y=100)

        bt2=Button(uz1br,command=update,text="Update",font=("times",20,"italic"),bd=0,
                   bg="#123",fg="white",width=14)
        bt2.place(x=400,y=100)

        bt3=Button(uz1br,command=delete,text="Delete",font=("times",20,"italic"),bd=0,
                   bg="#123",fg="white",width=14)
        bt3.place(x=600,y=100)

        bt4=Button(uz1br,command=read,text="Read",font=("times",20,"italic"),bd=0,
                   bg="#123",fg="white",width=14)
        bt4.place(x=800,y=100)

        bt5=Button(uz1br,command=bdls,text="Broker Details",font=("times",20,"italic"),
                   bd=0,bg="#123",fg="white",width=14)
        bt5.place(x=1000,y=100)
        
        b5=Button(uz1br,image=img9,bd=0,bg="#123",command=uz1br.destroy)
        b5.place(x=25,y=25)

        b6=Button(uz1br,text="Clear All",font=("Times",20,"italic"),bd=0,bg="#123",fg="white",command=clearall,width=10)
        b6.place(x=1050,y=440)
#--------------------------------History---------------------------------------
    def his():
        uz1hs=Toplevel()
        uz1hs.geometry("1366x768+0+0")
        uz1hs.title("Modern Garments")
        uz1hs.config(bg="#123")
        
        l0=Label(uz1hs,text="History",font=("times",34,"italic","bold"),
                 bd=0,bg="#123",fg="white",width=14)
        l0.place(x=490,y=50)

        b5=Button(uz1hs,image=img9,bd=0,bg="#123",command=uz1hs.destroy)
        b5.place(x=25,y=25)
        
        def stkhis():
            uzstkhs=Toplevel()
            uzstkhs.geometry("1366x768+0+0")
            uzstkhs.title("Modern Garments")
            uzstkhs.config(bg="#123")

            l0=Label(uzstkhs,text="Stock History",font=("times",34,"italic","bold"),
                 bd=0,bg="#123",fg="white",width=14)
            l0.place(x=490,y=50)

            sno=1

            mytree=ttk.Treeview(uzstkhs)
            mytree["columns"]=("Sno","id","Name","Qty","Rte","Chng")
            mytree.column('#0',width=0,stretch='No')
            mytree.column('#1',width=100,anchor="center")
            mytree.column('#2',width=100,anchor="center")
            mytree.column('#3',width=300,anchor="center")
            mytree.column('#4',width=250,anchor="center")
            mytree.column('#5',width=250,anchor="center")
            mytree.column('#6',width=300,anchor="center")

            mytree.heading('#0',text="")
            mytree.heading('#1',text="Sno")
            mytree.heading('#2',text="Id")
            mytree.heading('#3',text="Name")
            mytree.heading('#4',text="Quantity")
            mytree.heading('#5',text="Rate")
            mytree.heading('#6',text="Changes")
            mytree.place(x=33,y=150)

            con=mysql.connector.connect(host="localhost",user="root",
                                                password="12345678",database="uzair")
            cur=con.cursor()
            sql="select * from stkhis"
            cur.execute(sql)
            data=cur.fetchall()
            con.commit()
            con.close()

            for i in data:
                mytree.insert("",index="end",values=(sno,i[0],i[1],i[2],i[3],i[4]))
                sno+=1

            b5=Button(uzstkhs,image=img9,bd=0,bg="#123",command=uzstkhs.destroy)
            b5.place(x=25,y=25)

        
        def bchis():
            uzbchs=Toplevel()
            uzbchs.geometry("1366x768+0+0")
            uzbchs.title("Modern Garments")
            uzbchs.config(bg="#123")

            l0=Label(uzbchs,text="Cus & Bro History",font=("times",34,"italic","bold"),
                 bd=0,bg="#123",fg="white",width=14)
            l0.place(x=490,y=50)
            
            sno=1

            mytree=ttk.Treeview(uzbchs)
            mytree["columns"]=("Sno","id","Name","Deb","Cre","Phno","Chng")
            mytree.column('#0',width=0,stretch='No')
            mytree.column('#1',width=100,anchor="center")
            mytree.column('#2',width=100,anchor="center")
            mytree.column('#3',width=300,anchor="center")
            mytree.column('#4',width=100,anchor="center")
            mytree.column('#5',width=100,anchor="center")
            mytree.column('#6',width=300,anchor="center")
            mytree.column('#7',width=300,anchor="center")

            mytree.heading('#0',text="")
            mytree.heading('#1',text="Sno")
            mytree.heading('#2',text="Id")
            mytree.heading('#3',text="Name")
            mytree.heading('#4',text="Debit")
            mytree.heading('#5',text="Credit")
            mytree.heading('#6',text="Phone No")
            mytree.heading('#7',text="Changes")
            mytree.place(x=33,y=150)

            con=mysql.connector.connect(host="localhost",user="root",
                                                    password="12345678",database="uzair")
            cur=con.cursor()
            sql="select * from bchis"
            cur.execute(sql)
            data=cur.fetchall()
            con.commit()
            con.close()

            for i in data:
                mytree.insert("",index="end",values=(sno,i[0],i[1],i[2],i[3],i[4],i[5]))
                sno+=1

            b5=Button(uzbchs,image=img9,bd=0,bg="#123",command=uzbchs.destroy)
            b5.place(x=25,y=25)

        def blhis():
            uzblhs=Toplevel()
            uzblhs.geometry("1366x768+0+0")
            uzblhs.title("Modern Garments")
            uzblhs.config(bg="#123")

            l0=Label(uzblhs,text="Bill History",font=("times",34,"italic","bold"),
                 bd=0,bg="#123",fg="white",width=14)
            l0.place(x=490,y=50)

            con=mysql.connector.connect(host="localhost",user="root",
                                                password="12345678",database="uzair")
            cur=con.cursor()
            sql="select * from bilhis"
            cur.execute(sql)
            data=cur.fetchall()
            con.close()


            mytree=ttk.Treeview(uzblhs)
            mytree["columns"]=("Sno","cid","cname","bamnt")
            mytree.column('#0',width=0,stretch='No')
            mytree.column('#1',width=75,anchor="center")
            mytree.column('#2',width=75,anchor="center")
            mytree.column('#3',width=150,anchor="center")
            mytree.column('#4',width=100,anchor="center")
            

            mytree.heading('#0',text="")
            mytree.heading('#1',text="Sno")
            mytree.heading('#2',text="Cus Id")
            mytree.heading('#3',text="Cus Name")
            mytree.heading('#4',text="Bill Amount")
            mytree.place(x=100,y=150)

            for i in data:
                mytree.insert("",index="end",values=(i[0],i[1],i[2],i[3]))
                

            b5=Button(uzblhs,image=img9,bd=0,bg="#123",command=uzblhs.destroy)
            b5.place(x=25,y=25)
                                
        bt1=Button(uz1hs,text="Stocks",font=("times",20,"italic"),bd=0,bg="#123",
                    fg="white",width=20,command=stkhis)
        bt1.place(x=500,y=300)

        bt2=Button(uz1hs,text="Brokers & Customers",font=("times",20,"italic"),bd=0,bg="#123",
                    fg="white",width=20,command=bchis)
        bt2.place(x=500,y=400)

        bt2=Button(uz1hs,text="Bills",font=("times",20,"italic"),bd=0,bg="#123",
                    fg="white",width=20,command=blhis)
        bt2.place(x=500,y=500)
##--------------------------------logout------------------------------------
    def logout():
        uz1.withdraw()
        uz.deiconify()
        e1.delete(0,END)
        e2.delete(0,END)
#---------------------------------Billing---------------------------------
    def bill():
        uzbl=Toplevel()
        uzbl.geometry("1366x768+0+0")
        uzbl.title("Modern Garments")
        uzbl.config(bg="#123")
        sno=1

        con=mysql.connector.connect(host="localhost",user="root",
                                                password="12345678",database="uzair")
        cur=con.cursor()
        sql="select name from cus"
        cur.execute(sql)
        comcus=cur.fetchall()
        con.commit()
        con.close()
        def sltd_date():
            global bdate
            bdate = cal.get_date()
            bdate=bdate.strftime("%d-%m-%Y")
      
        def clearall():
            e1.delete(0,END)
            e2.delete(0,END)
            e3.delete(0,END)
            e4.delete(0,END)

        def stkchng(r,n,p,sq):
            m="Stock Sold"
            s=(r,)
            h=(r,n,p,sq,m)
            con=mysql.connector.connect(host="localhost",user="root",
                                            password="12345678",database="uzair")
            cur=con.cursor()
            sqlh="insert into stkhis (id,name,rate,qty,chngs) values (%s,%s,%s,%s,%s)"
            cur.execute(sqlh,h)
            schg="select qty from stk where id= %s"
            cur.execute(schg,s)
            stq=cur.fetchall()
            stq=stq.pop()
            
            for i in stq:
                pass
                
            sq=int(sq)
            q=i-sq
            t=(n,q)
            sql="update stk set name=%s,qty=%s where id= "+r
            cur.execute(sql,t)
            con.commit()
            con.close()
            clearall()
            

        def add():
            try:
                if (e1.get()=="" or e2.get()=="" or e3.get()=="" or e4.get()=="" or Name.get()==""):
                    msg.showwarning("Note","Please Enter All the Feils...!")
                    
                else:
                    global a
                    global csi
                    global csn
                    global q
                    global n
                    global r
                    global i
                    global u
                    
                    i=e1.get()
                    n=e2.get()
                    q=e3.get()
                    r=e4.get()
                    csi=cie.get()
                    csn=Name.get()
                    
                    q=int(q)
                    r=int(r)
                    a=q*r
                    q=str(q)
                    r=str(r)
                    a=str(a) 
                    t=(i,n,q,r,a)
                    con=mysql.connector.connect(host="localhost",user="root",
                                                    password="12345678",database="uzair")
                    cur=con.cursor()
                    idt=(i,)
                    sql="select * from bill where id=%s"
                    cur.execute(sql,idt)
                    row=cur.fetchall()
                    con.close()
                    if row==[]:
                        con=mysql.connector.connect(host="localhost",user="root",
                                                    password="12345678",database="uzair")
                        cur=con.cursor()
                        sql="insert into bill(id,name,qty,rte,amt) values (%s,%s,%s,%s,%s)"
                        cur.execute(sql,t)
                        con.commit()
                        con.close()
                        clearall()
                        
                    else:
                        con=mysql.connector.connect(host="localhost",user="root",
                                                    password="12345678",database="uzair")
                        cur=con.cursor()
                        u=(q,i)
                        sqlu="update bill set qty= %s where id= %s"
                        cur.execute(sqlu,u)
                        con.commit()
                        con.close()
                        clearall()
    
                      
                    con=mysql.connector.connect(host="localhost",user="root",
                                                        password="12345678",database="uzair")
                    cur=con.cursor()
                    tup1=(csn,)
                    sql="select id from cus where name= %s ;"
                    cur.execute(sql,tup1)
                    cid=cur.fetchall()
                    cie.delete(0,END)
                    cie.insert(0,cid)
                        
                        
                    tup2=(csn,)
                    sqlp="select phno from cus where name= %s ;"
                    cur.execute(sqlp,tup2)
                    cph=cur.fetchall()
                        
                    cid=cid.pop()
                    for u in cid:
                        pass

                        
                    con.commit()
                    con.close()
                    e5.delete(0,END)
                    e5.insert(0,cph)
                    stkchng(i,n,r,q)
            except Exception as ec:
                msg.showinfo("Note",ec)

        def update():
            pass


        def print1():
            global u
            p=e1.get()
            n=e2.get()
            sltd_date()
            
            con=mysql.connector.connect(host="localhost",user="root",
                                                    password="12345678",database="uzair")
            cur=con.cursor()
            sql="select * from bill"
            amt="select amt from bill;"
            clr="truncate table bill"
            cur.execute(sql)
            data=cur.fetchall()
            cur.execute(amt)
            tot=cur.fetchall()
            con.commit()
            
            sno=1
            
            top = Toplevel()
            top.geometry("500x500+800+150")
            top.config(bg="white")

            
            l1 = Label(top, text='Modern Garments',font=("times",20,"bold"),bg="white")
            l1.pack()
            l2 = Label(top, text='',font=("times",14,"bold"),bg="white")
            l2.pack()
            l3 = Label(top, text='---------RECIEPT----------',bg="white")
            l3.pack()
            
            rcpt=ttk.Treeview(top)
            rcpt["columns"]=("Sno","id","Name","Qty","Rte","Amt")
            rcpt.column('#0',width=0,stretch='No')
            rcpt.column('#1',width=50,anchor="center")
            rcpt.column('#2',width=25,anchor="center")
            rcpt.column('#3',width=150,anchor="center")
            rcpt.column('#4',width=100,anchor="center")
            rcpt.column('#5',width=75,anchor="center")
            rcpt.column('#6',width=100,anchor="center")
            
            rcpt.heading('#0',text="")
            rcpt.heading('#1',text="Sno")
            rcpt.heading('#2',text="Id")
            rcpt.heading('#3',text="Name")
            rcpt.heading('#4',text="Quantity")
            rcpt.heading('#5',text="Rate")
            rcpt.heading('#6',text="Amount")

            rcpt.place(x=0,y=150)
            s = ttk.Style()
            s.theme_use('clam')
            
            sno=1
            for i in data:
                rcpt.insert("",index="end",values=(sno,i[0],i[1],i[2],i[3],i[4]))
                sno+=1

            cur.execute(clr)
            con.close()
            
            b=0
            for k in tot:
                for j in k:
                    b=b+j
                    
            
            l4 = Label(top, text='Bill Amount :',font=("times",14,"bold"),bg="white")
            l4.place(x=300,y=400)
            l5= Label(top, text=b,font=("times",14,"bold"),bg="white")
            l5.place(x=421,y=400)

            time=d.datetime.now().strftime("%T")
            date=d.datetime.now().strftime("%D")
            l6 = Label(top, text=f"Date : {bdate}\nTime : {time}",font=("times",14),bg="white")
            l6.place(x=20,y=80)
            l7 = Label(top, text="Thank you Visit Again",font=("times",10),bg="white")
            l7.place(x=185,y=470)
            idd=cie.get()
            
            l8 = Label(top, text=f"Customer id: {idd}\nCustomer Name : {csn}",font=("times",14),bg="white")
            l8.place(x=230,y=80)
            
            
            csi=cie.get()
            cn=Name.get()
            
            con=mysql.connector.connect(host="localhost",user="root",
                                                password="12345678",database="uzair")
            cur=con.cursor()
            tup3=(csi,cn,b)
            
            blhs="insert into blhis (cid,cname,bamnt) values (%s,%s,%s)"
            cur.execute(blhs,tup3)
            con.commit()
            con.close()
            Name.delete(0,END)
            e5.delete(0,END)
            

        def selectRecord():
            e1.delete(0,END)
            e2.delete(0,END)
            e3.delete(0,END)
            e4.delete(0,END)
            sel=mytree.focus()
            vls=mytree.item(sel,'values') 
            e1.insert(0,vls[1]) 
            e2.insert(0,vls[2])
            #e3.insert(0,vls[3])
            e4.insert(0,vls[4])
            
        l5=Label(uzbl,text="Phone :",font=("times",15,"bold"),pady=5,bg="#123",fg="#fff")
        l5.place(x=100,y=145)
        e5=Entry(uzbl,font=("times",15))
        e5.place(x=200,y=150)    
        l1=Label(uzbl,text="ID   :",font=("times",15,"bold"),pady=5,bg="#123",fg="#fff")
        l1.place(x=100,y=195)
        e1=Entry(uzbl,font=("times",15))
        e1.place(x=200,y=200)
        l2=Label(uzbl,text="Name :",font=("times",15,"bold"),pady=5,bg="#123",fg="#fff")
        l2.place(x=100,y=245)
        e2=Entry(uzbl,font=("times",15))
        e2.place(x=200,y=250)
        l3=Label(uzbl,text="Quantity :",font=("times",15,"bold"),pady=5,bg="#123",fg="#fff")
        l3.place(x=100,y=295)
        e3=Entry(uzbl,font=("times",15))
        e3.place(x=200,y=300)
        l4=Label(uzbl,text="Rate :",font=("times",15,"bold"),pady=5,bg="#123",fg="#fff")
        l4.place(x=100,y=345)
        e4=Entry(uzbl,font=("times",15))
        e4.place(x=200,y=350)
        l5=Label(uzbl,text="Date :",font=("times",15,"bold"),pady=5,bg="#123",fg="#fff")
        l5.place(x=475,y=140)

        cal = DateEntry(uzbl, width=14, background="white", foreground="black", borderwidth=2
                        , date_pattern='dd/mm/y')
        cal.place(x=540,y=150)
       
        ci=Label(uzbl,text="Customer ID :",font=("times",15,"bold"),pady=5,bg="#123",fg="#fff")
        ci.place(x=100,y=45)
        
        cie=Entry(uzbl,font=("times",15))
        cie.place(x=250,y=50)
        
        cn=Label(uzbl,text="Customer Name :",font=("times",15,"bold"),pady=5,bg="#123",fg="#fff")
        cn.place(x=100,y=95)
        n = tk.StringVar()
        a=len(comcus)
        Name = ttk.Combobox(uzbl, width = 30, textvariable = n) 
        Name['values']=[comcus [i][0] for i in range(0,a)]
        Name.place(x=250,y=100)
        
        mytree=ttk.Treeview(uzbl)
        bill=ttk.Treeview(uzbl)
        mytree["columns"]=("Sno","id","Name","Qty","Rte")
        mytree.column('#0',width=0,stretch='No')
        mytree.column('#1',width=100,anchor="center")
        mytree.column('#2',width=100,anchor="center")
        mytree.column('#3',width=250,anchor="center")
        mytree.column('#4',width=150,anchor="center")
        mytree.column('#5',width=150,anchor="center")
        
        mytree.heading('#0',text="")
        mytree.heading('#1',text="Sno")
        mytree.heading('#2',text="Id")
        mytree.heading('#3',text="Name")
        mytree.heading('#4',text="Quantity")
        mytree.heading('#5',text="Rate")
        
        mytree.place(x=20,y=450)
        con=mysql.connector.connect(host="localhost",user="root",
                                                password="12345678",database="uzair")
        cur=con.cursor()
        sql="select * from stk"
        cur.execute(sql)
        data=cur.fetchall()
        con.commit()
        con.close()

        def crtcus():
            if Name.get()=="" or e5.get()=="":
                msg.showinfo("Note","Please Enter Name and Contact")

            else:
                n=Name.get()
                p=e5.get()
                c=0
                d=0
                m="Customer Created"
                t=(n,c,d,p)
                
                con=mysql.connector.connect(host="localhost",user="root",
                                                password="12345678",database="uzair")
                cur=con.cursor()
                sql="insert into cus(name,cre,deb,phno) values (%s,%s,%s,%s)"
                cur.execute(sql,t)
                con.commit()
                clearall()
                
                d=(n,)
                con=mysql.connector.connect(host="localhost",user="root",
                                                password="12345678",database="uzair")
                cur=con.cursor()
                e="select id from cus where name=%s"
                cur.execute(e,d)
                iid=cur.fetchall()
                for i in iid:
                    for j in i:
                        pass

                i=j
                con.close()
                clearall()

                con=mysql.connector.connect(host="localhost",user="root",
                                                password="12345678",database="uzair")
                cur=con.cursor()
                h=(i,n,p,m)
                sqlh="insert into bchis (id,name,phno,chngs) values (%s,%s,%s,%s)"
                cur.execute(sqlh,h)
                con.commit()
                con.close()
                clearall()
                Name.delete(0,END)
                e5.delete(0,END)
                

        def mybind(e):
            selectRecord()
        mytree.bind("<ButtonRelease-1>",mybind)

        for i in data:
                mytree.insert("",index="end",values=(sno,i[0],i[1],i[2],i[3]))
                sno+=1

        b2=Button(uzbl,text="Create",font=("times",15,"bold"),
                  bd=0,bg="#123",fg="#fff",command=crtcus,width=10)
        b2.place(x=550,y=200)

        b3=Button(uzbl,text="Clear",font=("times",15,"bold"),
                  bd=0,bg="#123",fg="#fff",command=clearall,width=10)
        b3.place(x=550,y=250)

        b4=Button(uzbl,text="Add",font=("times",15,"bold"),
                  bd=0,bg="#123",fg="#fff",command=add,width=10)
        b4.place(x=550,y=300)

        b5=Button(uzbl,text="Print",font=("times",15,"bold"),
                  bd=0,bg="#123",fg="#fff",command=print1,width=10)
        b5.place(x=550,y=350)

        b6=Button(uzbl,image=img9,bd=0,bg="#123",command=uzbl.destroy)
        b6.place(x=25,y=25)

        

#--------------------------------Options-------------------------------------        
    def options():
        fr=Frame(uz1,width=300,height=900,bg="#123")
        fr.place(x=0,y=0)

        bt1=Button(fr,text="Stocks",font=("times",20,"italic"),bd=0,bg="#123",
                    fg="white",width=14,command=stocks)
        bt1.place(x=60,y=100)

        l1=Label(fr,image=img11,bg="#123")
        l1.place(x=10,y=105)
        
        bt2=Button(fr,text="Customers",font=("times",20,"italic"),bd=0,bg="#123",
                    fg="white",width=14,command=cus)
        bt2.place(x=60,y=200)

        l2=Label(fr,image=img12,bg="#123")
        l2.place(x=10,y=205)

        bt3=Button(fr,text="Brokers",font=("times",20,"italic"),bd=0,bg="#123",
                    fg="white",width=14,command=bro)
        bt3.place(x=60,y=300)

        l3=Label(fr,image=img13,bg="#123")
        l3.place(x=10,y=305)

        bt4=Button(fr,text="History",font=("times",20,"italic"),bd=0,bg="#123",
                    fg="white",width=14,command=his)
        bt4.place(x=60,y=400)

        l4=Label(fr,image=img14,bg="#123")
        l4.place(x=10,y=405)

        bt5=Button(fr,text="Log Out",font=("times",20,"italic"),bd=0,bg="#123",
                    fg="white",width=14,command=logout)
        bt5.place(x=60,y=500)

        l5=Label(fr,image=img17,bg="#123")
        l5.place(x=10,y=505)

        bt6=Button(fr,text="Bill",font=("times",20,"italic"),bd=0,bg="#123",
                    fg="white",width=14,command=bill)
        bt6.place(x=60,y=600)

        l6=Label(fr,image=img18,bg="#123")
        l6.place(x=10,y=605)
            
        b2=Button(fr,image=img15,bd=0,bg="#123",command=fr.destroy)
        b2.place(x=15,y=15)

    b1=Button(uz1,image=img8,bd=0,command=options,bg="#b9b9b9",activebackground="#b9b9b9")
    b1.place(x=25,y=25)
#---------------------------------------------------------------------------
#--------------------------designing----------------------------------------

l0=Label(uz,image=img1)
l0.place(x=0,y=0)


l3=Label(uz,image=img2,bg="#d7d7d7")
l3.place(x=490,y=285)

def e1del(u):
    e1.config(fg="black")
    e1.delete(0,END)
def e1ins(u):
    if e1.get()=="":
        e1.config(fg="lightgrey")
        e1.insert (0,"Enter Your User Name")
        
e1=Entry(uz,font=("times",24,"italic"),fg="#000000",bd=0)
e1.place(x=555,y=280)
e1.config(fg="lightgrey")
e1.insert(0,"Enter Your User Name")
e1.bind("<FocusIn>",e1del)
e1.bind("<FocusOut>",e1ins)

l4=Label(uz,image=img3,bg="#e3e3e3")
l4.place(x=490,y=385)
    
e2=Entry(uz,font=("times",24,"italic"),fg="#000000",bd=0,show='*')
e2.place(x=555,y=380)

def show(u):
    l6.place_forget()
    l7.place(x=890,y=385)
    e2.config(show="*")
l6=Label(uz,image=img7)
l6.place(x=890,y=385)
l6.bind("<Button-1>",show)

def hide(u):
    l7.place_forget()
    l6.place(x=890,y=385)
    e2.config(show="")
l7=Label(uz,image=img6)
l7.place(x=890,y=385)
l7.bind("<Button-1>",hide)

b1=Button(uz,text="Log In",font=("times",20,"italic"),bd=0,command=check_user)#checkuser
b1.place(x=550,y=470)

b2=Button(uz,text="Sign up",font=("times",20,"italic"),bd=0,command=sign)#sign
b2.place(x=730,y=470)
#----------------------------------------------------------------------------
