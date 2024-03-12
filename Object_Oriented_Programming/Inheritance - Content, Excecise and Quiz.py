# Need for inheritance
'''
Let us say that the online shopping application wants to sell different types of phones:
- Feature phones and
- Smartphones

The below are the class diagrams for both the classes:

We can see that both the class have a lot in common.
This is because they both are ultimately phones and each is just a special type of phone.

Since both the classes are of type phone,
we can create a phone class with the common attributes, methods
and make these two classes inherit those attributes and behavior, as shown:

When a class inherits from another class, then those classes are said to have an "inheritance relationship".

The class which is inheriting is called the "child/sub/derived class"
and the class which is getting inherited is called the "parent/super/base class".

Inheritance is also called as "is-A" relationship.

In our example, FeaturePhone  and SmartPhone are inheriting the Phone class
(SmartPhone "is-A" phone, FeaturePhone "is-A" phone).
So Phone is the parent class and
FeaturePhone and SmartPhone are derived classes.

Note: The above class diagram illustrates the inheritance relationship'''


# There are three main advantages of inheritance:
'''
- We can keep common properties in a single place,
  thus any changes needs to be made need not be repeated

- Inheritance encourages code reuse thus saving us time

- If we want to add a new type of phone later on,
  we can simply inherit the Phone class instead of writing it from scratch'''

# Inheritance
'''Let us look at inheritance in code.
For now we will create the Phone class with necessary attributes and methods.
We will create FeaturePhone and SmartPhone classes without any attributes or methods now.
We will create them later.'''

class Phone:
    def __init__(self, price, brand, camera):
        self.price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a Phone")

    def return_phone(self):
        print("Returning a Phone")


class FeaturePhone:
    pass

class SmartPhone:
    pass

Phone(10000,"Apple","13px").buy()

'''To create an inheritance relationship between the classes,
mention the name of the parent class in brackets as shown:'''

class FeaturePhone(Phone):
    pass

class SmartPhone(Phone):
    pass

FeaturePhone(10000,"Apple","13px").buy()

# What gets inherited?
'''
When we have an inheritance relationship, the attributes and behaviors get inherited,

just like a child inherits certain attributes and behaviours from its parent.

From a code perspective, a child class inherits:
- Constructor
- Non-Private Attributes
- Non-Private Methods

This is true for languages like Java, C# etc.

Unlike other languages, private variables get inherited in Python. We will discuss more about this later.

When we say a child class inherits the attributes and methods,
we can treat the attributes and behavior as if it is owned by the child class itself.

Nowadays in real life a child has access to everything the parent has,
but the parents don’t have any access to things owned by the child.

Same thing holds true in OOP as well.

A child class can access everything a parent has,
but a parent class cannot access anything from the child class.

Since the SmartPhone class is inheriting the Phone class,
the SmartPhone class inherits the constructor of the Phone class.'''
  
class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a Phone")

    def return_phone(self):
        print("Returning a Phone")


class FeaturePhone(Phone):
    pass

class SmartPhone(Phone):
    pass

s = SmartPhone(20000,"Apple",13)
s.buy()

'''In real life, even though the child has access to everything the parent has,
the parents may not want their child to know about their difficulties.
They may choose to keep their difficulties private so that the child knows only good things.
Similarly, a child class cannot directly access the private attributes of the parent class.'''
class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a Phone")

    def return_phone(self):
        print("Returning a Phone")


class FeaturePhone(Phone):
    pass

class SmartPhone(Phone):
    def check(self):
        # print(self.__price)
        # print(self._Phone__price)
        pass

print()
print("Accessing private attributes of parent class-1")
s = SmartPhone(20000,"Apple",13)
s.check()

# Accessing private attributes of parent class
'''In order to access the private attributes of the parent class, 
getter and setter method should be defined in the parent class as below'''

class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a Phone")

    def return_phone(self):
        print("Returning a Phone")

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

class FeaturePhone(Phone):
    pass

class SmartPhone(Phone):
    def check(self):
        # print(self.__price)
        # print(self._Phone__price)
        print(self.get_price())
print()
print("Accessing private attributes of parent class-2")
s = SmartPhone(20000,"Apple",13)
s.check()

'''Apart from attributes, the child class inherits the methods of the parent class as shown:'''

print()
print("Accessing non-private methods of parent class-3")
s.buy()

'''Sometimes a child may not want to use what it has inherited from the parent.

The same holds true for OOP as well.

If the child class does not want to use a method inherited from the parent class
then it may create its own method with the same name.

When the child has a method with the same name as that of the parent,
it is said to override the parent’s method.

This is called as "Method Overriding".

Method overriding is also called as "Polymorphism".'''

class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a Phone")

    def return_phone(self):
        print("Returning a Phone")

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

class FeaturePhone(Phone):
    pass

class SmartPhone(Phone):
    def buy(self):
        print("Buying a SmartPhone")
        
    def check(self):
        # print(self.__price)
        # print(self._Phone__price)
        print(self.get_price())

print()
print("Polymorphism")
s = SmartPhone(20000,"Apple",13)
s.buy()

# Method overriding:
'''Even though the child class may override the methods of the parent class,
it might still decide to use the parent class overridden method.
To invoke anything belonging to the parent class,
the child class needs to use the super() function, as shown below:'''

class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a Phone")

    def return_phone(self):
        print("Returning a Phone")

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

class FeaturePhone(Phone):
    pass

class SmartPhone(Phone):
    def buy(self):
        print("Buying a SmartPhone")
        super().buy()
        
    def check(self):
        # print(self.__price)
        # print(self._Phone__price)
        print(self.get_price())

print()
print("Method Overriding - super()")
s = SmartPhone(20000,"Apple",13)
s.buy()

# Constructor overriding:

class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a Phone")

    def return_phone(self):
        print("Returning a Phone")

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

class FeaturePhone(Phone):
    pass

class SmartPhone(Phone):
    def __init__(self, os, ram):
        self.os = os
        self.ram = ram
        print("Inside SmarPhone consructor")
        
    def buy(self):
        print("Buying a SmartPhone")
        super().buy()
        
    def check(self):
        # print(self.__price)
        # print(self._Phone__price)
        print(self.get_price())

print()
print("Method Overriding - super()")
s = SmartPhone("Android",2)
print(s.os)
# print(s.brand) gives error

# Using super to access parent class constructor:
'''To access the parent class constructor we can use super().

Thus, the data is passed to the child class constructor,

from there the data is sent to the parent class constructor and

thus the attributes of the parent class get inherited.


super() function can be used to access the constructor or methods of the parent class,
but not the attributes.

Also super() function can be used only inside a class and not outside the class.'''

class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a Phone")

    def return_phone(self):
        print("Returning a Phone")

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

class FeaturePhone(Phone):
    pass

class SmartPhone(Phone):
    def __init__(self, price, brand, camera, os, ram):
        super().__init__(price, brand, camera)
        self.os = os
        self.ram = ram
        print("Inside SmarPhone consructor")
        
    def buy(self):
        print("Buying a SmartPhone")
        super().buy()
        
    def check(self):
        # print(self.__price)
        # print(self._Phone__price)
        print(self.get_price())

print()
print("Method Overriding - super()")
s = SmartPhone(20000,"Samsung", 12, "Android", 2)
print(s.os)
print(s.brand)

# Types of inheritance:
'''
Inheritance can come in many forms as below:

1. Single Level ==> ( Single Parent - Single Child )
2. Multi Level ==> ( Grand Parent - Parent - Child - Grand Child )
3. Hierachical ==> ( One Parent - Many Children )
4. Multiple ==> ( One Child - Many Parents )'''

# Simple inheritance:
'''Simple inheritance enables a derived class to inherit properties and behavior from a single parent class.
It allows a derived class to inherit the properties and behavior of a base class,
thus enabling code reusability as well as adding new features to the existing code'''
class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera
    def buy(self):
        print ("Buying a phone")
    def return_phone(self):
        print ("Returning a phone")
class SmartPhone(Phone):
    pass

print()
print("Simple inheritance")
SmartPhone(1000,"Apple","13px").buy()

# Multi level inheritance:

class Product:
    def review(self):
        print("Product Customer Review")

class Phone(Product):
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera
    def buy(self):
        print ("Buying a phone")
    def return_phone(self):
        print ("Returning a phone")
        
class SmartPhone(Phone):
    pass

print()
print("Multi level inheritance")
s = SmartPhone(1000,"Apple","13px")
s.buy()
s.review()

# Hierarchical inheritance:
'''Inheritance is the process of inheriting properties of objects of one class by objects of another class.

When more than one classes are derived from a single base class,
such inheritance is known as Hierarchical Inheritance,

where features that are common in lower level are included in parent class.'''

class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera
    def buy(self):
        print ("Buying a phone")
    def return_phone(self):
        print ("Returning a phone")
        
class FeaturePhone(Phone):
    pass

class SmartPhone(Phone):
    pass

print()
print("Hierarchical inheritance")
s = SmartPhone(1000,"Apple","13px")
s.buy()

# Multiple inheritance:
'''When an object or class can inherit characteristics and features from more than one parent object or parent class,
such type of inheritance is called as multiple inheritance.'''

class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera
    def buy(self):
        print ("Buying a phone")
    def return_phone(self):
        print ("Returning a phone")
        
class Product:
    def review(self):
        print("customer review")

class SmartPhone(Phone, Product):
    pass

print()
print("Multiple inheritance")
s = SmartPhone(1000,"Apple","13px")
s.buy()
s.review()

'''Note: When a child is inheriting from multiple parents,
and if there is a common behavior to be inherited,
it inherits the method in Parent class which is first in the list. In our example,
the buy() of Phone is inherited as it appears first in the list'''

# SUMMARY:
'''
- A class can inherit from another class
- Inheritance improves code reuse
- Constructor, attributes, methods get inherited to the child class
- The parent has no access to the child class
- Private properties of parent are not accessible directly in child class
- Child class can override the methods, this is called method overriding
- super() is an inbuilt function which is used to invoke the parent class methods and constructor
- Types of Inheritance - Simple, Multilevel, Hierarchical and Multiple inheritance'''

# EXCERCISE-1:
'''1. An apparel shop wants to manage the items which it sells.
Write a python program to implement the class diagram given below.'''

class Apparel:
    counter = 100
    def __init__(self, price, item_type):
        self.__price = price
        self.__item_type = item_type
        Apparel.counter += 1
        if self.__item_type == "Cotton":
            self.__item_id = "C" + str(Apparel.counter)
        elif self.__item_type == "Silk":
            self.__item_id = "S" + str(Apparel.counter)

    def get_item_id(self):
        return self.__item_id

    def get_price(self):
        return self.__price

    def get_item_type(self):
        return self.__item_type

    def set_price(self, price):
        self.__price = price

    def calculate_price(self):
        self.__price = self.__price + self.__price * 5 / 100

class Cotton(Apparel):
    def __init__(self, price, discount):
        super().__init__(price, "Cotton")
        self.__discount = discount

    def calculate_price(self):
        super().calculate_price()
        self.set_price( self.get_price() - self.get_price() * self.__discount / 100 )
        super().calculate_price()

    def get_discount(self):
        return self.__discount

class Silk(Apparel):
    def __init__(self, price):
        super().__init__(price, "Silk")
        self.__points = None

    def calculate_price(self):
        super().calculate_price()
        if self.get_price() > 10000:
            self.__points = 10
        else:
            self.__points = 3
        self.set_price( self.get_price() - self.get_price() * 10 / 100 )

    def get_points(self):
        return self.__points

print()
print("Excericise-1")
s = Silk(11500)
s.calculate_price()
print(s.get_points())
print(s.get_price())
c = Cotton(1250, 7)
c.calculate_price()
print(c.get_discount())
print(c.get_price())

# EXCERCISE-2:
'''2. Spice Hut is a tiffin service provider which home delivers dinner to their customers
– Occasional customers and Regular customers.
Write a Python program to implement class diagram given below.'''

class Customer:
    def __init__(self, customer_name):
        self.__customer_name = customer_name
        self.bill_amount = None
        self.bill_id = None

    def calculate_bill_amount(self):
        self.bill_amount = -1
        return self.bill_amount

    def get_customer_name(self):
        return self.__customer_name

class OccasionalCustomer(Customer):
    counter = 1000
    def __init__(self, customer_name, distance_in_kms):
        super().__init__(customer_name)
        self.__distance_in_kms = distance_in_kms
        OccasionalCustomer.counter += 1
        self.bill_id = "O" + str(OccasionalCustomer.counter)

    def validate_distance_in_kms(self):
        if self.__distance_in_kms >= 1 and self.__distance_in_kms <= 5:
            return True
        else:
            return False

    def calculate_bill_amount(self):
        if self.validate_distance_in_kms():
            if self.__distance_in_kms >= 1 and self.__distance_in_kms <= 2:
                self.bill_amount = 50 + (5 * self.__distance_in_kms)
            elif self.__distance_in_kms > 2 and self.__distance_in_kms <= 5:
                self.bill_amount = 50 + (7.5 * self.__distance_in_kms)
            return self.bill_amount
        else:
            super().calculate_bill_amount()

    def get_distance_in_kms(self):
        return self.__distance_in_kms

class RegularCustomer(Customer):
    counter = 1000
    def __init__(self, customer_name, no_of_tiffin):
        super().Customer(customer_name)
        self.__no_of_tiffin = no_of_tiffin
        OccasionalCustomer.counter += 1
        self.bill_id = "R" + RegularCustomer.counter
        
    def calculate_bill_amount(self):
        if self.validate_no_of_tiffin():
            self.bill_amount = self.__no_of_tiffin * 50
        else:
            super().calculate_bill_amount()

    def validate_no_of_tiffin(self):
        pass

    def get_no_of_tiffin(self):
        return self.__no_of_tiffin

print()
print("Excercise-2")
c1 = OccasionalCustomer("Bhanu",4)
print(c1.get_distance_in_kms())
print(c1.calculate_bill_amount())

# QUIZ - INHERITANCE:

# Q1 of 3

'''What is the output of the following code snippet?'''

class Parent:
    def __init__(self,num):
      self.__num=num
    def get_num(self):
      return self.__num
class Child(Parent):
    def __init__(self,num,val):
      super().__init__(num)
      self.__val=val
    def get_val(self):
      return self.__val
son=Child(100,200)
print(son.get_num())
print(son.get_val())
 

'''
- 100 200 - CORRECT
- 200 100
- None 200
- Error'''


# Q2 of 3

'''What is the output of the following code snippet?'''

class Parent:
    def __init__(self):
        self.num=100

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.var=200
    def show(self):
        print(self.num)
        print(self.var)

son=Child()
son.show()
 

'''
- None 200
- 100 200 - CORRECT
- Error'''


# Q3 of 3

'''Consider the following python function for representing the customers of a retail store.
Objective of the code is to record the details of the customers.'''

def customer_record(customer_type, name, discount, points_earned, membership_card_type):
    if(customer_type=="Regular"):
        record="Record Regular Customer:"+name+" "+(str)(discount)
    elif(customer_type=="Privileged"):
        record="Record Privileged Customer:"+name+" "+(str)(points_earned)
    elif(customer_type=="Elite"):
        record="Record Elite Customer:"+name+" "+membership_card_type
    print(record)

'''What will be the optimal class structure if this has to be re-written in Object oriented programming?'''


'''
- 3 independent classes: Regular, Privileged, Elite
- 1 class: Customer
- 4 classes with inheritance: Base class: Customer; Child classes: Regular, Privileged; Grand Child of Privileged: Elite
- 4 classes with inheritance: Base class: Customer; Child classes: Regular, Privileged, Elite - CORRECT
- 4 classes with inheritance: Base class: Customer; Child classes: Regular, Privileged; Grand Child of Regular: Elite'''
