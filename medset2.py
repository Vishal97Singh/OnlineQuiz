from Tkinter import*
import tkMessageBox
top = Tk()
def home():
    top.destroy()
    import main
def back():
    top.destroy()
    import medium
l1=Button(top, text="Set 2",fg="black",font=("ROSEWOOD STD REGULAR",40,"bold"),bd=10).grid(row=0)
a=["Q6)output?if d = {john:40,peter:45},then print(list(d.keys()))","Q7) What is the output of hello+1+2+3 ?","Q8)How many except statements can a try-except block have?","Q9)Which operator is overloaded by the __or__() function?","Q10) Which of the following is invalid?"]
b=["[john,peter]","Error","more than zero","|","none"]
c=[" [john:40, peter:45]","hello123","zero","||","_a"]
d=[" (john, peter)","hello","one","//","__a"]
e=[" (john:40,peter:46)","hello6","more than one","/","__a__"]
def score():
    f=open("name.txt","r")
    t=f.read(50)
    f.close()
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
b2=Button(top,text="Home",font="500",bg="red",command=home,fg="white").grid(row=1000,column=1)
b3=Button(top,text="Back",font="500",bg="red",command=back,fg="white").grid(row=1000,column=2)
b4=Button(top,text="Submit",font="500",bg="red",fg="white",command=check).grid(row=1000,column=3)
top.mainloop()
