import pickle

class Course:
    def __init__(self, course_id, interest_list = [], course_description = ''):
        self.course_id=course_id
        self.interest_list=interest_list
        self.course_description=course_description

        # assert list(filter(lambda x: x != '',self.interest_list)) == [], "Cannot have empty objects in course interest list"

    def __eq__(self,course_obj):
        return self.course_id == course_obj.course_id
    
    def compare_list(self,student_preference_list):
        #function to compare given preference list with course preference list
        match_count = 0
        for pref in student_preference_list:
            if pref in self.interest_list:
                match_count += 1
        return match_count

class Backend:
    def __init__(self,data_file_name = 'data'):
        #function to initialise the backend object 
        self.data_file_name = data_file_name
        self.admin_user_name = 'admin'
        self.admin_password = 'password'

        try:
            f = open(self.data_file_name,'rb')
            course_list = pickle.load(f)
            f.close()
            for course in course_list:
                print("%s. Interests: %s"%(course.course_id,course.interest_list))
        except FileNotFoundError:
            print("Data file does not exist. Creating a blank file")
            with open(self.data_file_name,'wb') as f:
                pickle.dump([],f)
        finally:
            print("Backend initialization complete")

    def add_course(self,course_id,interest_list,course_description):
        #function to add a new course to the binary final that stores all courses
        success, error_message = True, ""

        course_id = course_id.lower()

        final_interest_list = []        
        for i in interest_list:
            if i != '':
                final_interest_list.append(i)

        if final_interest_list == []:
            return False, "Empty interest list"

        new_course = Course(course_id,final_interest_list,course_description)
        
        course_list = None
        with open(self.data_file_name,'rb') as file_obj:
            course_list =pickle.load(file_obj)

        flag = True
        for existing_course in course_list:
            if existing_course == new_course:
                flag = False
                success = False
                error_message = "Course '%s' already exists"%(existing_course.course_id)
                break

        if flag == True:
            course_list.append(new_course)
            with open(self.data_file_name,'wb') as file_obj:
                pickle.dump(course_list,file_obj)

        return (success,error_message)
             
    def remove_course(self,course_id):
        #function to remove a new course to the binary final that stores all courses
        success, error_message = True, ""

        course_id = course_id.lower()

        course_to_remove = Course(course_id)

        course_list = None
        with open(self.data_file_name, 'rb') as file_obj:
            course_list = pickle.load(file_obj)
            
        try:
            course_list.remove(course_to_remove)
        except ValueError:
            success = False
            error_message = "Course '%s' does not exist"%(course_to_remove.course_id)

        with open(self.data_file_name, 'wb') as file_obj:
            pickle.dump(course_list, file_obj)

        return (success, error_message)

    def check_creds(self,username,password):
        #function to check the credentials while logging in to the admin account
        if username==self.admin_user_name and password==self.admin_password:
            return True
        else:
            return False

    def pick_course(self,student_preference_list):
        #function to return top three courses based on student preference list
        course_list = []
        with open(self.data_file_name,'rb') as file_obj:
            course_list = pickle.load(file_obj)

        max_courses_to_pick = 3
        if max_courses_to_pick > len(course_list):
            max_courses_to_pick = len(course_list)

        sorted_course_list = sorted(course_list, key= lambda x: x.compare_list(student_preference_list), reverse=True)

        picked_courses = []
        for i in range(max_courses_to_pick):
            picked_courses.append((sorted_course_list[i],sorted_course_list[i].compare_list(student_preference_list)))

        return picked_courses

    def get_interest_list(self):
        course_list = []
        with open(self.data_file_name, 'rb') as file_obj:
            course_list = pickle.load(file_obj)
        
        unique_interests = set()
        for course in course_list:
            for interest in course.interest_list:
                unique_interests.add(interest.lower())
        
        return list(unique_interests)

