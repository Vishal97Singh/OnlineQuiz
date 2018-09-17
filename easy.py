from Tkinter import*
top4 = Tk()
def set1():
    top4.destroy()
    import set1
def set2():
    top4.destroy()
    import set2
f=open("name.txt","r")
tex=f.readline(20)
f.close()
l=Label(top4, text="Welcome ",fg="black",font=("ROSEWOOD STD REGULAR",30,"bold"),bd=10).grid(row=0,column=1)
l=Label(top4, text=tex,fg="black",font=("ROSEWOOD STD REGULAR",30,"bold"),bd=10).grid(row=0,column=2)

l1=Button(top4, text="Enter your choice",fg="red",font=("ROSEWOOD STD REGULAR",50,"bold"),bd=10).grid(row=1,column=0)

l1=Button(top4, text="Set 1",fg="black",command=set1,font=("ROSEWOOD STD REGULAR",40,"bold"),bd=10).grid(row=2,column=0)
l1=Button(top4, text="Set 2",fg="black",command=set2,font=("ROSEWOOD STD REGULAR",40,"bold"),bd=10).grid(row=2,column=1)
def home():
    top4.destroy()
    import main
b2=Button(top4,text="Home",font="500",bg="red",command=home,fg="white").grid(row=1000,column=1)

top4.mainloop()
