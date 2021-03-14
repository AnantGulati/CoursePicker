import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from functools import partial
  
from course_picker import Backend

LARGEFONT =("Verdana", 35)
  
class tkinterApp(tk.Tk):
     
    # __init__ function for class tkinterApp 
    def __init__(self, *args, **kwargs): 
         
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
         
        # creating a container
        container = tk.Frame(self)  
        container.pack(side = "top", fill = "both", expand = True) 

        self.backend_obj = Backend()
        self.courses_interest_list = []
        self.update_interest_list()
  
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
  
        # initializing frames to an empty array
        self.frames = {}    
        # iterating through a tuple consisting
        # of the different page layouts
        for F in (StartPage, Page1, Page2, Page3, Page4,Page5,Page6):
  
            frame = F(container, self)
  
            # initializing frame of that object from
            # startpage, page1, page2 respectively with 
            # for loop
            self.frames[F] = frame 
  
            frame.grid(row = 0, column = 0, sticky ="nsew")
  
        self.show_frame(StartPage)
  
    # to display the current frame passed as parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
    
    def update_interest_list(self):
        self.courses_interest_list = self.backend_obj.get_interest_list()

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
        button2 = ttk.Button(self, text ="Admin",
        command = lambda : controller.show_frame(Page3))
     
        # putting the button in its place by
        # using grid
        button2.grid(row = 2, column = 1, padx = 10, pady = 10)

# second window frame page1 
class Page1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        e = ttk.Label(self,text = "Name :").grid(row = 1,column=10)
        s = ttk.Entry(self,width = 35)
        s.grid(row =1,column = 11,columnspan =3, padx = 10, pady =10)
        name  = s.get()
        f = ttk.Label(self,text = "SRN : ").grid(row = 2, column =10)
        t = ttk.Entry(self,width = 35)
        t.grid(row = 2, column =11,columnspan = 3, padx =10, pady =10)
        srn = t.get()
  
        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text ="Back",command = lambda : controller.show_frame(StartPage))
     
        # putting the button in its place by using grid
        button1.grid(row = 5, column = 1, padx = 10, pady = 10)
  
        # button to show frame 2 with text layout2
        button2 = ttk.Button(self, text ="Next",command = lambda : controller.show_frame(Page2))
     
        # putting the button in its place by 
        # using grid
        button2.grid(row = 5, column = 2, padx = 10, pady = 10)

# third window frame page2
class Page2(tk.Frame): 
    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent)
        l1 = ttk.Label(self,text = "Enter your interests one by one in an order of decreasing priority").grid(row = 0 , column =0)
        l1 = ttk.Label(self, text ="Interest 1:").grid (row = 1, column = 0)
        
        self.interest_entries = []
        
        self.interest_entries.append(ttk.Combobox(self, width = 27, textvariable = ""))
        self.interest_entries[-1]['values'] = self.controller.courses_interest_list
        self.interest_entries[-1].grid(row = 1,column =1)
        self.interest_entries[-1].current()

        l2 = ttk.Label(self, text ="Interest 2:").grid (row = 2, column = 0)
        self.interest_entries.append(ttk.Combobox(self, width=27, textvariable=""))
        self.interest_entries[-1]['values'] = self.controller.courses_interest_list
        self.interest_entries[-1].grid(row = 2,column =1)
        self.interest_entries[-1].current()

        l3 = ttk.Label(self, text ="Interest 3:").grid (row = 3, column = 0)
        self.interest_entries.append(ttk.Combobox(self, width = 27, textvariable = ""))
        self.interest_entries[-1]['values'] = self.controller.courses_interest_list
        self.interest_entries[-1].grid(row = 3,column =1)
        self.interest_entries[-1].current()
        
        button4 = ttk.Button(self, text ="See Courses",command = self.find_relevant_courses)
        button4.grid(row = 5, column = 1, padx = 10, pady = 10)
  
        button7 = ttk.Button(self, text ="Back",command = lambda : controller.show_frame(Page1))
        button7.grid(row = 5, column = 2, padx = 10, pady = 10)

        l4 = ttk.Label(self,text = "The three most relevant courses for your interests are as follows. Click to view description.").grid(row = 7,column = 1)
        self.relevant_course_buttons = []
        self.relevant_courses = []
        self.relevant_course_names = []
        for i in range(3):
            self.relevant_course_names.append(tk.StringVar())
            self.relevant_course_names[-1].set('')

        self.relevant_course_buttons.append(ttk.Button(self, textvariable = self.relevant_course_names[0], command = self.view_course(1)).grid(row = 10,column = 1))
        self.relevant_course_buttons.append(ttk.Button(self, textvariable = self.relevant_course_names[1], command = self.view_course(2)).grid(row = 11,column = 1))
        self.relevant_course_buttons.append(ttk.Button(self, textvariable=self.relevant_course_names[2], command=self.view_course(3)).grid(row=12, column=1))

    def find_relevant_courses(self):
        student_preference_list = []
        for interest_entry in self.interest_entries:
            student_preference_list.append(interest_entry.get())

        courses_collection = self.controller.backend_obj.pick_course(student_preference_list)
        self.relevant_courses = []
        self.course_match_score = []
        for course_obj, match in courses_collection:
            self.relevant_courses.append(course_obj)
            self.course_match_score.append(match)
        print(self.relevant_courses)

        idx = 0
        for course in self.relevant_courses:
            self.relevant_course_names[idx].set(course.course_id)
            idx += 1

    def view_course(self, course_num):
        def course_viewer_function():
            if len(self.relevant_courses) < course_num:
                return None
            else:
                messagebox.showinfo("", "Match Score: %d\nDescription: %s\nInterests: %s" % (\
                    self.course_match_score[course_num - 1], self.relevant_courses[course_num - 1].course_description, str(self.relevant_courses[course_num - 1].interest_list)))
        return course_viewer_function

class Page3(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Login", font = LARGEFONT)
        label.grid(row = 0, column = 4, padx = 10, pady = 10)
        Label1 = ttk.Label(self, text  = "Username")
        Label1.grid(row = 1, column = 3, padx = 10, pady = 10)
        Label2 = ttk.Label(self,text = 'Password')
        Label2.grid(row = 2, column = 3, padx =10, pady = 10)
        
        self.uname_entry = ttk.Entry(self, width =35)
        self.uname_entry.grid(row=1, column=4, padx=10, pady=10)
        self.pwd_entry = ttk.Entry(self, width = 35)
        self.pwd_entry.grid(row=2, column=4, padx=10, pady=10)
        
        button1 = ttk.Button(self, text ="Login ", command = self.verify_login)
        button1.grid(row = 3, column = 1, padx = 10, pady = 10)

        button2 = ttk.Button(self, text ="Back ", command = lambda: controller.show_frame(StartPage))
        button2.grid(row = 3, column = 2, padx = 10, pady = 10)
  
    def verify_login(self):
        uname = self.uname_entry.get()
        pwd = self.pwd_entry.get()
        valid = self.controller.backend_obj.check_creds(uname,pwd)
        if valid:
            self.controller.show_frame(Page4)
        else:
            messagebox.showerror("Invalid Login","Invalid Username(%s) or Password(%s)"%(uname,pwd))

class Page4(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="COURSE ADDER", font = LARGEFONT)
        label.grid(row = 0, column = 4, padx = 10, pady = 10)
        
  
        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text ="ADD", command = lambda : controller.show_frame(Page5))
     
        # putting the button in its place 
        # by using grid
        button1.grid(row = 1, column = 4, padx = 10, pady = 10)
  
        # button to show frame 2 with text
        # layout2
        button2 = ttk.Button(self, text ="REMOVE",command = lambda : controller.show_frame(Page6))

     
        # putting the button in its place by 
        # using grid
        button2.grid(row = 2, column = 4, padx = 10, pady = 10)
        button3 = ttk.Button(self, text = 'LOGOUT',command = lambda : controller.show_frame(Page3))
        button3.grid(row = 3, column = 4, padx = 10, pady =10)

class Page5(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Name", font = LARGEFONT)
        label.grid(row = 0, column = 3, padx = 10, pady = 10)
        self.course_name_entry = ttk.Entry(self, width = 45)
        self.course_name_entry.grid(row=0, column=4)

        label1 = ttk.Label(self,text = "Description")
        label1.grid(row = 1, column = 3,padx = 10, pady =10)
        self.course_desc_entry = ttk.Entry(self, width = 65)
        self.course_desc_entry.grid(row=1, column=4)
        
        self.interest_entries = []

        label2 = ttk.Label(self,text = "Interest1:")
        label2.grid(row = 2, column = 3)
        self.interest_entries.append(ttk.Entry(self, width = 65))
        self.interest_entries[-1].grid(row=2, column=4)
        
        label3 = ttk.Label(self,text = "Interest2:")
        label3.grid(row = 3, column = 3,padx = 10, pady =10)
        self.interest_entries.append(ttk.Entry(self, width=65))
        self.interest_entries[-1].grid(row=3, column=4)

        label4 = ttk.Label(self,text = "Interest3:")
        label4.grid(row = 4, column = 3,padx = 10, pady =10)
        self.interest_entries.append(ttk.Entry(self, width=65))
        self.interest_entries[-1].grid(row=4, column=4)
  
        # button to show frame 2 with text
        button1 = ttk.Button(self, text ="ADD", command = self.add_course)
        button1.grid(row = 5, column = 4, padx = 10, pady = 10)
        
        # button to show frame 2 with text
        # layout2
        button2 = ttk.Button(self, text ="BACK",command = lambda : controller.show_frame(Page4))
        button2.grid(row = 7, column = 4, padx = 10, pady = 10)
    
    def add_course(self):
        course_name = self.course_name_entry.get()
        course_desc = self.course_desc_entry.get()
        interest_list = []
        for interest_entry in self.interest_entries:
            interest_list.append(interest_entry.get().lower())

        success,error_message = self.controller.backend_obj.add_course(course_name,interest_list,course_desc)
        if success:
            self.controller.update_interest_list()
            messagebox.showinfo("Success","Course '%s' was added successfully"%(course_name))
            self.controller.show_frame(Page4)
        else:
            messagebox.showerror("Error","Unable to add course due to the following error: %s"%(error_message))


class Page6(tk.Frame):
     
    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="NAME" )
        label.grid(row = 0, column = 3, padx = 10, pady = 10)
        self.course_name_entry = ttk.Entry(self, width = 35)
        self.course_name_entry.grid(row=0, column=4)
  
        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text ="REMOVE", command = self.remove_course)
     
        # putting the button in its place 
        # by using grid
        button1.grid(row = 1, column = 4, padx = 10, pady = 10)
  
        # button to show frame 2 with text
        # layout2
        button2 = ttk.Button(self, text ="BACK",command = lambda : controller.show_frame(Page4))
        button2.grid(row = 2, column = 4, padx = 10, pady =10)

    def remove_course(self):
        course_name = self.course_name_entry.get()
        success, error_message = self.controller.backend_obj.remove_course(course_name)
        if success:
            messagebox.showinfo("Success","Course '%s' was removed successfully"%(course_name))
            self.controller.update_interest_list()
            self.controller.show_frame(Page4)
        else:
            messagebox.showerror("Error","Unable to remove course due to the following error: %s"%(error_message))


# Driver Code
app = tkinterApp()
app.mainloop()
