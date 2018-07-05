from tkinter import *

# #ques 1:
# a=Tk()
# dic = {"Abhay": 223, "aditya": 354,"Madhav": 856, "palvi mahajan": 778,}
#
# L3=Label(a,text=" ")
# L3.grid(row=1,column=1)
# def show(evt):
#      L3.config(text=dic[l1.get(l1.curselection())])
# L1=Label(a,text="Name:")
# L1.grid(row=0,column=0)
# L2=Label(a,text="Mobile Number:")
# L2.grid(row=0,column=1)
# s1=Scrollbar(a,orient=VERTICAL)
#
# l1=Listbox(a,height=7,yscrollcommand=s1.set)
# for i in dic.keys():
#       l1.insert(END,i)
# s1.config(command=l1.yview)
# l1.grid(row=1,column=0,rowspan=3)
# s1.grid(row=1,column=0,rowspan=3,sticky=E+N+S)
# l1.bind("<<ListboxSelect>>",show)
# a.mainloop()

#ques 2:


root=Tk()
mi = {"tanya": 758,"Aditya": 973, "Aanchal": 202, "palvi mahajan": 457}
x = StringVar()
y=StringVar()
listb=Label(root,text=" ")
listb.grid(row=1,column=1)
def show(evt):
    listb.config(text=mi[lab.get(lab.curselection())])
def show1():
    mi[x.get()]=y.get()
    print(mi)
    show2()
Lab=Label(root,text="Name:")
Lab.grid(row=0,column=0)
Lab2=Label(root,text="Mobile Number:")
Lab2.grid(row=0,column=1)
scr1=Scrollbar(root,orient=VERTICAL)
lab=Listbox(root,height=10,yscrollcommand=scr1.set,exportselection=0)
def show2():
    for i in mi.keys():
        lab.insert(END, i)
        print(i)
    scr1.config(command=lab.yview)
    lab.grid(row=1, column=0, rowspan=3)
    scr1.grid(row=1, column=0, rowspan=3)
    lab.bind("<<ListboxSelect>>", show)
show2()
lab4=Label(root,text="enter name=")
lab4.grid(row=4,column=0)
lab5=Label(root,text="Enter mobile number=")
lab5.grid(row=4,column=1)
eb1=Entry(root,textvariable=x)
eb1.grid(row=5,column=0)
eb2=Entry(root,textvariable=y)
eb2.grid(row=5,column=1)
b1=Button(root,text="Refresh",command=show1)
b1.grid(row=6)
root.mainloop()