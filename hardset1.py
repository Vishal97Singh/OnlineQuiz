import tkMessageBox
from Tkinter import*
top = Tk()
def home():
    top.destroy()
    import main
def back():
    top.destroy()
    import hard
l1=Button(top, text="Set 1",fg="black",font=("ROSEWOOD STD REGULAR",40,"bold"),bd=10).grid(row=0)

a=["1)t=(1,2,4,3,8,9),then t[i] for i in range(0,len(t)","Q2)Which is not attributes of file?","Q3)  What is the use of seek() method in files?","Q4)Output of invalid file in read mode","Q5)  What happens when str 1 == 1 is executed?"]
b=[" [1, 4, 8]","rename","set files current position at the offset","value error","we get a false"," a b c = 1000 2000 3000", "5","2"," two stars followed by a valid identifier","3"]
c=["[2,3,9]","mode","set files previous position at the offset","IOerror","we get a true"," abc = 1,000,000","1","0","one star followed by a valid identifier","27"]
d=["[1,2,4,3,8,9]","softspace","set files current position within the file","Invalid error","an TypeError occures"," a,b,c = 1000, 2000, 3000",2,4," one underscore followed by a valid identifier","9"]
e=["(1,4,8)","closed","None ","none","ValueError occurs","a_b_c = 1,000,000","4","error","two underscores followed by a valid identifier","1"]
def score():
    f=open("name.txt","r")
    t=f.read(50)
    f.close()
    t=tkMessageBox.askquestion(t,"Do you want to submit")
    t=tkMessageBox.showinfo(t,count)
    top.destroy()
    import level
x=IntVar()
y=IntVar()
z=IntVar()
p=IntVar()
q=IntVar()
var=[x,y,z,p,q]
global count
count=0

def check():
    temp=0
    global count
    for i in range(0,5):
            if (var[i].get())==2:
                count=count+1
            else:
                count=count-0.25
    score()
            #print temp
for i in range(0,5):
         l=Label(top, text=a[i],fg="red",font=("times new roman",20,"bold italic"),bd=10).grid(row=1+(5*i),column=0)
         r1=Radiobutton(top,text=b[i],variable=var[i],value=1,font=("times new roman",15,"bold italic")).grid(row=1+(5*i)+1,column=0)
         r2=Radiobutton(top,text=c[i],variable=var[i],value=2,font=("times new roman",15,"bold italic")).grid(row=1+(5*i)+1,column=1)
         r3=Radiobutton(top,text=d[i],variable=var[i],value=3,font=("times new roman",15,"bold italic")).grid(row=1+(5*i)+1,column=2)
         r4=Radiobutton(top,text=e[i],variable=var[i],value=4,font=("times new roman",15,"bold italic")).grid(row=1+(5*i)+1,column=3)
b2=Button(top,text="Home",font="500",bg="red",command=home,fg="white").grid(row=1000,column=0)
b3=Button(top,text="Back",font="500",bg="red",command=back,fg="white").grid(row=1000,column=1)
b4=Button(top,text="Submit",font="500",bg="red",fg="white",command=check).grid(row=1000,column=2)
top.mainloop()

