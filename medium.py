from Tkinter import*
top = Tk()
def set1():
    top.destroy()
    import medset1
def set2():
    top.destroy()
    import medset2
f=open("name.txt","r")
tex=f.readline(20)
f.close()
l=Label(top, text="Welcome ",fg="black",font=("ROSEWOOD STD REGULAR",30,"bold"),bd=10).grid(row=0,column=2)
l=Label(top, text=tex,fg="black",font=("ROSEWOOD STD REGULAR",30,"bold"),bd=10).grid(row=0,column=3)

l1=Button(top, text="Enter choice",fg="red",font=("ROSEWOOD STD REGULAR",50,"bold"),bd=10).grid(row=1,column=0)

l1=Button(top, text="Medium Set 1",fg="black",command=set1,font=("ROSEWOOD STD REGULAR",40,"bold"),bd=10).grid(row=2,column=0)
l1=Button(top, text="Medium Set 2",fg="black",command=set2,font=("ROSEWOOD STD REGULAR",40,"bold"),bd=10).grid(row=2,column=1)
def home():
    top.destroy()
    import main
b2=Button(top,text="Home",font="500",bg="red",command=home,fg="white").grid(row=1000,column=1)

top.mainloop()
