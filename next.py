from Tkinter import*
top = Tk()
a=["Q1)Python is a________","Q2) What is the output of print str * 2 if str = 'Hello World!'?","Q3)  What is the output of print tinylist * 2 if tinylist = [123, 'john']?","Q4) Which of the following function convert an integer to octal string in python?","Q5) What is the output of L[2] if L = [1,2,3]?","Q6) Who developed python?","Q7) Suppose list1 is [2445,133,12454,123], what is max(list1) ?","Q8) Suppose list1 is [2, 33, 222, 14, 25], What is list1[-1] ?","Q9) Which of the following is a Python tuple?","Q10) What will be the output? if t=(1,2,4,3),t[1:3]=?"] 
b=["Structured language"," Hello World! * 2","[123, 'john'] * 2","dec(x)","error"," hello ",2445,"Error","1,3,3","1,2"]
c=["object oriented","Hello World!Hello World!","[123, 'john', 123, 'john']","oct(x)","3"," [h, e, l, l, o ]",12454,25,"1,2,3","2,4"]
d=["scripting language","Hello World!"," Error","hex(x)","1"," llo","Error","none","[1,1,3]","1,2,4"]
e=["markup language","None of the above"," None of the above","unichar(x)","2","olleh ","123","2","1,1,2","2,4,3"]
i=0
k=i
l=Label(top, text=a[i],fg="red",font="50",bd=10).grid(row=0)
r1=Radiobutton(top,text=b[i],variable=k,value=1,font="150").grid(row=2)
r2=Radiobutton(top,text=c[i],variable=k,value=2,font="150").grid(row=3)
r3=Radiobutton(top,text=d[i],variable=k,value=3,font="150").grid(row=4)
r4=Radiobutton(top,text=e[i],variable=k,value=4,font="150").grid(row=5)
top.mainloop()
