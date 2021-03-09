'''
class User:
    def __init__(self,name,pwd,id):
        self.name=name
        self.pwd=pwd
        self.id=id

class Student(User):
    def __init__(self,pref):
        self.pref=pref
        assert type(self.pref) == type([]), "Unexpected type " + str(type(self.pref)) + " for pref"
    def add_pref(self):
        self.pref=input("enter your prefferences in order")
    def remove_pref(self):
        pass
    def select_pref(self):
        pass
    def view_pref(self):
        pass

class Admin(User):
    def __init__(self):
        self.user_id="admin"
        self.password="password"
        self.course_data_filename = "course_data.txt"
        self.course_file_object=open("course_data.txt","ab")
    def add_course(self,course):
        course.course_id=input("enter course id")
        course.course_description=input("enter course description")
        course.course_interes=input("enter course interests in order")
        #add_to_pickle()
        pickle.dump(course,self.course_file_object)
    def remove_course(self,course_id):
        with open("course_data.txt","wb") as self.course_file_object:
            pass
            
'''
import pickle

class Course:
    def __init__(self,course_id,interest_list,course_description):
        self.course_id=course_id
        self.interest_list=interest_list
        self.course_description=course_description
    def compare_list(self,preferences):
        #function to compare given preference list with course preference list
        pass 


class Backend:
    def __init__(self,file_object_name):
        #function to initialise filename 
        self.file_object_name="data"
    def add_course(self,course_id,interest_list,course_description):
        #function to add a new course to the binary final that stores all courses
        #data=open("data.txt","x")
        with open("data.txt",'a+') as data:
            new_course = Course(course_id,interest_list,course_description)
            pickle.dump(new_course,data)
    def remove_course(self,course_id):
        #function to remove a new course to the binary final that stores all courses
        #pref_list=list(unpickle_database("data.txt"))
        for i in pref_list:
            if i.course_id == self.course_id:
                pref_list.remove(i)

    def check_creds(self,username,password):
        #function to check the credentials while logging in to the admin account
        if username=="admin" and password=="password":
            return True
    def pick_course(self,):
        #function to pick courses based on preference list
        pass
