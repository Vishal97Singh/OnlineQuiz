from Tkinter import*
import tkMessageBox
top7=Tk()
var=IntVar()
def marks():
    def main():
       t.destroy()
       import main
    top7.destroy()
    t=Tk()
    f=open("name.txt")
    l=Label(t, text="Welcome to Quiz",fg="black",font=("ROSEWOOD STD REGULAR",50,"bold"),bd=10).grid(row=0,column=3)
    l1=Label(t, text="Name:",font=("times new roman",20,"italic"),fg="blue",bd=10).grid(row=1,column=1)
    l2=Label(t, text="Registration NO:",font=("times new roman",20,"italic"),fg="blue",bd=10).grid(row=2,column=1)
    l3=Label(t, text="Section:",fg="blue",font=("times new roman",20,"italic"),bd=10).grid(row=3,column=1)
    l4=Label(t, text="Marks:",fg="blue",font=("times new roman",20,"italic"),bd=10).grid(row=4,column=1)
    l5=Label(t, text="Email id:",fg="blue",font=("times new roman",20,"italic"),bd=10).grid(row=5,column=1)
    file1=open("name.txt","r")
    name=file1.readline(30)
    file1=open("reg.txt","r")
    reg=file1.readline(30)
    file1=open("section.txt","r")
    sec=file1.readline(30)
    file1=open("email.txt","r")
    mail=file1.readline(30)
    file1=open("marks.txt","r")
    marks=file1.readline(30)
    l=Label(t, text=name,fg="blue",font=("times new roman",20,"italic"),bd=10).grid(row=1,column=2)
    l1=Label(t, text=reg,font=("times new roman",20,"italic"),fg="blue",bd=10).grid(row=2,column=2)
    l2=Label(t, text=sec,font=("times new roman",20,"italic"),fg="blue",bd=10).grid(row=3,column=2)
    l3=Label(t, text=mail,fg="blue",font=("times new roman",20,"italic"),bd=10).grid(row=5,column=2)
    l5=Label(t, text=float(marks),fg="blue",font=("times new roman",20,"italic"),bd=10).grid(row=4,column=2)
    b1=Button(t,text="Go to HOME ",command=main,bg="red",font=("Rockwell Extra Bold",20,"bold"),fg="white").grid(row=20,column=0)
    
def easy():
    top7.destroy()
    import easy
def medium():
    top7.destroy()
    import medium
def hard():
    top7.destroy()
    import hard
def main():
    top7.destroy()
    import main
f=open("name.txt","r")
tex=f.readline(20)
f.close()
l=Label(top7, text="Welcome to Quiz",fg="black",font=("ROSEWOOD STD REGULAR",50,"bold"),bd=10).grid(row=1)
l=Label(top7, text=tex,fg="black",font=("ROSEWOOD STD REGULAR",30,"bold"),bd=10).grid(row=2)
l=Label(top7, text="Choose Level of Python Quiz",fg="black",font=("ROSEWOOD STD REGULAR",30,"bold"),bd=10).grid(row=3)
r1=Radiobutton(top7,text="Easy",variable=var,value=1,activebackground='red',font=("Rockwell Extra Bold",20,"bold"),bg='green',command=easy).grid(row=4)
r2=Radiobutton(top7,text="Medium",variable=var,value=2,activebackground='red',font=("Rockwell Extra Bold",20,"bold"),bg='Yellow',command=medium).grid(row=5)
r3=Radiobutton(top7,text="Hard",variable=var,value=3,activebackground='red',font=("Rockwell Extra Bold",20,"bold"),bg='red',command=hard).grid(row=6)
l=Label(top7, text="All questions are compulsory",fg="black",font=("times new roman",30,"bold"),bd=10).grid(row=9)

l=Label(top7, text="0.25 will be deducted for unattempted or wrong answer",fg="black",font=("times new roman",30,"bold"),bd=10).grid(row=10)
l=Label(top7, text="1 marks will be awarded for correct answer",fg="black",font=("times new roman",30,"bold"),bd=10).grid(row=11)
b1=Button(top7,text="Go to HOME ",command=main,bg="red",font=("Rockwell Extra Bold",20,"bold"),fg="white").grid(row=20,column=0)
b1=Button(top7,text="Know your previous marks ",command=marks,bg="red",font=("Rockwell Extra Bold",20,"bold"),fg="white").grid(row=20,column=1)
top7.mainloop()

