from Tkinter import*
import tkMessageBox
top5 = Tk()
def home():
    top5.destroy()
    import main
def back():
    top5.destroy()
    import easy
l1=Button(top5, text="Set 1",fg="black",font=("ROSEWOOD STD REGULAR",40,"bold"),bd=10).grid(row=0)

a=["Q1)Python is a/an________","Q2) What is the output of print str * 2 if str = 'Hello World!'?","Q3)What is correct for print tinylist * 2 if tinylist = [123, 'john']?","Q4)How to convert an integer to octal string in python?","Q5) What is the output of L[2] if L = [1,2,3]?","Q6) Who developed python?","Q7) Suppose list1 is [2445,133,12454,123], what is max(list1) ?","Q8) Suppose list1 is [2, 33, 222, 14, 25], What is list1[-1] ?","Q9) Which of the following is a Python tuple?","Q10) What will be the output? if t=(1,2,4,3),t[1:3]=?"] 
b=["Structured language"," Hello World! * 2","[123, 'john'] * 2","dec(x)","error","Guido Pan rossum ",2445,"Error","1,3,3","1,2"]
c=["object oriented","Hello World!Hello World!","[123, 'john', 123, 'john']","oct(x)","3"," Guido van Rossum",12454,25,"1,2,3","2,4"]
d=["scripting language","Hello World!"," Error","hex(x)","1","Banki moon","Error","none","[1,1,3]","1,2,4"]
e=["markup language","None of the above"," None of the above","unichar(x)","2","Dennis Ritchie","123","2","1,1,2","2,4,3"]
def score():
    f=open("name.txt","r")
    t=f.read(50)
    f1=open("marks.txt","w")
    f1.write(str(count))
    f.close()
    t=tkMessageBox.askquestion(t,"Do you want to submit")
    
    t=tkMessageBox.showinfo(t,count)
    top5.destroy()
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
         l=Label(top5, text=a[i],fg="red",font=("times new roman",20,"bold italic"),bd=10).grid(row=1+(5*i),column=0)
         r1=Radiobutton(top5,text=b[i],variable=var[i],value=1,font=("times new roman",15,"bold italic")).grid(row=1+(5*i)+1,column=0)
         r2=Radiobutton(top5,text=c[i],variable=var[i],value=2,font=("times new roman",15,"bold italic")).grid(row=1+(5*i)+1,column=1)
         r3=Radiobutton(top5,text=d[i],variable=var[i],value=3,font=("times new roman",15,"bold italic")).grid(row=1+(5*i)+1,column=2)
         r4=Radiobutton(top5,text=e[i],variable=var[i],value=4,font=("times new roman",15,"bold italic")).grid(row=1+(5*i)+1,column=3)
b2=Button(top5,text="Home",font="500",bg="red",command=home,fg="white").grid(row=1000,column=1)
b3=Button(top5,text="Back",font="500",bg="red",command=back,fg="white").grid(row=1000,column=2)
b4=Button(top5,text="Submit",font="500",bg="red",fg="white",command=check).grid(row=1000,column=3)
top5.mainloop()
