# RELATIONSHIPS:

'''In real life objects interact with other objects.
For example, a Customer object buys a mobile object.
Therefore, it must be true in OOP as well.
So far, we have been creating classes and objects which don’t interact with other objects.
Now we will take a look at how to create objects which have some relationship with other objects.'''

# Common types of OOP relationships

# INHERITANCE:
'''When an object is a type of another object
Ex: Mobile is a Product'''

# AGGREGATION:
'''When one object owns another object, but they both have INDEPENDENT life cycle.
Ex: Customer has an Address.
Even if the customer is no more, there may be other cutomers in that address.
So Address continues to exist even after a customer is no more.'''

# COMPOSITION:
'''When one object owns another object, but they both have SAME life cycle.
Ex: College has a Department
If colleges closes, the department is also closed.


Also, each object may relate with multiple objects at the same time.

For example, Shoe is also a Product.
A Customer may have many addresses.
A department may have many employees.
A child may have many siblings, etc.

In this section, we will be looking at Inheritance and Aggregation alone.'''


# AGGREGATION:
'''If class A owns class B, then class A is said to aggregate class B.

This is also commonly known as "has-A" relationship.

For example, in our online shopping application, a Customer has an Address.

First let us look at the Customer class and Address class independently.

Customer:
 - name
 - age
 - phone_no

 __init__(name,age,phone_no)
 + view_details()
 + update_details()

Address:
 - door_no
 - street
 - area
 - pincode

 __init__(door_no,street,area,pincode)
 + update_address()


Let us look at the code of both the classes:'''

class Customer:
    def __init__(self, name, age, phone_no):
        self.name = name
        self.age = age
        self.phone_no = phone_no

    def view_details(self):
        pass

    def update_details(self):
        pass

class Address:
    def __init__(self, door_no, street, area, pincode):
        self.door_no = door_no
        self.street = street
        self.area = area
        self.pincode = pincode

    def update_address(self):
        pass

'''If we want the Customer object to aggregate the Address object,
thereby owning the Address object and having full access to it,
then the Customer object must have an additional attribute for Address as shown below:'''

# Just like Customer "has-a" name, Customer "has-a" age, Customer "has-a" phone_no, now Customer also "has-a" Address

'''Note: In class diagram, aggregation is represented by a line connecting the classes
and a diamond symbol in the class which aggregates the other class.

In the above example, the Customer aggregates the Address and hence the diamond symbol is near the Customer class'''


'''Let us add the extra attribute in the Customer class so that it can aggregate the Address class as shown below:'''

class Customer:
    def __init__(self, name, age, phone_no, address):
        self.name = name
        self.age = age
        self.phone_no = phone_no
        self.address = address

    def view_details(self):
        # pass
        print(self.name, self.age, self.phone_no)
        print(self.address.door_no, self.address.street, self.address.area, self.address.pincode)

    def update_details(self,add):
        self.address = add

class Address:
    def __init__(self, door_no, street, area, pincode):
        self.door_no = door_no
        self.street = street
        self.area = area
        self.pincode = pincode

    def update_address(self):
        pass

print("Aggregation - 1")
add1 = Address(123,"5th lane","Hyd",56001)
add2 = Address(567,"6th lane","Sec",82006)
# cus1 = Customer("Jack",24,1234,None)
# cus2 = Customer("Jane",25,5678,None)
cus1 = Customer("Jack",24,1234,add1)
cus2 = Customer("Jane",25,5678,add2)

'''Since the Customer class has aggregated the Address class,
the address object is available in all the methods of the Customer class, just like regular attributes'''

cus1.view_details()
cus1.update_details(add2)
cus1.view_details()

# Aggregation and access specifiers
'''We have already seen that private variables cannot be accessed outside the class.
This is true even in aggregation.
The owning class cannot access the private attributes of the aggregated class directly.'''

class Customer:
    def __init__(self, name, age, phone_no, address):
        self.name = name
        self.age = age
        self.phone_no = phone_no
        self.address = address
        
    def view_details(self):
        print (self.name, self.age, self.phone_no)
        # print (self.address.__door_no, self.address.__street, self.address.__area, self.address.__pincode) # wrong
        
class Address:
    def __init__(self, door_no, street, area, pincode):
        self.__door_no = door_no
        self.__street = street
        self.__area = area
        self.__pincode = pincode

    def update_details(self):
        pass

print()
print("Aggregation - class with private variables")
add1 = Address(123,"5th Lane", "Kukatpally", 56001)
cus1 = Customer("Jack", 24, 1234, add1)
cus1.view_details()

'''Once we have appropriate accessor and mutator methods
we can start accessing the private variables of the aggregated class using those methods.'''

class Customer:
    def __init__(self, name, age, phone_no, address):
        self.name = name
        self.age = age
        self.phone_no = phone_no
        self.address = address

    def view_details(self):
        print(self.name, self.age, self.phone_no)
        print(self.address.get_door_no(), self.address.get_street(), self.address.get_area(), self.address.get_pincode())

class Address:
    def __init__(self, door_no, street, area, pincode):
        self.__door_no = door_no
        self.__street = street
        self.__area = area
        self.__pincode = pincode

    def get_door_no(self):
        return self.__door_no

    def get_street(self):
        return self.__street

    def get_area(self):
        return self.__area

    def get_pincode(self):
        return self.__pincode

    def set_door_no(self, value):
        self.__door_no = value

    def set_street(self, value):
        self.__street = value

    def set_area(self, value):
        self.__area = value

    def set_pincode(self, value):
        self.__pincode = value

    def update_address(self):
        pass
    
print()
print("Aggregation with private variables and access specifiers")
add1 = Address(123,"5th Lane", "Kukatpally", 56001)
cus1 = Customer("Jack", 24, 1234, add1)
cus1.view_details()
        
# WEAKER RELATIONSHIP:
'''Sometimes a class may depend on another class for some of its use.
This is not a strict relationship and hence won’t appear in the class diagram.
For example, in the below code, the Customer class depends on a payment object for purchasing.
Here payment is a local variable and not an attribute.'''

class Customer:
    def __init__(self, name, age, phone_no):
        self.name = name
        self.age = age
        self.phone_no = phone_no

    def purchase(self, payment):
        if payment.type == "card":
            print("Paying by card")
        elif payment.type == "e-wallet":
            print("Paying by wallet")
        else:
            print("Paying by cash")

class Payment:
    def __init__(self, type):
        self.type = type

print()
print("Weaker relationship")
payment1 = Payment("card")
c = Customer("Jack",23,1234)
c.purchase(payment1)

'''Apart from an object being passed as a parameter to the method,
we can also create an object locally inside a method.

This again is a weaker dependency which does not reflect in the class diagram.'''

# Object Creation:

class Customer:
    def __init__(self, name, cust_type, bill):
        self.name = name
        self.bill = bill
        self.cust_type = cust_type

    def calculate_bill(self):
        tax1 = Tax(self.cust_type)
        final_bill = self.bill * tax1.tax_details(self.cust_type)
        return final_bill

class Tax:
    def __init__(self, cust_type):
        self.cust_type = cust_type

    def tax_details(self, cust_type):
        if (cust_type == "Student"):
            return 5
        else:
            return 10

cus1 = Customer("Maddy", "Student", 100)
print(cus1.calculate_bill())


# Weaker relationship using static methods or attributes
'''Also, sometimes we may access the static attributes or methods of another class directly inside our class.
This again is a weaker relationship.'''

# Usage of Static attribute:
class CustomerCare:
    helpline = 111000
class Customer:
    def call_support(self):
        print("Calling",str(CustomerCare.helpline))
print()
print("Weaker relationship using Static attribute")
Customer().call_support()

# Usage of Static Method:
class CustomerCare:
    __helpline = 111000

    @staticmethod
    def get_helpline():
        return CustomerCare.__helpline

class Customer:
    def call_support(self):
        print("Calling",str(CustomerCare.get_helpline()))
    
print()
print("Weaker relationship using Static Method")
Customer().call_support()
        
# SUMMARY:
'''
- Classes can have relationships with other classes
- In aggregation one class owns another though they have their own life cycle.
- Aggregation is represented using a diamond sysmbol in the class diagram.
- if an object is used only in a method of a class as a local variable then it is called Association.
- As an Association is not a strict relationship, it can not be represnted in the class diagram
- We can also use staic variable or method of one class inside another class using Association.'''

# EXCERCISE-1:
'''1. Freight Pvt. Ltd, a cargo company, forwards cargos/freights between its customers.
Freight charges are applied based on weight and distance of the shipment.
Write a python program to implement the class diagram given below.'''

'''Method description:

- Initialize counter variable to 198 in Freight class

- All validate methods should return true, if validation succeeds. Else it should return false

- validate_customer_id(): Customer id should be 6 digits and should begin with digit 1

- validate_weight(): Weight should be a multiple of 5

- validate_distance(): Distance should be between 500kms and 5000kms (both inclusive)

- forward_cargo()

    - Validate from_customer.customer_id, recipient_customer.customer_id, distance and weight of the freight

    - If valid,

        - auto-generate freight_id starting from 200 and initialize it. freight_id should be even

        - calculate freight_charge based on weight (Rs.150/kg) and distance (Rs.60/km)

    - Else, set freight_charge to 0

'''

class Customer:
    def __init__(self, customer_id, customer_name, address):
        self.__customer_id = customer_id
        self.__customer_name = customer_name
        self.__address = address

    def validate_customer_id(self):
        if self.__customer_id >= 100000 and self.__customer_id <= 199999:
            return True
        else:
            return False

    def get_customer_id(self):
        return self.__customer_id

    def get_customer_name(self):
        return self.__customer_name

    def get_address(self):
        return self.__address


class Freight:
    counter = 198
    def __init__(self, recipient_customer, from_customer, weight, distance):
        self.__freight_id = None
        self.__recipient_customer = recipient_customer
        self.__from_customer = from_customer
        self.__weight = weight
        self.__distance = distance
        self.__freight_charge = None

    def validate_weight(self):
        if self.__weight%5 == 0:
            return True
        else:
            return False

    def validate_distance(self):
        if self.__distance >= 500 and self.__distance <= 5000:
            return True
        else:
            return False

    def forward_cargo(self):
        if self.__from_customer.validate_customer_id() and self.__recipient_customer.validate_customer_id() and self.validate_weight() and self.validate_distance():
            Freight.counter = Freight.counter + 2
            self.__freight_id = Freight.counter
            self.__freight_charge = 150 * self.__weight + 60 * self.__distance
            self.print_detals()
        else:
            self.__freight_charge = 0

    def get_freight_id(self):
        return self.__freight_id

    def get_freight_charge(self):
        return self.__freight_charge

    def get_recipient_customer(self):
        return self.__recipient_customer

    def get_from_customer(self):
        return self.__from_customer

    def get_weight(self):
        return self.__weight

    def get_distance(self):
        return self.__distance

    def print_detals(self):
        print("get_freight_id:", self.get_freight_id())
        print("get_freight_charge:", self.get_freight_charge())
        print("get_from_customer.get_customer_id:", self.get_from_customer().get_customer_id())
        print("get_from_customer.get_customer_name:", self.get_from_customer().get_customer_name())
        print("get_from_customer.get_address:", self.get_from_customer().get_address())
        print("get_recipient_customer.get_customer_id:", self.get_recipient_customer().get_customer_id())
        print("get_recipient_customer.get_customer_name:", self.get_recipient_customer().get_customer_name())
        print("get_recipient_customer.get_address:", self.get_recipient_customer().get_address())
        print("get_weight:", self.get_weight())
        print("get_distance:", self.get_distance())

print()
print("Excercise-1")
b1 = Customer(187586,"bhanu","SRD")
c1 = Customer(122112,"Chandu","GNP")
f1 = Freight(b1,c1,55,771)
f2 = Freight(c1,b1,70,2200)
f1.forward_cargo()
print()
f2.forward_cargo()

# EXCERCISE-2:
'''Coorg Fruit Farm is a retail chain which sells fruits grown in their orchards in Coorg, India.
They want to keep track of customers who buy fruits from them and also the billing process.

Write a python program to implement the class diagram given below.'''

class FruitInfo:
    __fruit_name_list = ["Apple","Guava","Orange","Grape","Sweet Lime"]
    __fruit_price_list = [200,80,70,110,60]

    @staticmethod
    def get_fruit_price(fruit_name):
        if fruit_name in FruitInfo.__fruit_name_list:
            return FruitInfo.get_fruit_price_list()[FruitInfo.get_fruit_name_list().index(fruit_name)]
        else:
            return -1

    @staticmethod
    def get_fruit_name_list():
        return FruitInfo.__fruit_name_list

    @staticmethod
    def get_fruit_price_list():
        return FruitInfo.__fruit_price_list

class Purchase:
    __counter = 101
    def __init__(self, customer, fruit_name, quantity):
        self.__purchase_id = None
        self.__customer = customer
        self.__fruit_name = fruit_name
        self.__quantity = quantity

    def get_purchase_id(self):
        return self.__purchase_id 

    def get_customer(self):
        return self.__customer

    def get_quantity(self):
        return self.__quantity

    def calculate_price(self):
        price_per_kg = FruitInfo.get_fruit_price(self.__fruit_name)
        if price_per_kg != -1:
            price = price_per_kg * self.__quantity
            if price_per_kg == max(FruitInfo.get_fruit_price_list()) and self.__quantity > 1:
                discount = 2
            elif price_per_kg == min(FruitInfo.get_fruit_price_list()) and self.__quantity >= 5:
                discount = 5
            else:
                discount = 0
            price = price - price * discount / 100
            
            if self.__customer.get_cust_type() == "wholesale":
                price = price - price * 10 / 100
                
            self.__purchase_id = "P" + str(Purchase.__counter)
            Purchase.__counter += 1
            return price
        else:
            return -1

class Customer:
    def __init__(self, customer_name, cust_type):
        self.__customer_name = customer_name
        self.__cust_type = cust_type

    def get_customer_name(self):
        return self.__customer_name
    
    def get_cust_type(self):
        return self.__cust_type
        

print()
print("Excercise-2")
c1 = Customer("Bhanu","wholesale")
c2 = Customer("Vishnu","retail")
p1 = Purchase(c1, "Apple", 10)
p2 = Purchase(c1, "Orange", 10)
p3 = Purchase(c1, "Sweet Lime", 10)
p4 = Purchase(c2, "Guava", 10)
p5 = Purchase(c2, "Grape", 10)
print(p1.calculate_price())
print(p2.calculate_price())
print(p3.calculate_price())
print(p4.calculate_price())
print(p5.calculate_price())

# EXCERCISE-3:
'''3. Care hospital management wants to calculate the charge of lab tests done by its patients.
Write a python program to implement the class diagram given below.'''
class LabTestRepository:
    __list_of_hospital_lab_test_ids = ["i1","i2","i3","i4","i5"]
    __list_of_lab_test_charge = [1500,250,1200,1450,670]

    @staticmethod
    def get_test_charge(lab_test_id):
        if lab_test_id in LabTestRepository.__list_of_hospital_lab_test_ids:
            index = LabTestRepository.__list_of_hospital_lab_test_ids.index(lab_test_id)
            return LabTestRepository.__list_of_lab_test_charge[index]
        else:
            return -1

class Patient:
    def __init__(self, patient_id, patient_name, list_of_lab_test_ids):
        self.__patient_id = patient_id
        self.__patient_name = patient_name
        self.__list_of_lab_test_ids = list_of_lab_test_ids
        self.__lab_test_charge = None

    def get_patient_id(self):
        return self.__patient_id

    def get_patient_name(self):
        return self.__patient_name

    def get_list_of_lab_test_ids(self):
        return self.__list_of_lab_test_ids

    def get_lab_test_charge(self):
        return self.__lab_test_charge

    def calculate_lab_test_charge(self):
        self.__lab_test_charge = 0
        for i in self.__list_of_lab_test_ids:
            charge = LabTestRepository.get_test_charge(i)
            if  charge != -1:
                self.__lab_test_charge += charge
            else:
                self.__lab_test_charge += 0
        return self.__lab_test_charge
    

print()
print("Excercise-3:")
p1 = Patient("101","Bhanu",["i2","i3","i1"])
print(p1.calculate_lab_test_charge())

# Quiz - Relationships in OOP


# Q1 of 3
'''What is the output of the following code snippet?'''

class Mobile:
    def __init__(self,brand,case):
        self.brand=brand
        self.case=case
    def display(self):
        print(self.case.color)

class Case:
    def __init__(self,color):
        self.color=color
c1=Case("Black")
c2=Case("White")
m1=Mobile("Hony",c1)
c1.color="Green"
m1.display()
 

'''
- Black
- White
- Green - CORRECT'''

# Q2 of 3

'''What is the output of the following code snippet?'''

class Customer:
    def __init__(self,name,mobile):
        self.name=name
        self.mobile=mobile
class Mobile:
    def __init__(self,brand):
        self.brand=brand
    def unlock(self,cover):
        print(cover.color)
class Cover:
    def __init__(self):
        self.__color="red"
# Customer("Cus1",Mobile("Apple")).mobile.unlock(Cover())
 
'''
Error - CORRECT
red
None'''

# Q3 of 3

'''What is the output of the following code snippet?'''

class Customer:
    def __init__(self,name,mobile):
        self.name=name
        self.mobile=mobile
class Mobile:
    def __init__(self,brand):
        self.brand=brand
    def unlock(self,cover):
        cover.color="yellow"
class Cover:
    def __init__(self):
        self.color="red"
Customer("Cus1",Mobile("Apple")).mobile.unlock(Cover())
print(Cover().color)
 
'''
- Error
- red - CORRECT
- yellow
'''
