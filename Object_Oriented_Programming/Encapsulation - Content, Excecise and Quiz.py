# ENCAPSULATION:
'''What is the use of a lock?

Just the way a lock prevents others from accessing your property,
we can restrict other parts of the code from directly accessing sensitive data.

Consider the below code where the customer has a wallet_balance and there are methods
which allow us to access and update that balance based on some logic.'''

class Customer:
    def __init__(self, cust_id, name, age, wallet_balance):
        self.cust_id = cust_id
        self.name = name
        self.age = age
        self.wallet_balance = wallet_balance

    def update_balance(self, amount):
        if amount < 1000 and amount > 0:
            self.wallet_balance += amount

    def show_balance(self):
        print("The balance is", self.wallet_balance)

c1 = Customer(100, "Gopal", 24, 1000)
c1.update_balance(500)
c1.show_balance()

'''But with the way currently it is coded,
the data can be accidentally changed by directly assigning a incorrect value to it as shown below:'''

c1.wallet_balance = 10000000000
c1.show_balance()

'''We can put a lock on that data by adding a double underscore in front of it, as shown below:'''

class Customer:
    def __init__(self, cust_id, name, age, wallet_balance):
        self.cust_id = cust_id
        self.name = name
        self.age = age
        self.__wallet_balance = wallet_balance

    def update_balance(self, amount):
        if amount < 1000 and amount > 0:
            self.__wallet_balance += amount

    def show_balance(self):
        print("The balance is", self.__wallet_balance)

c1 = Customer(100, "Gopal", 24, 1000)
# print(c1.__wallet_balance)
# AttributeError: 'Customer' object has no attribute '__wallet_balance'
c1.update_balance(500)
c1.show_balance()

''''Adding a double underscore makes the attribute a private attribute.
Private attributes are those which are accessible only inside the class.
This method of restricting access to our data is called "Encapsulation".'''

# Common mistake with encapsulation
'''If we try to assign a value to a private variable,
we end up creating a new attribute in python.
Thus this code does not give an error,
but it is logically flawed and does not produce the intended result.'''

c1.__wallet_balance = 10000000000
c1.show_balance()
print(c1.__wallet_balance)

# Accessing private variables
'''Since we know that the name of the variable changes when we make it private,
we can access it using its modified name as shown below:'''

c1._Customer__wallet_balance = 50000
c1.show_balance()

'''So, if private variable can be accessed outside the class and can be modified,
then what is the advantage of making it private?'''

# Note: Languages like Java, C#, etc do not allow access of private variable outside the class
'''What is the use of a lock, if a thief can open it?

Any lock can be broken by a determined thief.
Similarly, just because you make your code private,
does not mean it is not accessible to other developers.
When a developer sees a private variable,
it’s a gentleman's agreement not to access it directly.
It is used to only prevent accidental access.

Thus in python encapsulation is more like a caution sign than a lock.
A caution sign is there so that you don’t accidentally break a rule.
But if you still want to break it you can, with consequence ;)'''

# Getter and Setter methods

'''To have a error free way of accessing and updating private variables, we create specific methods for this.

Those methods which are meant to set a value to a private variable are called "setter/mutator methods"

and methods meant to access private variable values are called "getter/accessor methods".

The below code is an example of getter and setter methods:'''

class Customer:
    def __init__(self, id, name, age, wallet_balance):
        self.id = id
        self.name = name
        self.age = age
        self.__wallet_balance = wallet_balance

    def set_wallet_balance(self, amount):
        if amount < 1000 and amount > 0 :
            self.__wallet_balance = amount

    def get_wallet_balance(self):
        return self.__wallet_balance

print()
c1 = Customer(100, "Gopal", 24, 1000)
print(c1.id)
c1.set_wallet_balance(900)
print(c1.get_wallet_balance())

'''All setter methods must accept the value to be updated as a parameter
and all getter methods must not have any parameter and they must return the value.'''

# Summary
'''
- Encapsulation is preventing access to a data outside the class

- Adding a __ in front of a attribute makes it private

- Getter and Setter methods should be used to access a private attribute'''

# Excercise - 1 :
'''In the Athlete class given below,
     a. make all the attributes private and
     b. add the necessary accessor and mutator methods

Represent Maria, the runner and make her run.'''

class Athlete:
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender
    def running(self):
        if(self.gender=="girl"):
            print("150mtr running")
        else:
            print("200mtr running")

# class with private variables

class Athlete:
    def __init__(self,name,gender):
        self.__name = name
        self.__gender = gender
    def running(self):
        if(self.__gender=="girl"):
            print("150mtr running")
        else:
            print("200mtr running")
    def set_name(self,name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_gender(self,gender):
        self.__gender = gender

    def get_gender(self):
        return self.__gender

print("Excercise - 1:")
maria = Athlete("Maria","girl")
maria.running()

# Excercise - 2 :
'''A university wants to automate their admission process.
Students are admitted based on marks scored in a qualifying exam.
A student is identified by student id, age and marks in qualifying exam.

Data are valid, if:
  a. Age is greater than 20
  b. Marks is between 0 and 100 (both inclusive)

A student qualifies for admission, if
  a. Age and marks are valid and
  b. Marks is 65 or more

Write a python program to represent the students seeking admission in the university.

Business rules'''

class Student:
    def __init__(self):
        self.__student_id = None
        self.__marks = None
        self.__age = None

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

    def check_qualification(self):
        if self.validate_marks() and self.validate_age():
            if self.__marks >= 65:
                return True
            else:
                return False
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

    def __str__(self):
        return "Student ID: " + str(self.get_student_id()) + "\nMarks: " + str(self.get_marks()) + "\nAge: " + str(self.get_age())

print("Excercise - 2:")
bhanu = Student()
bhanu.set_student_id(304)
bhanu.set_marks(85)
bhanu.set_age(24)
print(bhanu)
if bhanu.check_qualification():
    print("Student will get Admission")
else:
    print("No Admission")
    

# Excercise - 3 :
'''Continuing with the previous scenario,
a student eligible for admission has to choose a course
and pay the fees for it.

If they have scored more than 85 marks in qualifying exam,
they get 25% discount on fees.

Valid course ids and fees are given below:


Extend the program written in the previous assignment to include the above requirement.

Business rules
'''
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


# Quiz - Encapsulation:

# Q1 of 3

'''What should be written in line 12 to get the output as 6?'''

class Example:
    def __init__(self):
        self.__num=5

    def set_num(self,num):
        self.__num=num

    def get_num(self):
        return self.__num
obj=Example()
obj.set_num(6)
#line 12
 

'''
- print(obj.__num)
- print(obj.get_num()) 
- print(obj.num)
- print(num)
'''
print(obj.get_num())

# Q2 of 3

'''What should be written in line 9 to get the output in line 13 as 5?'''

'''
class Example:
    def __init__(self):
        self.__num=None

    def set_num(self,num):
        self.__num=num

    def change_num(self):
        #line 9
        return self.__num
obj=Example()
obj.set_num(10)
print(obj.change_num())
''' 

'''
- self.__num=5 
- __num=5
- self.num=5
'''
class Example:
    def __init__(self):
        self.__num=None

    def set_num(self,num):
        self.__num=num

    def change_num(self):
        self.__num=5
        return self.__num
obj=Example()
obj.set_num(10)
print(obj.change_num())


# Q3 of 3

'''Jennifer is a python developer who has written the below code:'''

class Dam:
    def __init__(self,name, length):
        self.name=name
        self.__length=length
    def get_length(self):
        return self.__length

dam1=Dam("ABC dam",3.5 )
# print("Dam name:",dam1.__name)
# print("Dam Length", dam1.__length)
'''
She desires the output to be:
Dam name: ABC dam
Dam length: 3.5
but, she is unable to proceed due to an error. Which of the following steps should she follow to get the desired output?
YOU MUST CHOOSE TWO OPTIONS.
'''
'''
- Change Line 9 to: print("Dam name:",dam1.name) - CORRECT
- Change Line 9 to: print("Dam name:",dam1.get_name())
- Change Line 10 to : print("Dam length:", dam1.length)
- Change Line 10 to : print("Dam length:", dam1.get_length())  - CORRECT'''

print("Dam name:",dam1.name)
print("Dam length:", dam1.get_length())

