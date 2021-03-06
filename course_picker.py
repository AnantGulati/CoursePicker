class user:
    def __init__(self,name,pwd,id):
        self.name=name
        self.pwd=pwd
        self.id=id
class student(user):
    def __init__(self,pref):
        self.pref=pref
    def add_pref():
        pass
    def remove_pref():
        pass
    def select_pref():
        pass
    def view_pref():
        pass
class admin(user):
    def add_course(course):
        pass
    def remove_course(course_id):
        pass

class course:
    def __init__(self,course_id,interest_list):
        self.course_id=course_id
        self.interest_list=interest_list
    def get_score():
        pass