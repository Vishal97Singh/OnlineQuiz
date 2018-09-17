from Tkinter import*
import tkMessageBox
import sqlite3
top3=Tk()
l=Label(top3, text="Welcome to Quiz",fg="black",font=("ROSEWOOD STD REGULAR",50,"bold"),bd=10).grid(row=0,column=3)
l1=Label(top3, text="Name:*",font=("times new roman",20,"italic"),fg="red",bd=10).grid(row=5,column=1)
l2=Label(top3, text="Registration NO:*",font=("times new roman",20,"italic"),fg="dark blue",bd=10).grid(row=6,column=1)
l3=Label(top3, text="Section:*",fg="blue",font=("times new roman",20,"italic"),bd=10).grid(row=7,column=1)
l4=Label(top3, text="Stream:",fg="blue",font=("times new roman",20,"italic"),bd=10).grid(row=8,column=1)
l5=Label(top3, text="Email id:*",fg="blue",font=("times new roman",20,"italic"),bd=10).grid(row=9,column=1)
l6=Label(top3, text="Password:*",fg="blue",font=("times new roman",20,"italic"),bd=10).grid(row=10,column=1)
l7=Label(top3, text="Confirm password:*",fg="blue",font=("times new roman",20,"italic"),bd=10).grid(row=11,column=1)
l7=Label(top3, text="What is your Nick name?*:",fg="blue",font=("times new roman",20,"italic"),bd=10).grid(row=12,column=1)
e1 = Entry(top3,relief=GROOVE,bg='gray',width='40')
e2 = Entry(top3,relief=GROOVE,bg='gray',width='40')
e3= Entry(top3,relief=GROOVE,bg='gray',width='40')
e4= Entry(top3,relief=GROOVE,bg='gray',width='40')
e5= Entry(top3,relief=GROOVE,bg='gray',width='40')
e6= Entry(top3,relief=GROOVE,show="*",bg='gray',width='40')
e7= Entry(top3,relief=GROOVE,show="*",bg='gray',width='40')
e8= Entry(top3,relief=GROOVE,bg='gray',width='40')

global a,b,c,d,e,f
e1.grid(row=5, column=2)
e2.grid(row=6, column=2)
e3.grid(row=7,column=2)
e4.grid(row=8,column=2)
e5.grid(row=9,column=2)
e8.grid(row=12,column=2)

e6.grid(row=10,column=2)
e7.grid(row=11,column=2)
def login():
    top3.destroy()
    import login
def main():
    top3.destroy()
    import main
def reg():
    global a,b,c,d,e,f
    a=str(e1.get())
    b=e2.get()
    c=str(e3.get())
    d=str(e4.get())
    e=str(e5.get())
    f=str(e6.get())
    g=str(e7.get())
    h=str(e8.get())
    if f!=g:
        t=tkMessageBox.showinfo("Alert","Error occurred!!!!!!!!                    Please Use same password for confirmation")
    else:
        file1=open("name.txt","w")
        file1.write(a)
        file1=open("reg.txt","w")
        file1.write(b)
        file1=open("section.txt","w")
        file1.write(c)
        file1=open("email.txt","w")
        file1.write(e)
        file1=open("password.txt","w")
        file1.write(f)
        file1=open("security.txt","w")
        file1.write(h)
        t=tkMessageBox.showinfo("alert","Successfully registered")
        file1.close()
        login()
b1=Button(top3,text="Register",font=("ROSEWOOD STD REGULAR",20,"bold"),bg="gray",fg="black",command=reg).grid(row=14,column=2)

b1=Button(top3,text="Go to HOME ",command=main,bg="red",font=("Rockwell Extra Bold",20,"bold"),fg="white").grid(row=20,column=0)
top3.mainloop()
