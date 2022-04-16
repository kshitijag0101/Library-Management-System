import mysql.connector as m
import tkinter
from tkinter import *
from tkinter import messagebox
from datetime import datetime
conn=m.connect(host="localhost",user="root",passwd="kshitij",database="lms")
c=conn.cursor()
c.execute("create table if not exists customers(custid int primary key,name varchar(40),phoneno varchar(20))")
c.execute("create table if not exists books(bookid int primary key,bookname varchar(40),author varchar(30),qty int)")
c.execute("create table if not exists transactions(transid int primary key,bookid int,book varchar(40),custid int,name varchar(40),date_of_issue_return datetime,status int)")
k=tkinter.Tk()
k.title("Library Management System")
k.geometry("400x630")
k.configure(background="#606060")
def AID(file):
    c.execute("select * from {}".format(file))
    a=c.fetchall()
    conn.commit()
    if a==[]:
        return 1
    else:
        return a[len(a)-1][0]+1
def addbooks():
    def add():
        book=e1.get()
        author=e2.get()
        quantity=e3.get()
        if book!="" and author!="" and quantity!="":
            c.execute("insert into books values({},'{}','{}',{})".format(int(AID("books")),book,author,quantity))
            messagebox.showinfo("Sucess","Data Saved")
            e1.delete(0,END)
            e2.delete(0,END)
            e3.delete(0,END)
        else:
            messagebox.showinfo("Error","Enter all the info.!")
    r=tkinter.Tk()
    r.title("Add Books")
    r.geometry("400x300")
    r.configure(background="#FF66AA")
    l=Label(r,text="Add Books",width=12,height=1,bg="#FFB6C1",font="Jokerman")
    l.place(x=130,y=30)
    l1=Label(r,text="Books Name",bg="#FF66AA")
    l1.place(x=80,y=90)
    e1=Entry(r,width=20)
    e1.place(x=180,y=90)
    l2=Label(r,text="Author",bg="#FF66AA")
    l2.place(x=100,y=130)
    e2=Entry(r,width=20)
    e2.place(x=180,y=130)
    l3=Label(r,text="Quantity",bg="#FF66AA")
    l3.place(x=100, y=170)
    e3=Entry(r, width=20)
    e3.place(x=180, y=170)
    b=Button(r,text="Back",command=r.destroy)
    b.place(x=350,y=250)
    b1=Button(r,text="Add",width="10",command=add)
    b1.place(x=180,y=220)
    r.mainloop()
def delbook():
    def delete():
        bid=e1.get()
        book=e2.get()
        k=0
        if bid!="":
            c.execute("select * from books where bookid={}".format(bid))
            a=c.fetchall()
            if a==[]:
                messagebox.showinfo("Error","Invalid Book No.")
                e1.delete(0,END)
            elif a[0][3]!=0:
                c.execute("update books set qty=0 where bookid={}".format(bid))
                conn.commit()
                messagebox.showinfo("Success","Removed")
                e1.delete(0,END)
                e2.delete(0,END)
                k=1
            elif a[0][3]==0:
                messagebox.showinfo("Caution","Alreday Removed")
                e1.delete(0,END)
                k=2
        else:
            messagebox.showinfo("Error","Enter all the info.!")
    def dispbook():
        t.delete(0,END)
        c.execute("select * from books")
        a=c.fetchall()
        c.execute("select * from books where bookname like '{}%' or author like '{}%'".format(e3.get(),e3.get()))
        b=c.fetchall()
        t.insert(0,"Book Id"+"               "+"Books"+"                  "+"Author"+"                  "+"Quantity")
        if b!=[]:
            for i in b:
                t.insert(END,"  "+str(i[0])+"                  "+i[1]+"                  "+i[2]+"                  "+str(i[3]))
        elif a!=[] and b==[]:
            t.insert(END,"\n")
            t.insert(END,"                          No book(s) found of given name/author                            ")
        elif a==[]:
            t.insert(END,"\n")
            t.insert(END,"                          No Books Found                          ")
    a=tkinter.Tk()
    a.title("Delete Books")
    a.geometry("800x600")
    a.configure(background="#22FF66")
    l=Label(a,text="Delete a book",width=14,height=1,bg="Yellow",font="Jokerman")
    l.place(x=280,y=20)
    l1=Label(a,text="Book ID",bg="#22FF66")
    l1.place(x=70,y=100)
    e1=Entry(a)
    e1.place(x=140,y=100)
    l2=Label(a,text="Book Name\n(optional)",bg="#22FF66")
    l2.place(x=60,y=130)
    l3=Label(a,text="Search by Book Name/Author",bg="#22FF66")
    l3.place(x=360,y=130)
    e2=Entry(a)
    e2.place(x=140,y=130)
    e3=Entry(a)
    e3.place(x=540,y=130,width=150)
    t=Listbox(a,width=70,height=20)
    t.place(x=350,y=160)
    b1=Button(a,text="Available books",command=dispbook,font="Papyrus",bg="#BBFF44",width=10,height=1)
    b1.place(x=500, y=60)
    b2=Button(a,text="Delete",command=delete)
    b2.place(x=170,y=180)
    b3=Button(a,text="Back",command=a.destroy,width=10)
    b3.place(x=680,y=520)
    i=0
    a.mainloop()
def addcustomer():
    def add():
        name=e1.get()
        phoneno=e2.get()
        if name!="" and phoneno!="":
            c.execute("insert into customers values({},'{}',{})".format(int(AID("customers")),name,phoneno))
            conn.commit()
            messagebox.showinfo("Success","Added")
            e1.delete(0, END)
            e2.delete(0, END)
        else:
            messagebox.showinfo("Error","Enter all the info!")
    r=tkinter.Tk()
    r.title("Add Customer")
    r.geometry("400x300")
    r.configure(background="#F0F00F")
    l=Label(r,text="Add Customer",width=15,height=1,bg="#50F040",font="Jokerman")
    l.place(x=130,y=30)
    l1=Label(r,text="Customer Name",bg="#F0F00F")
    l1.place(x=80,y=90)
    e1=Entry(r,width=20)
    e1.place(x=180,y=90)
    l2=Label(r,text="Customer Phone Number",bg="#F0F00F")
    l2.place(x=30,y=130)
    e2=Entry(r,width=20)
    e2.place(x=180,y=130)
    b=Button(r,text="Back",command=r.destroy)
    b.place(x=350,y=250)
    b1=Button(r,text="Add",width="10",command=add)
    b1.place(x=180,y=180)
    r.mainloop()
def deletecustomer():
    def delete():
        custid=e1.get()
        cusname=e2.get()
        k=0
        if custid!="":
            c.execute("select * from transactions where custid={}".format(custid))
            a=c.fetchall()
            if a==[]:
                c.execute("delete from customers where custid={}".format(custid))
                messagebox.showinfo("Success","Deleted")
                e1.delete(0,END)
                e2.delete(0,END)
                k=1
            else:
                c.execute("delete from customers where custid={}".format(custid))
                messagebox.showinfo("Success","Deleted")
                messagebox.showinfo("INFO.","All transactions made by this\n customer has been completed!")
                l=[]
                for i in a:
                    l.append(i[1])
                c.execute("update transactions set status=1,date_of_issue_return=now() where custid={}".format(custid))
                for j in l:
                    c.execute("select * from books where bookid={}".format(j))
                    b=c.fetchall()
                    c.execute("update books set qty={} where bookid={}".format(int(b[0][3])+1,j))
                    conn.commit()
                k=2
        else:
            messagebox.showinfo("Error","Enter all the info.!")
            k=3
        if k==0:
            messagebox.showinfo("Error","Invalid Customer ID")
    def dispcust():
        t.delete(0,END)
        c.execute("select * from customers")
        a=c.fetchall()
        c.execute("select * from customers where name like '{}%' or phoneno like '{}%'".format(e3.get(),e3.get()))
        b=c.fetchall()
        t.insert(0,"Customer ID"+"        "+"Customer Name"+"               "+"Phone No.")
        if b!=[]:
            for i in b:
                t.insert(END,str(i[0])+"                                 "+i[1]+"                              "+str(i[2]))
        elif a==[]:
            t.insert(END,"\n")
            t.insert(END,"                               No Customers Found                            ")
        elif a!=[] and b==[]:
            t.insert(END,"\n")
            t.insert(END,"                          No customer(s) found of entered name/Phone No.                            ")
    a=tkinter.Tk()
    a.title("Delete Customer")
    a.geometry("800x560")
    a.configure(background="#AA33EE")
    l=Label(a,text="Delete Customer",width=17,height=2,bg="#FF44FF",font="Jokerman")
    l.place(x=250,y=20)
    l1=Label(a,text="Customer ID",bg="#AA33EE")
    l1.place(x=50,y=100)
    e1=Entry(a)
    e1.place(x=140,y=100)
    l2=Label(a,text="Customer Name\n(optional)",bg="#AA33EE")
    l2.place(x=40,y=130)
    e2=Entry(a)
    e2.place(x=140,y=130)
    l3=Label(a,text="Search by Name/PhoneNo.",bg="#AA33EE")
    l3.place(x=350,y=140)
    e3=Entry(a,width=30)
    e3.place(x=540,y=140)
    b=Button(a,text="Available Customer",command=dispcust,font="Papyrus",bg="#DE0066")
    b.place(x=500, y=60)
    t=Listbox(a,width=70,height=20)
    t.place(x=350,y=170)
    b1=Button(a,text="Delete",command=delete)
    b1.place(x=170,y=180)
    b2=Button(a,text="Back",command=a.destroy,width=10)
    b2.place(x=650,y=520)
    a.mainloop()
def issue():
    def isu():
        bid=e1.get()
        cid=e2.get()
        k=0
        q=0
        if bid!="" and cid!="":
            c.execute("select * from books where bookid={}".format(bid))
            a=c.fetchall()
            if a!=[]:
                nq=int(a[0][3])
                if nq!=0:
                    c.execute("update books set qty={} where bookid={}".format(int(nq-1),bid))
                    conn.commit()
                    q=a[0][1]
                    c.execute("select * from customers where custid={}".format(cid))
                    b=c.fetchall()
                    k=1
                else:
                    messagebox.showinfo("Sorry","Book not Available!")
                    e1.delete(0,END)
            else:
                messagebox.showinfo("Error","Enter valid book ID!")
                e1.delete(0,END)
                e2.delete(0,END)
        else:
            messagebox.showinfo("Error","Enter all the info.!")
        
        if k==1 and b!=[]:
            c.execute("insert into transactions values({},{},'{}',{},'{}',now(),0)".format(int(AID("transactions")),bid,q,cid,b[0][1]))
            conn.commit()
            messagebox.showinfo("Success","Issued")
            e1.delete(0,END)
            e2.delete(0,END)
        elif k==1 and b==[]:
            messagebox.showinfo("Error","Enter valid customer ID!")
            c.execute("select * from books where bookid={}".format(bid))
            a=c.fetchall()
            nq=int(a[0][3])
            c.execute("update books set qty={} where bookid={}".format(int(nq+1),bid))
            conn.commit()
            e2.delete(0,END)
            e1.delete(0,END)
    def dispbook():
        t1.delete(0,END)
        c.execute("select * from books")
        a=c.fetchall()
        c.execute("select * from books where bookname like '{}%' or author like '{}%'".format(e3.get(),e3.get()))
        b=c.fetchall()
        t1.insert(0,"Book Id"+"               "+"Books"+"                  "+"Author"+"                  "+"Quantity")
        if b!=[]:
            for i in b:
                t1.insert(END,"  "+str(i[0])+"                  "+i[1]+"                  "+i[2]+"                  "+str(i[3]))
        elif a!=[] and b==[]:
            t1.insert(END,"\n")
            t1.insert(END,"  No book(s) found of given name/author                            ")
        elif a==[]:
            t1.insert(END,"\n")
            t1.insert(END,"                          No Books Found                           ")
    def dispcust():
        t2.delete(0,END)
        c.execute("select * from customers")
        a=c.fetchall()
        c.execute("select * from customers where name like '{}%' or phoneno like '{}%'".format(e4.get(),e4.get()))
        b=c.fetchall()
        t2.insert(0,"Customer ID"+"        "+"Customer Name"+"               "+"Phone No.")
        if b!=[]:
            for i in b:
                t2.insert(END,str(i[0])+"                                 "+i[1]+"                              "+str(i[2]))
        elif a==[]:
            t2.insert(END,"\n")
            t2.insert(END,"                         No Customers Found                          ")
        elif a!=[] and b==[]:
            t2.insert(END,"\n")
            t2.insert(END,"  No customer(s) found of entered name/Phone No.                            ")
    z=tkinter.Tk()
    z.title("Issue")
    z.geometry("880x550")
    z.configure(background="#00FFFF")
    l=Label(z,text="Issue a book",width=17,height=2,bg="#22CCDD",font="Jokerman")
    l.place(x=220,y=20)
    l1=Label(z,text="Books ID",bg="#00FFFF")
    l1.place(x=70,y=100)
    e1=Entry(z)
    e1.place(x=160,y=100)
    l2=Label(z,text="Customer ID",bg="#00FFFF")
    l2.place(x=60,y=130)
    e2=Entry(z)
    e2.place(x=160,y=130)
    b1=Button(z,text="Available books",command=dispbook,font="Papyrus",bg="#FF66AA")
    b1.place(x=420,y=90)
    t1=Listbox(z,width=40,height=20)
    t1.place(x=360,y=185)
    b2=Button(z,text="Available Customers",command=dispcust,font="Papyrus",bg="#FF66AA")
    b2.place(x=640,y=90)
    l3=Label(z,text="Search by name/author",bg="#00FFFF")
    l3.place(x=360,y=160)
    l4=Label(z,text="Search by name/P.No.",bg="#00FFFF")
    l4.place(x=610,y=160)
    e3=Entry(z,width=18)
    e3.place(x=490,y=160)
    e4=Entry(z,width=18)
    e4.place(x=740,y=160)
    t2=Listbox(z,width=40,height=20)
    t2.place(x=610,y=185)
    b3=Button(z,text="Issue",command=isu)
    b3.place(x=170,y=170)
    b4=Button(z,text="Back",command=z.destroy,width=10)
    b4.place(x=700,y=510)
    z.mainloop()
def defaulters():
    def disp():
        t.delete(0,END)
        c.execute("select * from transactions where status=0")
        a=c.fetchall()
        c.execute("select * from transactions where status=0 and (book like '{}%' or name like '{}%')".format(e.get(),e.get()))
        b=c.fetchall()
        t.insert(0,"Trans Id" + "          " + "Book Id" + "               " + "Book" + "             " + "Cust Id" + "                         " + "Name" + "               " + "Date & Time" + "                                " + "Status")
        if b!=[]:
            for i in b:
                t.insert(END,str(i[0]) + "                                 " + str(i[1]) + "             " + i[2] + "                " + str(i[3]) + "                      " + i[4] + "     " + str(i[5]) + "                               "+ str(i[6]))
        elif a!=[] and b==[]:
            t.insert(END," ")
            t.insert(END,"         No record(s) found of entered\n Bookname or Customer Name            ")
        elif a==[]:
            t.insert(END," ")
            t.insert(END,"                                       No Defaulters                         ")
    a=tkinter.Tk()
    a.geometry("400x480")
    a.title("Display Defaulters")
    a.configure(background="Light Green")
    b=Button(a,text="Defaulter",bg="Green",command=disp,font="Jokerman")
    b.place(x=140, y=20, width=110,height=30)
    t=Listbox(a,width=62,height=20)
    t.place(x=10,y=100)
    l=Label(a,text="Search by Customer Name/Book Name",bg="Light Green")
    l.place(x=10,y=70)
    e=Entry(a)
    e.place(x=250,y=70)
    b1=Button(a,text="Back",command=a.destroy)
    b1.place(x=350,y=440)
    a.mainloop()
def dispbooks():
    def dispb():
        t.delete(0,END)
        c.execute("select * from books")
        a=c.fetchall()
        c.execute("select * from books where bookname like '{}%' or author like '{}%'".format(e.get(),e.get()))
        b=c.fetchall()
        t.insert(0,"Book Id"+"                  "+"Books"+"                  "+"Author"+"                  "+"Quantity")
        if b!=[]:
            for i in b:
                t.insert(END,str(i[0])+"                  "+i[1]+"                  "+i[2]+"                 "+str(i[3]))
        elif a!=[] and b==[]:
            t.insert(END," ")
            t.insert(END,"               No record(s) found of entered Bookname or Author            ")
        elif a==[]:
            t.insert(END," ")
            t.insert(END,"                        No Data Entered                          ")
    a=tkinter.Tk()
    a.geometry("400x490")
    a.title("Display Books")
    a.configure(background="Purple")
    b=Button(a,text="Books",bg="Pink",command=dispb,font="Jokerman",width=10)
    b.place(x=140,y=15)
    l=Label(a,text="Search by Book_Name",bg="Purple")
    l.place(x=10,y=90)
    e=Entry(a,width=23)
    e.place(x=150,y=90)
    t=Listbox(a,width=62,height=20)
    t.place(x=10,y=120)
    b1=Button(a, text="Back",command=a.destroy)
    b1.place(x=350,y=450)
    a.mainloop()
def dispcustomers():
    def dispc():
        t.delete(0,END)
        c.execute("select * from customers")
        a=c.fetchall()
        c.execute("select * from customers where name like '{}%' or phoneno like '{}%'".format(e.get(),e.get()))
        b=c.fetchall()
        t.insert(0,"Customer ID"+"        "+"Customer Name"+"               "+"Phone No.")
        if b!=[]:
            for i in b:
                t.insert(END,str(i[0])+"                                 "+i[1]+"                              "+str(i[2]))
        elif a==[]:
            t.insert(END,"\n")
            t.insert(END,"                               No data entered                            ")
        elif a!=[] and b==[]:
            t.insert(END,"\n")
            t.insert(END,"                          No customer(s) found of entered name/Phone No.                            ")
    a=tkinter.Tk()
    a.geometry("400x490")
    a.title("Display Customers")
    a.configure(background="Indigo")
    b=Button(a,text="Customers",bg="Light Blue",command=dispc,font="Jokerman",width=12)
    b.place(x=125,y=15)
    l=Label(a,text="Search by Customer_Name",bg="Indigo")
    l.place(x=10,y=90)
    e=Entry(a,width=23)
    e.place(x=180,y=90)
    t=Listbox(a,width=63,height=20)
    t.place(x=10,y=120)
    b1=Button(a, text="Back",command=a.destroy)
    b1.place(x=350,y=450)
    a.mainloop()
def disptrans():
    def disp():
        t.delete(0,END)
        c.execute("select * from transactions")
        a=c.fetchall()
        c.execute("select * from transactions where book like '{}%' or name like '{}%'".format(e.get(),e.get()))
        b=c.fetchall()
        t.insert(0,"Trans Id" + "          " + "Book Id" + "               " + "Book" + "             " + "Cust Id" + "                         " + "Name" + "               " + "Date & Time" + "                                " + "Status")
        if b!=[]:
            for i in b:
                t.insert(END,str(i[0]) + "                                 " + str(i[1]) + "             " + i[2] + "                " + str(i[3]) + "                      " + i[4] + "     " + str(i[5]) + "                               "+ str(i[6]))
        elif a!=[] and b==[]:
            t.insert(END," ")
            t.insert(END,"         No record(s) found of entered\n Bookname or Customer Name            ")
        elif a==[]:
            t.insert(END," ")
            t.insert(END,"                        No Transactions Found                         ")
    a=tkinter.Tk()
    a.geometry("400x480")
    a.title("Display Transactions")
    a.configure(background="#530123")
    b=Button(a,text="Defaulter",bg="Red",command=disp,font="Jokerman")
    b.place(x=140, y=20, width=110,height=30)
    t=Listbox(a,width=62,height=20)
    t.place(x=10,y=100)
    l=Label(a,text="Search by Customer Name/Book Name",bg="#530123")
    l.place(x=10,y=70)
    e=Entry(a)
    e.place(x=250,y=70)
    b1=Button(a,text="Back",command=a.destroy)
    b1.place(x=350,y=440)
    a.mainloop()
def ret():
    def returnbook():
        transid=e1.get()
        k=0
        if transid!="":
            c.execute("select * from transactions where transid={}".format(transid))
            a=c.fetchall()
            if a==[]:
                messagebox.showinfo("Error","Enter valid Transaction ID!")
                e1.delete(0,END)
            elif a!=[] and a[0][6]==0:
                c.execute("select * from books where bookid={}".format(a[0][1]))
                b=c.fetchall()
                c.execute("update books set qty={} where bookid={}".format(int(b[0][3])+1,b[0][0]))
                conn.commit()
                k=1
            elif a[0][6]==1:
                messagebox.showinfo("Error","Transactions already done\n for this transaction ID")
                e1.delete(0,END)
        else:
            messagebox.showinfo("Error","Enter the Transaction ID")
        if k==1:
            c.execute("update transactions set status=1,date_of_issue_return=now() where transid={}".format(transid))
            conn.commit()
            messagebox.showinfo("Success","Reurned!")
            e1.delete(0,END)
    def disp():
        t.delete(0,END)
        c.execute("select * from transactions")
        a=c.fetchall()
        c.execute("select * from transactions where book like '{}%' or name like '{}%'".format(e2.get(),e2.get()))
        b=c.fetchall()
        t.insert(0,"Trans Id" + "          " + "Book Id" + "               " + "Book" + "             " + "Cust Id" + "                         " + "Name" + "               " + "Date & Time" + "                                " + "Status")
        if b!=[]:
            for i in b:
                t.insert(END,str(i[0]) + "                                 " + str(i[1]) + "             " + i[2] + "                " + str(i[3]) + "                      " + i[4] + "     " + str(i[5]) + "                               "+ str(i[6]))
        elif a!=[] and b==[]:
            t.insert(END," ")
            t.insert(END,"         No record(s) found of entered\n Bookname or Customer Name            ")
        elif a==[]:
            t.insert(END," ")
            t.insert(END,"                        No Transactions Found                        ")
    z=tkinter.Tk()
    z.title("Issue")
    z.geometry("700x580")
    z.configure(background="#FF00FF")
    l=Label(z,text="Return a book",width=20,height=2,bg="#FF0000",font="Jokerman")
    l.place(x=250,y=20)
    l1=Label(z,text="Transaction Id",bg="#FF00FF")
    l1.place(x=30,y=100)
    l2=Label(z,text="Search by Name/Bookname",bg="#FF00FF")
    l2.place(x=300,y=160)
    e1=Entry(z)
    e1.place(x=140,y=100)
    e2=Entry(z)
    e2.place(x=480,y=160)
    b1=Button(z,text="Transactions",command=disp,bg="#FFD700",font="Papyrus",width=13,height=1)
    b1.place(x=390,y=90)
    t=Listbox(z,width=60,height=20)
    t.place(x=300,y=190)
    b2=Button(z,text="Return",command=returnbook)
    b2.place(x=170,y=150)
    b3=Button(z,text="Back",command=z.destroy,width=10)
    b3.place(x= 500,y=520)
    z.mainloop()
def about():
    a=tkinter.Tk()
    a.title("About...")
    a.configure(background="#D2691E")
    a.geometry("200x200")
    l1=Label(a,text="This is the",bg="#D2691E")
    l2=Label(a,text="Library Management System",bg="#D2691E")
    l3=Label(a,text="created in",bg="#D2691E")
    l4=Label(a,text="Tkinter Library",bg="#D2691E")
    l5=Label(a,text="in Python...",bg="#D2691E")
    l6=Label(a,text="~Kshitij Agarwal",bg="#8B4513")
    l1.place(x=60,y=10)
    l2.place(x=30,y=30)
    l3.place(x=60,y=50)
    l4.place(x=50,y=70)
    l5.place(x=60,y=90)
    l6.place(x=100,y=160)
l=Label(k,text="Library Management",width=20,height=2,bg="#E2E5E8",font="ArialRoundedMTBold",borderwidth=3,relief="ridge")
l.place(x=100,y=20)
l1=Button(k,text="Add a book",command=addbooks,bg="#C2C5C8",font="BahnschriftSemiLight",width=10,borderwidth=1)
l1.place(x=150,y=100)
l2=Button(k,text="Delete a book",command=delbook,bg="#C2C5C8",font="BahnschriftSemiLight",width=13,borderwidth=1)
l2.place(x=135,y=150)
l3=Button(k,text="Add a customer",command=addcustomer,bg="#C2C5C8",font="BahnschriftSemiLight",width=15,borderwidth=1)
l3.place(x=125,y=200)
l4=Button(k,text="Delete a customer",command=deletecustomer,bg="#C2C5C8",font="BahnschriftSemiLight",width=15,borderwidth=1)
l4.place(x=125,y=250)
l5=Button(k,text="Issue a Book",command=issue,bg="#C2C5C8",font="BahnschriftSemiLight",width=13,borderwidth=1)
l5.place(x=135,y=300)
l6=Button(k,text="Defaulters",command=defaulters,bg="#C2C5C8",font="BahnschriftSemiLight",width=9,borderwidth=1)
l6.place(x=160,y=350)
l7=Button(k,text="Display Books",command=dispbooks,bg="#C2C5C8",font="BahnschriftSemiLight",width=13,borderwidth=1)
l7.place(x=135,y=400)
l8=Button(k,text="Display Customers",command=dispcustomers,bg="#C2C5C8",font="BahnschriftSemiLight",width=15,borderwidth=1)
l8.place(x=125,y=450)
l9=Button(k,text="Display transactions",command=disptrans,bg="#C2C5C8",font="BahnschriftSemiLight",width=17,borderwidth=1)
l9.place(x=110,y=500)
l10=Button(k,text="Return Book",command=ret,bg="#C2C5C8",font="BahnschriftSemiLight",width=13,borderwidth=1)
l10.place(x=135,y=550)
menubar = Menu(k)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Exit", command=k.destroy)
menubar.add_cascade(label="File", menu=filemenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About...",command=about)
menubar.add_cascade(label="Help", menu=helpmenu)
k.config(menu=menubar)
k.mainloop()