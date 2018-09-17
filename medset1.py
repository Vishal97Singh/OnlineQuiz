from Tkinter import*
import tkMessageBox
top = Tk()
def home():
    top.destroy()
    import main
def back():
    top.destroy()
    import medium
l1=Button(top, text="Set 1",fg="black",font=("ROSEWOOD STD REGULAR",40,"bold"),bd=10).grid(row=0)
a=["Q1)Output?if t=(1,2,4,3) then t[1:-1]=?","Q2)output? if t1 = (1, 2, 4, 3),t2=(1, 2, 3, 4),then t1 < t2","Q3)  Which keyword is use for function?","Q4) To read two characters from a file object infile, we use","Q5) What is the currect syntax of remove() a file?"]
b=["(2,4)","False","def","infile.read(2)","remove(file_name)"]
c=["(1,2)","True","define","infile.read()"," remove(newfile,currentfile)"]
d=["(1,2,4)","Error","fun","infile.readline()","None"]
e=["(2,4,3)","None","function","infile.readlines()","remove((),file_name))"]
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
