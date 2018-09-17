from Tkinter import *
import tkMessageBox
top = Tk()
l=Label(top, text="Welcome to Quiz",fg="black",font=("ROSEWOOD STD REGULAR",50,"bold"),bd=10).grid(row=1,column=5)
l1=Label(top, text="Email id:",font="150",height=2,width=10,fg="red",bd=10).grid(row=5,column=1)
l2=Label(top, text="Password:",font="150",fg="red",bd=10).grid(row=6,column=1)
e1 = Entry(top,relief=GROOVE,bg='gray',width='20')
e2 = Entry(top,relief=GROOVE,bg='gray',width='20')
e1.grid(row=5, column=2)
e2.grid(row=6, column=2)
count=0
a=["Q1)Python is a________","Q2) What is the output of print str * 2 if str = 'Hello World!'?","Q3)  What is the output of print tinylist * 2 if tinylist = [123, 'john']?","Q4) Which of the following function convert an integer to octal string in python?","Q5) What is the output of L[2] if L = [1,2,3]?","Q6) Who developed python?","Q7) Suppose list1 is [2445,133,12454,123], what is max(list1) ?","Q8) Suppose list1 is [2, 33, 222, 14, 25], What is list1[-1] ?","Q9) Which of the following is a Python tuple?","Q10) What will be the output? if t=(1,2,4,3),t[1:3]=?"] 
b=["Structured language"," Hello World! * 2","[123, 'john'] * 2","dec(x)","error"," hello ",2445,"Error","1,3,3","1,2"]

c=["object oriented","Hello World!Hello World!","[123, 'john', 123, 'john']","oct(x)","3"," [h, e, l, l, o ]",12454,25,"1,2,3","2,4"]
d=["scripting language","Hello World!"," Error","hex(x)","1"," llo","Error","none","[1,1,3]","1,2,4"]
e=["markup language","None of the above"," None of the above","unichar(x)","2","olleh ","123","2","1,1,2","2,4,3"]
global i
i=0
def next():
    global i
    l=Label(top, text=a[i],fg="red",font="500",bd=10).grid(row=0)
    i=i+1

def count():
    if k.get()==2:
        count=count+1
    print "Your score:",count
k=IntVar()
def easy():
    top.destroy()
    import easy

def info():
    f=open("info.txt","w")
    f.write(str(e1.get()))
    f.write(str(e2.get()))
    f.close()
    if(var.get()==1):
        easy()
    if(var.get()==2):
        medium()
    if(var.get()==3):
        hard()
var=IntVar()
l4=Label(top,text="Level",font="150",fg='magenta',bd=10).grid(row=9)
r1=Radiobutton(top,text="Easy",variable=var,value=1,activebackground='red',font=("Rockwell Extra Bold",20,"bold"),bg='green').grid(row=9,column=1)
r2=Radiobutton(top,text="Medium",variable=var,value=2,activebackground='red',font=("Rockwell Extra Bold",20,"bold"),bg='Yellow').grid(row=9,column=2)
r3=Radiobutton(top,text="Hard",variable=var,value=3,activebackground='red',font=("Rockwell Extra Bold",20,"bold"),bg='red').grid(row=9,column=3)
b1=Button(top,text="Submit",bg="red",font=("Rockwell Extra Bold",20,"bold"),fg="white",command=info).grid(row=10,column=4)

top.mainloop()

