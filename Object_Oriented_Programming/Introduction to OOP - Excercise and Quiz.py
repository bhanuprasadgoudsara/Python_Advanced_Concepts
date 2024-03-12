# Exercise -1
'''
WeCare insurance company wants to calculate premium of vehicles.

Vehicles are of two types – "Two Wheeler" and "Four Wheeler".
Each vehicle is identified by vehicle id, type, cost and premium amount.
Premium amount is 2% of the vehicle cost for two wheeler and 6% of the vehicle cost for four wheeler.
Calculate the premium amount and display the vehicle details.

Write a Python program to implement the class chosen with its attributes and methods.

Note:

1. Display appropriate error message, if the vehicle type is invalid

2. Perform case sensitive string comparison'''

class Vehicle:
    vehicle_id = 1000
    
    def __init__(self,vtype,vcost):
        Vehicle.vehicle_id += 1
        self.vehicle_id = Vehicle.vehicle_id
        self.vehicle_type = vtype
        self.vehicle_cost = vcost

    def __str__(self):
        return "Vehicle id: " + str(self.vehicle_id) + "\nVehicle type: " + self.vehicle_type + "\nVehicle cost: " + str(self.vehicle_cost)

    def calculate_premium(self):
        if self.vehicle_type == "Two Wheeler":
            print("Premium: " + str(self.vehicle_cost * 2 /100))
        elif self.vehicle_type == "Four Wheeler":
            print("Premium: " + str(self.vehicle_cost * 6 /100))
        else:
            print("Vehicle type is invalid")
            
v1 = Vehicle("Two Wheeler",98000)
v2 = Vehicle("Four Wheeler",1300000)
v3 = Vehicle("Three Wheeler",500000)
print(v1)
v1.calculate_premium()
print(v2)
v2.calculate_premium()
print(v3)
v3.calculate_premium()


# Exercise -2
'''
Consider the below scenario of a retail store.


 

Implement the Customer class based on the identified class structure and details given below:

    1. Consider all instance variables and methods to be public
    2. Assume that bill_amount is initialized with total bill amount of the customer
    3. Customer is eligible for 5% discount on the bill amount
    4. purchases(): Compute discounted bill amount and pay bill
    5. pays_bill(amount): Display, <customer_name> pays bill amount of Rs. <amount>

Represent few customers, invoke purchases() method and display the details.
'''

class Customer:
    def __init__(self,name,bill):
        self.customer_name = name
        self.bill_amount = bill

    def purchases(self):
        discount = 5
        self.bill_amount = self.bill_amount - self.bill_amount * discount / 100
        self.pays_bill(self.bill_amount)

    def pays_bill(self,amount):
        # print("Customer name:",self.customer_name,"\nBill amount: Rs.",amount)
        print(self.customer_name + " pays Rs." + str(amount))       

class Employee:
    def __init(self,name,role):
        self.emp_name = name
        self.designation = role
        
class Item:
    item_id = 1000
    def __init__(self, price, desc):
        Item.item_id = Item.item_id + 1
        self.item_id = Item.item_id
        self.price_per_unit = price
        self.desciption = desc

c1 = Customer("Bhanu",1200)
c1.purchases()


# Quiz - Introduction to OOP

# Q1 of 4

'''Choose the statements which are CORRECT with respect to the below code:'''

class Employee:
    def __init__(self):
        self.employee_id = None
    def check_eligibility(self):
        if(self.employee_id>=9000 and self.employee_id<=10000):
            print("The employee is eligible for special benefits")
        else:
            print("The employee is not eligible for special benefits")
emp1=Employee()
emp1.employee_id=10000
emp1.check_eligibility()
emp2=Employee()
emp2.employee_id=4500
emp2.check_eligibility()
 
'''
- There will be only one employee_id variable created for both the objects - emp1 and emp2
- There will be two employee_id variables created - one for emp1 and one for emp2 
- When check_eligibility() is invoked on emp1, self refers to emp1 
- When emp2.check_eligibility() is invoked, self.employee_id will have value None
- When emp2.check_eligibility() is invoked, line 8 will get executed 
'''

#Option There will be two employee_id variables created - one for emp1 and one for emp2 is correct

#Option When check_eligibility() is invoked on emp1, self refers to emp1 is correct

#Option When emp2.check_eligibility() is invoked, line 8 will get executed is correct



#Q2 of 4

'''What is the output of the below code snippet?'''

class Example:
    def __init__(self,num):
        self.num=num

    def set_num(self,num):
        self.num=num

    def get_num(self):
        return self.num
obj=Example(10)
print(obj.get_num())
obj.set_num(15)
print(obj.get_num())
 
'''
- 10 10
- 10 15 
- Error: constructor cannot accept a value
'''
# Option 10 15 is correct


# Q3 of 4

'''What is the output of the following code snippet?'''

class Example:
    def __init__(self,num):
        self.num=num

    def set_num(self,num):
        num=num

    def get_num(self):
        return self.num
obj=Example(10)
print(obj.get_num())
obj.set_num(15)
print(obj.get_num())
 
'''
- 10 10 
- 10 15
- Error: setters can assign value only to instance variables
'''
# Option 10 10 is correct



# Q4 of 4

'''What is the output of the following code snippet?'''

class Customer:
    def __init__(self):
        cust_id = 100

c1=Customer()
print(c1.cust_id)
 
'''
- 100
- Error 
- None
'''
# Option Error is correct
