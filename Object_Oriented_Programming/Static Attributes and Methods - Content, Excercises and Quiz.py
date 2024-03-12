# STATIC ATTRIBUTES AND METHODS:

# Need for static:
'''Let us assume that in our online shopping app,
we want to provide a limited 50% flat off on all mobile phones

How can we write our code so that all mobile objects get a 50% off?
One solution is to create a discount attribute and hard code the value as 50% as shown below:'''

class Mobile:
    def __init__(self, price, brand):
        self.price = price
        self.brand = brand
        self.discount = 50

    def purchase(self):
        total = self.price - self.price * self.discount / 100
        print(self.brand, "mobile with price", self.price, "is available after discount at", total)

print("Need for static:")
mob1 = Mobile(20000,"Apple")
mob2 = Mobile(30000,"Apple")
mob3 = Mobile(5000,"Samsung")

mob1.purchase()
mob2.purchase()

'''However, the solution of hardcoding the value in the attribute is not a good one.

For example, since this is a limited time discount

we should be able to programmatically enable and disable the discount using functions like this:'''

class Mobile:
    def __init__(self, price, brand):
        self.price = price
        self.brand = brand
        self.discount = 0

    def purchase(self):
        total = self.price - self.price * self.discount / 100
        print(self.brand, "mobile with price", self.price, "is available after discount at", total)

def enable_discount(list_of_mobiles):
    for mobile in list_of_mobiles:
        mobile.discount=50

def disable_discount(list_of_mobiles):
    for mobile in list_of_mobiles:
        mobile.discount=0

print()
print("Need for static - 2:")
mob1=Mobile(20000, "Apple")
mob2=Mobile(30000, "Apple")
mob3=Mobile(5000, "Samsung")
mob4=Mobile(6000, "Samsung")

mobiles=[mob1,mob2,mob3,mob4]

mob1.purchase()
enable_discount(mobiles)
mob2.purchase()
mob3.purchase()
disable_discount(mobiles)
mob4.purchase()

'''However, in our current approach, each object has discount as an attribute.
If we change the value for one object, it does not affect the other object.
If we have to change, we have to change for all the objects, one by one.'''

'''What we need is a way to make an attribute shared across objects.
The data is shared by all objects, not owned by each object.
Thus, by making a single change, it should reflect in all objects at one go.'''

# Static variables :

'''We can create shared attributes by placing them directly inside the class and not inside the constructor.

And since this attribute is not owned by any one object, we don’t need the self to create this attribute.

Such variables which are created at a class level are called "static variables".

Here discount is a static variable.'''

class Mobile:
    discount = 50
    def __init__(self, price, brand):
        self.price = price
        self.brand = brand

# Accessing static variables
'''Now, we have created static variables, we can access them using the Class name itself.

Static variable belong to the class and not an object.

Hence we don’t need self to access static variables.'''

class Mobile:
    discount = 50
    def __init__(self, price, brand):
        self.price = price
        self.brand = brand

    def purchase(self):
        total = self.price - self.price * Mobile.discount / 100
        print (self.brand, "mobile with price", self.price, "is available after discount at", total)

print()
print("Accessing static variables:")
mob1=Mobile(20000, "Apple")
mob2=Mobile(30000, "Apple")
mob3=Mobile(5000, "Samsung")
mob1.purchase()
mob2.purchase()
mob3.purchase()

# Updating static values

class Mobile:
    discount = 50
    def __init__(self, price, brand):
        self.price = price
        self.brand = brand
    def purchase(self):
        total = self.price - self.price * Mobile.discount / 100
        print (self.brand, "mobile with price", self.price, "is available after discount at", total)

def enable_discount():
    Mobile.discount = 50

def disable_discount():
    Mobile.discount = 0

print()
print("Updating static values:")
mob1=Mobile(20000, "Apple")
mob2=Mobile(30000, "Apple")
mob3=Mobile(5000, "Samsung")

enable_discount()
mob1.purchase()
mob2.purchase()

disable_discount()
mob3.purchase()

'''Note: Static variables belong to the class
and hence it is incorrect to access them or update them using the reference variable or self.
Doing so may cause unexpected consequences in the code and should be refrained from.'''

# Static variables and encapsulation
'''We can make our static variable as a private variable by adding a double underscore in front of it.
We can also create getter and setter methods to access or modify it.'''

class Mobile:
    __discount = 50

    def get_discount(self):
        return Mobile.__discount

    def set_discount(self, discount):
        Mobile.__discount = discount

print()
print("Static variables and encapsulation")
m1 = Mobile()
print(m1.get_discount())

# Static method :
'''In the below code we are invoking the getter method using a reference variable.
But the self is not used inside the method at all.'''

class Mobile:
    __discount = 50
    def __init__(self, price, brand):
        self.price = price
        self.brand = brand
    def purchase(self):
        total = self.price - self.price * Mobile.__discount / 100
        print ("Total is ",total)
    def get_discount(self):
        return Mobile.__discount
    def set_discount(self,discount):
        Mobile.__discount = discount

mob1=Mobile(20000, "Apple")
mob2=Mobile(30000, "Apple")
mob3=Mobile(5000, "Samsung")
print()
print("Static method - Need")
print(mob1.get_discount())

'''Since static variable is object independent,
we need a way to access the getter setter methods without an object.

This is possible by creating static methods.
Static methods are those methods which can be accessed without an object.

They are accessed using the class name.

There are two rules in creating such static methods:
 - The methods should not have self
 - @staticmethod must be written on top of it'''

class Mobile:
    __discount = 50
    def __init__(self, price, brand):
        self.price = price
        self.brand = brand
    def purchase(self):
        total = self.price - self.price * Mobile.__discount / 100
        print ("Total is ",total)

    @staticmethod
    def get_discount():
        return Mobile.__discount
    
    @staticmethod
    def set_discount(discount):
        Mobile.__discount = discount

'''We can access static methods directly using the class name, even without creating objects.'''
print()
print("Static Method:")
print(Mobile.get_discount())

# Complete solution

class Mobile:
    __discount = 50
    def __init__(self, price, brand):
        self.price = price
        self.brand = brand
    def purchase(self):
        total = self.price - self.price * Mobile.__discount / 100
        print (self.brand, "mobile with price", self.price, "is available after discount at", total)

    @staticmethod
    def enable_discount():
        Mobile.set_discount(50)

    @staticmethod
    def disable_discount():
        Mobile.set_discount(0)

    @staticmethod
    def get_discount():
        return Mobile.__discount
    
    @staticmethod
    def set_discount(discount):
        Mobile.__discount = discount

print()
print('Static Method - Complete solution:')
mob1=Mobile(20000, "Apple")
mob2=Mobile(30000, "Apple")
mob3=Mobile(5000, "Samsung")

Mobile.disable_discount()
mob1.purchase()

Mobile.enable_discount()
mob2.purchase()

Mobile.disable_discount()
mob3.purchase()

# SUMMARY:
'''
 - Static attributes are created at class level.
 - Static attributes are accepted using ClassName.
 - Static attributes are object independent,
   We can access them without creating instances(object) of the class in which they are defined.
 - The value stored in static attribute is shared between
   all instances(objects) of the class in which the static attribute is defined.'''

# EXCERCISE - 1:
'''
1. Write a python program to find out if a given classroom is present in the left wing of a university building.
   Implement the class, Classroom given below.



Method/Attribute description:

- classroom_list: Static list which store the name of the class rooms in the left wing

- search_classroom(class_room): Static method which search for the given class room in the classroom_list.
  If found, return "Found". Else, return -1

Note: Perform case insensitive string comparison'''

class Classroom:
    classroom_list = ['A01','B02','C01','D01']
    @staticmethod
    def search_classroom(class_room):
        if class_room.upper() in Classroom.classroom_list:
            return print("Found")
        else:
            return print(-1)
print()
print("Excercise-1:")
Classroom.search_classroom('D01')


# EXCERCISE - 2:
'''2. Write a Python program to generate tickets for online bus booking, based on the class diagram given below.'''

class Ticket:
    counter = 0
    def __init__(self, passenger_name, source, destination):
        # Ticket.counter = Ticket.counter + 1
        # self.__ticket_id = Ticket.counter
        self.__passenger_name = passenger_name
        self.__source = source
        self.__destination = destination

    def validate_source_destination(self):
        if ( self.__source.upper() == 'DELHI' ) and ( self.__destination.upper() in ['MUMBAI','CHENNAI','PUNE','KOLKATA'] ):
            return True
        else:
            return False            

    def generate_ticket(self):
        if self.validate_source_destination():
            Ticket.counter = Ticket.counter + 1
            if Ticket.counter < 10:
                self.__ticket_id = self.__source.upper()[0] + self.__destination.upper()[0] + str(0) + str(Ticket.counter)
            else:
                self.__ticket_id = self.__source.upper()[0] + self.__destination.upper()[0] + str(Ticket.counter)
        else:
            self.__ticket_id = None
        
    def get_ticket_id(self):
        return self.__ticket_id

    def get_passenger_name(self):
        return self.__passenger_name

    def get_source(self):
        return self.__source

    def get_destination(self):
        return self.__destination
print()
print("Excercise-2:")
t1 = Ticket("Bhanu","Delhi","Mumbai")
t2 = Ticket("Maheshwari","Delhi","Mumbai")
t3 = Ticket("Bhanu","Delhi","Chennai")
t4 = Ticket("Maheshwari","Delhi","Chennai")
t5 = Ticket("Bhanu","Delhi","Pune")
t6 = Ticket("Bhanu","Delhi","Kolkata")
t7 = Ticket("Maheshwari","Delhi","Pune")
t8 = Ticket("Maheshwari","Delhi","Kolkata")
t9 = Ticket("Bhanu","Delhi","Kolkata")
t10 = Ticket("Maheshwari","Delhi","Kolkata")
t11 = Ticket("Bhanu","Delhi","Chennai")
t12 = Ticket("Maheshwari","Delhi","Chennai")
t13 = Ticket("Bhanu","Delhi","Mumbai")
t14 = Ticket("Maheshwari","Delhi","Mumbai")
t15 = Ticket("Bhanu","Delhi","Pune")
t16 = Ticket("Maheshwari","Delhi","Pune")

t1.generate_ticket()
t2.generate_ticket()
t3.generate_ticket()
t4.generate_ticket()
t5.generate_ticket()
t6.generate_ticket()
t7.generate_ticket()
t8.generate_ticket()
t9.generate_ticket()
t10.generate_ticket()
t11.generate_ticket()
t12.generate_ticket()
t13.generate_ticket()
t14.generate_ticket()
t15.generate_ticket()
t16.generate_ticket()

print(t1.get_ticket_id())
print(t2.get_ticket_id())
print(t3.get_ticket_id())
print(t4.get_ticket_id())
print(t5.get_ticket_id())
print(t6.get_ticket_id())
print(t7.get_ticket_id())
print(t8.get_ticket_id())
print(t9.get_ticket_id())
print(t10.get_ticket_id())
print(t11.get_ticket_id())
print(t12.get_ticket_id())
print(t13.get_ticket_id())
print(t14.get_ticket_id())
print(t15.get_ticket_id())
print(t16.get_ticket_id())


# Q1 of 3
'''What is the output of the following code snippet?'''
class Table:
    def __init__(self):
        self.no_of_legs=4
        self.__glass_top=None
        self.__wooden_top=None

    def assign_data(self,glass_top,wooden_top):
        self.__glass_top=glass_top
        self.__wooden_top=wooden_top

    def identify_rate(self,glass_top,wooden_top):
        self.assign_data(glass_top, wooden_top)
        if(self.__glass_top==True):
            rate=20000
        elif(self.__wooden_top==True):
            rate=30000
        else:
            rate=0
        return rate
dining_table=Table()
rate=dining_table.identify_rate(True, False)
print(rate)
 
'''
- 30000
- 0
- 20000 
- Error'''

# Option 20000 is correct

# Q2 of 3

'''What will be the output of the following snippet?'''

class Example:
    num=10
    @staticmethod
    def add(num1,num2):
        result=(num1+num2)*Example.num
        return result
print(Example.add(100, 200))
 
'''
- Error: num being static cannot be accessed in add() method
- Error: add() method cannot be invoked using Example
- 3000 
- Error: Example.num is not initialized'''

# Option 3000 is correct


# Q3 of 3

'''Choose the statements which are INCORRECT with regard to the below code.'''

class Lion:
    __water_source="well in the circus"

    def __init__(self,name, gender):
        self.__name=name
        self.__gender=gender

    def drink_water(self):
        print(self.__name,"drinks water from the",Lion.__water_source)

simba=Lion("Simba","Male")
nala=Lion("Nala","Female")
simba.drink_water()
nala.drink_water()
 
'''
There will be only one __water_source variable created for both simba and nala objects
There will be two separate __water_source variables created for both simba and nala objects 
drink_water() cannot access __water_source variable 
__water_source should be always accessed using self in a method of the same class 
__water_source can be accessed using Lion in a method of the same class
'''

# Option There will be two separate __water_source variables created for both simba and nala objects is correct

# Option drink_water() cannot access __water_source variable is correct

# Option __water_source should be always accessed using self in a method of the same class is correct
