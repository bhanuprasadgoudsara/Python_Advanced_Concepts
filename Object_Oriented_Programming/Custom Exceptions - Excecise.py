# EXCERCISE:

class InvalidMechanicException(Exception):
    pass
class InvalidMechanicSpecializationException(Exception):
    pass

class Mechanic:
    def __init__(self, mechanic_id, specialization, vehicle_count):
        self.__mechanic_id = mechanic_id
        self.__specialization = specialization
        self.__vehicle_count = vehicle_count

    def get_mechanic_id(self):
        return self.__mechanic_id

    def get_specialization(self):
        return self.__specialization

    def get_vehicle_count(self):
        return self.__vehicle_count

    def set_mechanic_id(self, mechanic_id):
        self.__mechanic_id = mechanic_id

    def set_specialization(self, specialization):
        self.__specialization = specialization

    def set_vehicle_count(self, vehicle_count):
        self.__vehicle_count = vehicle_count

class VehicleService:
    def __init__(self, mechanic_list):
        self.__mechanic_list = mechanic_list

    def assign_vehicle_for_service(self, mechanic_id, vehicle_type):
        for i in self.__mechanic_list:
            if i.get_mechanic_id() == mechanic_id:
                if i.get_specialization() == vehicle_type:
                    i.set_vehicle_count(i.get_vehicle_count() + 1)
                    break
                else:
                    raise InvalidMechanicSpecializationException("Invalid Mechanic Specialization")
            elif self.__mechanic_list.index(i) == len(self.__mechanic_list)-1:
                raise InvalidMechanicException("Invalid Mechanic")
            else:
                continue
                
    def print_mechanic_list(self):
        count = 1
        for i in self.__mechanic_list:
            print("["+ i.get_mechanic_id()+", "+i.get_specialization()+", "+ str(i.get_vehicle_count())+"]")
            count += 1
            
            
m1 = Mechanic('M01','TW',1)
m2 = Mechanic('M02','FW',0)
m3 = Mechanic('M03','TW',4)
m4 = Mechanic('M04','FW',2)
m5 = Mechanic('M05','FW',1)

vs1 = VehicleService([m1,m2,m3,m4,m5])

try:
    # vs1.assign_vehicle_for_service('M03','TW')
    # vs1.assign_vehicle_for_service('M06','FW')
    vs1.assign_vehicle_for_service('M03','FW')

    vs1.print_mechanic_list()
except InvalidMechanicException:
    print("Invalid Mechanic Selected, Please Re-Enter")
except InvalidMechanicSpecializationException:
    print("Invalid Mechanic Specialization Selected, Please Re-Enter")
except Exception as e:
    print("Exception, Something went wrong !!")


# QUIZ:


# Q1 of 3

'''What is the output of the below program?'''

class InvalidAccountException(Exception):
    pass
class Account:
    account_list=[1001,1002,1003,1004]
    def validate_account(self,account_id):
        status=0
        for acct_id in self.account_list:
            if(account_id==acct_id):
                status=1
                break
        if(status!=0):
            return True
        else:
            raise InvalidAccountException
try:
    account1=Account()
    account1.validate_account(1006)
    print("Valid account number")
except InvalidAccountException:
    print("Invalid account number")
 
'''
- Valid account number
- Invalid account number - CORRECT
- Error: Element not found in list
'''

# Q2 of 3

'''What will be the output of the code given below?'''

class NameLengthException(Exception):
    pass
class EmployeeIdException(Exception):
    pass
class Employee:
    __trials=0
    def __init__(self,emp_id,emp_name):
        self.__emp_name=emp_name
        self.__emp_id=emp_id
    def validate_name(self):
        try:
            if(len(self.__emp_name) < 4):
                Employee.__trials=Employee.__trials+1
                raise NameLengthException
            if( not(self.__emp_id.startswith('E'))):
                raise EmployeeIdException
        except NameLengthException:
            Employee.__trials=Employee.__trials+1
            print(Employee.__trials)
        except EmployeeIdException:
            Employee.__trials=Employee.__trials+1
            print(Employee.__trials)
emp1=Employee('E1001','Tom')
emp1.validate_name()
emp2=Employee('1001','Tomy')
emp2.validate_name()
 
'''
- 2 3 - CORRECT
- 2 1
- 3 2
'''


# Q3 of 3

'''What will be the output of the code given below?'''

class InvalidEmployeeException(Exception):
    pass
class Project:
    def __init__(self,employee_list):
        self.__employee_list=employee_list

    def validate_employee(self,employee_id):
        flag=False
        for key in self.__employee_list:
            if(key==employee_id):
                flag=True
        if(flag==False):
            raise InvalidEmployeeException
            print("1")
        return True

project1=Project([1001,1002,1003])
try:
    print(project1.validate_employee(1005))
except Exception:
    print("2")
except InvalidEmployeeException:
    print("3")
 
'''
- 2 - CORRECT
- 3
- Error: Except should be the last block
'''
