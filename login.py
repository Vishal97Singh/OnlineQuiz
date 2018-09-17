from Tkinter import*
import tkMessageBox
import sqlite3

top1=Tk()
def forgot():
    top1.destroy()
    import forgot
        
def main():
    top1.destroy()
    import main
def level():
    top1.destroy()
    import level
def check():
    f=open("email.txt","r")
    text=f.readline(20)
    f=open("password.txt","r")
    passw=f.readline(20)
    if(text==str(e1.get()) and passw==str(e2.get())):
        t=tkMessageBox.showinfo("alert","Log in Successful")
        level()
    else:
        t=tkMessageBox.showinfo("alert","Invalid username or password") 

l1=Label(top1, text="Login",fg="black",font=("ROSEWOOD STD REGULAR",50,"bold"),bd=10).grid(row=1,column=5)
l5=Label(top1, text="Email id:",fg="blue",font=("ROSEWOOD STD REGULAR",20,"italic"),bd=10).grid(row=6)
l6=Label(top1, text="Password:",fg="blue",font=("ROSEWOOD STD REGULAR",20,"italic"),bd=10).grid(row=7)
e1 = Entry(top1,relief=GROOVE,bg='gray',width='40')
e2 = Entry(top1,relief=GROOVE,bg='gray',show="*",width='40')
e1.grid(row=6,column=1)
e2.grid(row=7,column=1)
b1=Button(top1,text="Login",font=("ROSEWOOD STD REGULAR",20,"bold"),bg="gray",fg="black",command=check).grid(row=12,column=2)
b1=Button(top1,text="forgot password?",font=("ROSEWOOD STD REGULAR",20,"bold"),bg="gray",fg="black",command=forgot).grid(row=14,column=2)
b1=Button(top1,text="Go to HOME ",command=main,bg="red",font=("Rockwell Extra Bold",20,"bold"),fg="white").grid(row=20,column=0)
top1.mainloop()
