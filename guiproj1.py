from tkinter import *
from tkinter import messagebox as mb
root = Tk()
root.title("Student Electives Suggestor")
root.geometry('500x100')
e = Label(root,text = "Name :").grid(row = 10,column=10)
s = Entry(root,width = 35, borderwidth =5)
s.grid(row =10,column = 11,columnspan =3, padx = 10, pady =10)
name  = s.get()
f = Label(root,text = "SRN : ").grid(row = 11, column =10)
t = Entry(root,width = 35, borderwidth = 5)
t.grid(row = 11, column =11,columnspan = 3, padx =10, pady =10)
srn = t.get()
b2 = Button(text = "Next",)
b2.grid(row = 13, column =13)
root.mainloop()