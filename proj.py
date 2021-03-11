import tkinter as tk
from tkinter import ttk
  
 
LARGEFONT =("Verdana", 35)
  
class tkinterApp(tk.Tk):
     
    # __init__ function for class tkinterApp 
    def __init__(self, *args, **kwargs): 
         
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
         
        # creating a container
        container = tk.Frame(self)  
        container.pack(side = "top", fill = "both", expand = True) 
  
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
  
        # initializing frames to an empty array
        self.frames = {}    
        # iterating through a tuple consisting
        # of the different page layouts
        for F in (StartPage, Page1, Page2, Page3, Page4):
  
            frame = F(container, self)
  
            # initializing frame of that object from
            # startpage, page1, page2 respectively with 
            # for loop
            self.frames[F] = frame 
  
            frame.grid(row = 0, column = 0, sticky ="nsew")
  
        self.show_frame(StartPage)
  
    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
  
# first window frame startpage
  
class StartPage(tk.Frame):
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent)
         
        # label of frame Layout 2
        label = ttk.Label(self, text ="Course Picker", font = LARGEFONT)
         
        # putting the grid in its place by using
        # grid
        label.grid(row = 0, column = 4, padx = 10, pady = 10) 
  
        button1 = ttk.Button(self, text ="Student",
        command = lambda : controller.show_frame(Page1))
     
        # putting the button in its place by
        # using grid
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)
  
        ## button to show frame 2 with text layout2
        button2 = ttk.Button(self, text ="Teacher",
        command = lambda : controller.show_frame(Page2))
     
        # putting the button in its place by
        # using grid
        button2.grid(row = 2, column = 1, padx = 10, pady = 10)
  
          
  
  
# second window frame page1 
class Page1(tk.Frame):
     
    def __init__(self, parent, controller):
         
        tk.Frame.__init__(self, parent)
        e = ttk.Label(self,text = "Name :").grid(row = 10,column=10)
        s = ttk.Entry(self,width = 35)
        s.grid(row =10,column = 11,columnspan =3, padx = 10, pady =10)
        name  = s.get()
        f = ttk.Label(self,text = "SRN : ").grid(row = 11, column =10)
        t = ttk.Entry(self,width = 35)
        t.grid(row = 11, column =11,columnspan = 3, padx =10, pady =10)
        srn = t.get()
  
        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text ="Back",
                            command = lambda : controller.show_frame(StartPage))
     
        # putting the button in its place 
        # by using grid
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)
  
        # button to show frame 2 with text
        # layout2
        button2 = ttk.Button(self, text ="Next",
                            command = lambda : controller.show_frame(Page2))
     
        # putting the button in its place by 
        # using grid
        button2.grid(row = 2, column = 1, padx = 10, pady = 10)
  
  
  
  
# third window frame page2
class Page2(tk.Frame): 
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        l1 = ttk.Label(self,text = "Enter your intrests one  by one in an order of decreasing priority in them").grid(row = 0 , column =0)
        l1 = ttk.Label(self, text ="Interst 1:").grid (row = 1, column = 0)
        n=""
        d1 = ttk.Combobox(self, width = 27, textvariable = n)
        d1['values'] = ["Intrest1","Intrest2","Intrest3","Intrest4","interst5"]
        d1.grid(row = 1,column =1)
        d1.current()
        l2 = ttk.Label(self, text ="Interst 2:").grid (row = 2, column = 0)
        m=""
        d2 = ttk.Combobox(self, width = 27, textvariable = m)
        d2['values'] = ["Intrest1","Intrest2","Intrest3","Intrest4","interst5"]
        d2.grid(row = 2,column =1)
        d2.current()
        l3 = ttk.Label(self, text ="Interst 3:").grid (row = 3, column = 0)
        q=""
        d3 = ttk.Combobox(self, width = 27, textvariable = q)
        d3['values'] = ["Intrest1","Intrest2","Intrest3","Intrest4","interst5"]
        d3.grid(row = 3,column =1)
        d3.current()
        t1 = d1.get()
        t2 = d2.get()
        t3  = d3.get()
        # button to show frame 2 with text
        # layout2
        button4 = ttk.Button(self, text ="Next",
                            command = lambda : controller.show_frame(Page3))
     
        # putting the button in its place by 
        # using grid
        button4.grid(row = 8, column = 1, padx = 10, pady = 10)
  
        # button to show frame 3 with text
        # layout3
        button7 = ttk.Button(self, text ="Back",
                            command = lambda : controller.show_frame(Page1))
     
        # putting the button in its place by
        # using grid
        button7.grid(row = 9, column = 1, padx = 10, pady = 10)
class Page3(tk.Frame): 
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        label5 = ttk.Label(self, text ="Intersts Chosen", font = LARGEFONT)
        label5.grid(row = 0, column = 4, padx = 10, pady = 10)
        Label1 = ttk.Label(self, text = "")
        Label1.grid(row = 1, column =4 ,padx=10,pady =10)
        Label2 = ttk.Label(self, text = "")
        Label2.grid(row = 2, column =4 ,padx=10,pady =10)
        Label3 = ttk.Label(self, text = "")
        Label3.grid(row = 3, column =4 ,padx=10,pady =10)
  
        # button to show frame 3 with text
        # layout3
        button6 = ttk.Button(self, text ="Submit", command = lambda : controller.show_frame(Page4))
     
        # putting the button in its place by 
        # using grid
        button6.grid(row = 4, column = 4, padx = 10, pady = 10)
class Page4(tk.Frame):
        def __init__(self,parent,controller):
            tk.Frame.__init__(self, parent)
            label = ttk.Label(self, text = "The courses you can CHOOSE", font = LARGEFONT)
            label.grid(row = 5,column = 4 , padx = 10, pady =10)
            Label5 = ttk.Label(self,text = "")
            button5 = ttk.Button(self, text = "Back", command = lambda : controller.show_frame(Page3))
            button6 = ttk.Button(self,text = "Submit",)
  
        # button to show frame 3 with text
        # layout3
# Driver Code
app = tkinterApp()
app.mainloop()