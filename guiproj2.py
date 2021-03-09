from tkinter import *
from tkinter import ttk
root  = Tk()
root.geometry('500x300')
root.title("Intrests")
l = ttk.Label(root,text = "Enter your intrests one  by one in an order of decreasing priority in them").grid(row = 0 , column =0)
l1 = ttk.Label(root, text ="Interst 1:").grid (row = 1, column = 0)
n=""
d1 = ttk.Combobox(root, width = 27, textvariable = n)
d1['values'] = ["Intrest1","Intrest2","Intrest3","Intrest4","interst5"]
d1.grid(row = 1,column =1)
d1.current()
l2 = ttk.Label(root, text ="Interst 2:").grid (row = 2, column = 0)
m=""
d2 = ttk.Combobox(root, width = 27, textvariable = m)
d2['values'] = ["Intrest1","Intrest2","Intrest3","Intrest4","interst5"]
d2.grid(row = 2,column =1)
d2.current()
l3 = ttk.Label(root, text ="Interst 3:").grid (row = 3, column = 0)
q=""
d3 = ttk.Combobox(root, width = 27, textvariable = q)
d3['values'] = ["Intrest1","Intrest2","Intrest3","Intrest4","interst5"]
d3.grid(row = 3,column =1)
d3.current()
l4 = ttk.Label(root, text ="Interst 4:").grid (row = 4, column = 0)
r=""
d4 = ttk.Combobox(root, width = 27, textvariable = r)
d4['values'] = ["Intrest1","Intrest2","Intrest3","Intrest4","interst5"]
d4.grid(row = 4,column =1)
d4.current()
l5 = ttk.Label(root, text ="Interst 1:").grid (row = 5, column = 0)
w=""
d5 = ttk.Combobox(root, width = 27, textvariable = w)
d5['values'] = ["Intrest1","Intrest2","Intrest3","Intrest4","interst5"]
d5.grid(row = 5,column =1)
d5.current()
b3 = Button(text = "Submit")
b3.grid(row =7,column =2 )
root.mainloop()
