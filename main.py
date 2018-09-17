from Tkinter import*
import tkMessageBox
top=Tk()
def main():
    top.destroy()
    import main

def login():
    top.destroy()
    import login
def register():
    top.destroy()
    import register
def about():
    top.destroy()
    import about

l=Label(top, text="Welcome to Quiz",fg="black",font=("ROSEWOOD STD REGULAR",50,"bold"),bd=10).grid(row=1)
b1=Button(top,text="HOME ",command=main,bg="red",font=("Rockwell Extra Bold",20,"bold"),fg="white").grid(row=2,column=0)

b1=Button(top,text="Log in ",command=login,bg="red",font=("Rockwell Extra Bold",20,"bold"),fg="white").grid(row=3,column=0)
b1=Button(top,text="Register",command=register,bg="red",font=("Rockwell Extra Bold",20,"bold"),fg="white").grid(row=4,column=0)
b1=Button(top,text="About us",command=about,bg="red",font=("Rockwell Extra Bold",20,"bold"),fg="white").grid(row=6,column=0)
l=Label(top, text="This is python quiz wap. It consist of three levels:-Easy,Medium and hard",fg="blue",font=("times new roman",20,"italic"),bd=10).grid(row=7)
l=Label(top, text="You have to login or register for accessing the quiz",fg="blue",font=("times new roman",20,"italic"),bd=10).grid(row=8)
l=Label(top, text="This wap is copyright of VLR and company.",fg="blue",font=("times new roman",20,"italic"),bd=10).grid(row=9)
l=Label(top, text="Any imitation and copy is strictly prohibited",fg="blue",font=("times new roman",20,"italic"),bd=10).grid(row=10)


top.mainloop()
