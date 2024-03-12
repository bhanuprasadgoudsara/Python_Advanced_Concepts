# Special Methods in Python's OOP:

'''What happens when you try to place an object in print statement?'''

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

p1 = Product("Iphone",1000)
print('printing an Object - error')
print(p1)

'''The details of the object will be printed because,
no functionality is defined for printing an object.

The functionality can be defined using a special method called as __str__ method.

This method should always return a string.'''

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return self.name + ' ' + str(self.price)

p1 = Product("Iphone",1000)
print()
print('printing an Object - Correct method')
print(p1)

'''In python, we can use a + operator between two or more integers (or) between two or more strings.

what happens, if we use a + operator between two objects of a User Defined Class?

Let's see,'''

class Product:
    counter = 100
    def __init__(self, name, description, brand, price):
        self.id = 'P' + str(Product.counter + 1)
        self.name = name
        self.description = description
        self.brand = brand
        self.price = price

    def purchase(self):
        total_amount = self.price
        total_amount += 0.05 * total_amount
        print('Product ID:',self.id)
        print('Product Name:',self.name)
        print('Price:',self.price)
        print('Tax Amount:',total_amount - self.price)
        print('Grand Total:',total_amount)
        print('Thanks for the purchase.\n')

product1 = Product('Iphone','A mobile device with 4GB memory and 64GB Storage space which supprots 4G Network','Apple',72500.25)
product2 = Product('Air Max','A Sport Shoe','Nike',1280.0)
# product1 + product2

'''Traceback (most recent call last):
  File "C:/Users/sara.goud/Desktop/Coding_Skills/Infosys_Lex/Advanced Python Concepts/Object Oriented Programming/Special Methods in Python's OOP - Content, Excecise and Quiz.py", line 58, in <module>
    product1 + product2
TypeError: unsupported operand type(s) for +: 'Product' and 'Product' '''

# The interpreter will throw an error if you try to use an operator between objects of a User Defined Class. But, why?

'''This is because, we did not define any logic for the + operator in our user defined class Product.

We have some special function like __add__(), __sub()__, __mul__() to define the functionality of operators.

Some of these special functions are listed in the file below:'''

# In the following example, We are going to define logic for + operator for the class Product.

class Product:
    counter = 100
    def __init__(self, name, description, brand, price):
        self.id = 'P' + str(Product.counter + 1)
        self.name = name
        self.description = description
        self.brand = brand
        self.price = price

    def __add__(self, other):
        return self.price + other.price
product1 = Product('Iphone','A mobile device with 4GB memory and 64GB Storage space which supprots 4G Network','Apple',72500.25)
product2 = Product('Air Max','A Sport Shoe','Nike',1280.0)
print()
print('__add__')
print(product1 + product2)

'''In the above example, __add__(self,other) to define the functionality of + operator.

The first argument self takes the reference of first operand and other takes the reference of second argument.'''

# Summary:
'''In this section, we have seen how to define the functionality of operators with objects as operands using special methods.'''

# Quiz - Special Methods :

# Q1 of 2

'''What is the output of the following code?'''

class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def __add__(self,other):
        if self.price>other.price:
            return self.price
        return other.price

p1=Product('Iphone',1000)
p2=Product('Samsung',500)
print(p1+p2)
 
'''
- 1000 
- Error
- 500
'''
# Option 1000 is correct

# Q2 of 2

'''What is the output of the following code?'''

class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def __add__(self,other):
        if self.price>other.price:
            return self.price
        return other.price

p1=Product('Iphone',1000)
p2=Product('Samsung',500)
# print(p1+1000)
 
'''
- 1000
- Error 
- 500
'''
# AttributeError: 'int' object has no attribute 'price'
# Option Error is correct'''     
