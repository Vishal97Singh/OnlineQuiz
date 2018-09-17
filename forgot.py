from Tkinter import*
import tkMessageBox
top2 = Tk()
def check():
    f1=open("security.txt","r")
    re=f1.read(40)
    f1=open("password.txt","r")
    passw=f1.read(40)
    f1.close()
    if(re==e2.get()):
        t=tkMessageBox.showinfo("alert","Your Password is  :   "+passw)
        top2.destroy()
        import login
    else:
        t=tkMessageBox.showerror("alert","You have entered wrong email id or security answer")
    
l1=Label(top2, text="Enter your email id",fg="black",font=("ROSEWOOD STD REGULAR",20,"bold"),bd=10).grid(row=1,column=1)
l5=Label(top2, text="What is your nick name?:",fg="black",font=("ROSEWOOD STD REGULAR",20,"italic"),bd=10).grid(row=2,column=1)
e1 = Entry(top2,relief=GROOVE,bg='gray',width='40')
e2 = Entry(top2,relief=GROOVE,bg='gray',width='40')
e1.grid(row=1,column=2)
e2.grid(row=2,column=2)
b1=Button(top2,text="Submit",font=("ROSEWOOD STD REGULAR",20,"bold"),bg="gray",fg="black",command=check).grid(row=3,column=2)
top2.mainloop()
