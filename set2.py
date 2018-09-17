from Tkinter import*
import tkMessageBox
top6 = Tk()
l1=Button(top6, text="Set 2",fg="black",font=("ROSEWOOD STD REGULAR",40,"bold"),bd=10).grid(row=0)

def home():
    top6.destroy()
    import main
def back():
    top6.destroy()
    import easy
    
a=["Q6) Who developed python?","Q7) Suppose list1 is [2445,133,12454,123], what is max(list1) ?","Q8) Suppose list1 is [2, 33, 222, 14, 25], What is list1[-1] ?","Q9) Which of the following is a Python tuple?","Q10) What will be the output? if t=(1,2,4,3),t[1:3]=?"] 
b=["Guido Pan rossum ",2445,"Error","1,3,3","1,2"]
c=[" Guido van Rossum",12454,25,"1,2,3","2,4"]
d=["Banki moon","Error","none","[1,1,3]","1,2,4"]
e=["Dennis Ritchie","123","2","1,1,2","2,4,3"]
def score():
    f=open("name.txt","r")
    t=f.read(50)
    f.close()
    t=tkMessageBox.showinfo(t,count)
    top6.destroy()
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
         l=Label(top6, text=a[i],fg="red",font=("times new roman",20,"bold italic"),bd=10).grid(row=1+(5*i),column=0)
         r1=Radiobutton(top6,text=b[i],variable=var[i],value=1,font=("times new roman",15,"bold italic")).grid(row=1+(5*i)+1,column=0)
         r2=Radiobutton(top6,text=c[i],variable=var[i],value=2,font=("times new roman",15,"bold italic")).grid(row=1+(5*i)+1,column=1)
         r3=Radiobutton(top6,text=d[i],variable=var[i],value=3,font=("times new roman",15,"bold italic")).grid(row=1+(5*i)+1,column=2)
         r4=Radiobutton(top6,text=e[i],variable=var[i],value=4,font=("times new roman",15,"bold italic")).grid(row=1+(5*i)+1,column=3)
b2=Button(top6,text="Home",font="500",bg="red",command=home,fg="white").grid(row=1000,column=1)
b3=Button(top6,text="Back",font="500",bg="red",command=back,fg="white").grid(row=1000,column=2)
 
b4=Button(top6,text="Submit",font="500",bg="red",command=check,fg="white").grid(row=1000,column=10)
top6.mainloop()
