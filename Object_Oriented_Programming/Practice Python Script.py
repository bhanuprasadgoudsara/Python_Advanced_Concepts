class Student:
    def __init__(self):
        self.__student_id = None
        self.__marks = None
        self.__age = None
        self.__course_id = None
        self.__fees = None

    def validate_marks(self):
        if self.__marks >= 0 and self.__marks <= 100 :
            return True
        else:
            return False

    def validate_age(self):
        if self.__age > 20:
            return True
        else:
            return False

    def set_student_id(self, sid):
        self.__student_id = sid

    def set_marks(self, marks):
        self.__marks = marks

    def set_age(self, age):
        self.__age = age

    def get_student_id(self):
        return self.__student_id

    def get_marks(self):
        return self.__marks

    def get_age(self):
        return self.__age

    def get_course_id(self):
        return self.__course_id

    def get_fees(self):
        return self.__fees

    def check_qualification(self):
        if self.validate_marks() and self.validate_age():
            if self.__marks >= 65:
                return True
            else:
                return False
        else:
            return False

    def choose_course(self, course_id):
        courses = {'1001':25575,'1002':15500}
        #for i in courses.keys():
        #    print(i)
        if str(course_id) in courses.keys():
            self.__course_id = course_id
            self.__fees = courses[str(course_id)]
            if int(self.get_marks()) > 85:
                self.__fees = self.get_fees() - self.get_fees() * 25 / 100
            return True
        else:
            return False                  

    def __str__(self):
        student_details = "Student ID: " + str(self.get_student_id()) + "\nMarks: " + str(self.get_marks()) + "\nAge: " + str(self.get_age())
        course_details = "\nCourse ID: " + str(self.get_course_id()) + "\nfees: " + str(self.get_fees())
        return student_details + course_details
    

print("Excercise - 3:")
bhanu = Student()
bhanu.set_student_id(304)
bhanu.set_marks(87)
bhanu.set_age(24)
bhanu.choose_course(1001)
if bhanu.check_qualification():
    print("Student will get Admission")
    print(bhanu)
else:
    print("No Admission")
