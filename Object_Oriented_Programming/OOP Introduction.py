# INTRODUCTION:
'''
Now, you are going to learn how to build complex real world applications using a technique known as "object oriented programming".
We will be using an online shopping scenario to understand OOP concepts.

Consider the below code which allows you to purchase different products. All products have discount of 10%.'''

def purchase_product(product_type, price):
    discount = 10
    total_price = price - price * discount / 100
    print("Total price of " + product_type + " is " + str(total_price) )

purchase_product("Mobile",20000)
purchase_product("Shoe",200)

'''Run the code  in the playground and observe the output'''
# Total price of Mobile is 18000.0
# Total price of Shoe is 180.0


'''Let us say that we want to update our code such that:

If the mobile brand is Apple then the discount is 10% else the discount is 5%

All shoes have 2% tax and no discount


We can accomplish this by adding additional parameters to our function and updating our logic as shown below'''

def purchase_product(product_type, price, mobile_brand = None):
    if product_type == "Mobile" :
        if mobile_brand == "Apple" :
            discount = 10
        else:
            discount = 5
        total_price = price - price * discount / 100
    else:
        total_price = price + price * 2 / 100
    print("Total price of " + product_type + " is " + str(total_price) )

purchase_product("Mobile",20000, "Apple")
purchase_product("Shoe",200)

# Total price of Mobile is 18000.0
# Total price of Shoe is 204.0

# INCREASING PROBLEMS :
'''
The solution we came up with has a key problem.

Data for mobiles and shoes are mixed up in the same code.

If we have to make changes to the logic for purchasing shoes,
we have to modify method that has logic for both shoes and mobiles.

For example, if we have to add 'material' to the shoe and have a 5% tax on 'leather' shoes,
then we have to go through code related to mobile as well, as shown below:'''

def purchase_product(product_type, price, mobile_brand, material):
    if product_type == "Mobile" :
        if mobile_brand == "Apple" :
            discount = 10
        else:
            discount = 5
        total_price = price - price * discount / 100
    else:
        if material == "leather" :
            tax = 5
        else:
            tax = 2
        total_price = price + price * tax / 100
    print("Total price of " + product_type + " is " + str(total_price) )

purchase_product("Mobile",20000, "Apple",None)
purchase_product("Shoe",200,None,"leather")

# Total price of Mobile is 18000.0
# Total price of Shoe is 210.0


# TRYOUT:
'''A better solution would be to modularize the code and separate the logic for Mobiles and Shoes.

Modify the code as per the below guidelines:

- Create two functions: purchase_mobile and purchase_shoe.
- purchase_mobile() takes two parameters: price and brand.
- purchase_shoe() takes two parameters: price and material.
- If the mobile brand is “Apple”, discount is 10%, else discount is 5%.
- If the shoe material is “leather”, tax is 5%, else tax is 2%.

The modified code would look something like this:'''

def purchase_mobile(price,brand):
    if brand == "Apple" :
        discount = 10
    else:
        discount = 5
    total_price = price - price * discount / 100
    print("Total price of Mobile is "+str(total_price))


def purchase_shoe(price,material):
    if material == "leather" :
        tax = 5
    else:
        tax = 2
    total_price = price + price * tax / 100
    print("Total price of Shoe is "+str(total_price))


purchase_mobile(20000,"Apple")
purchase_shoe(200,"leather")

# Total price of Mobile is 18000.0
# Total price of Shoe is 210.0

# INCREASING REQUIREMENTS:
'''We want to provide users with facility to return products as well.
During return, refund amount should be displayed'''

# Displaying the refund amount
'''How do we go about displaying the refund amount?
One way is to recalculate the price as shown below.
Here, price calculation logic is repeated in purchase as well as in return functions.
This obviously is a bad idea.'''

def return_mobile(price,brand):
    if brand == "Apple" :
        discount = 10
    else:
        discount = 5
    total_price = price - price * discount / 100
    print("Refund price for Mobile is "+str(total_price))


def return_shoe(price,material):
    if material == "leather" :
        tax = 5
    else:
        tax = 2
    total_price = price + price * tax / 100
    print("Refund price for Shoe is "+str(total_price))


return_mobile(20000,"Apple")
return_shoe(200,"leather")

# Refund price for Mobile is 18000.0
# Refund price for Shoe is 210.0



# GLOBAL VARIABLES :

'''Alternatively we can use global variables.

We calculate the price during purchase and store it in a global variable.

Later during return we access the calculated price from the global variable.

But this brings more complications than it tries to solve.'''

total_price_mobile = 0
total_price_shoe = 0
def purchase_mobile(price,brand):
    global total_price_mobile
    if brand == "Apple" :
        discount = 10
    else:
        discount = 5
    total_price_mobile = price - price * discount / 100
    print("Total price of Mobile is "+str(total_price_mobile))


def purchase_shoe(price,material):
    global total_price_shoe
    if material == "leather" :
        tax = 5
    else:
        tax = 2
    total_price_shoe = price + price * tax / 100
    print("Total price of Shoe is "+str(total_price_shoe))


def return_mobile():
    print("Refund price for Mobile is "+str(total_price_mobile))

def return_shoe():
    print("Refund price for Shoe is "+str(total_price_shoe))
    

purchase_mobile(20000,"Apple")
purchase_shoe(200,"leather")
return_mobile()

# Total price of Mobile is 18000.0
# Total price of Shoe is 210.0
# Refund price for Mobile is 18000.0

'''
What if we want to purchase two mobiles and return one of them?

Which will be returned?

Also, can we be sure that purchase_shoe() won't accidentally modify the global value for mobile?'''
total_price_mobile = 0
total_price_shoe = 0
def purchase_mobile(price,brand):
    global total_price_mobile
    if brand == "Apple" :
        discount = 10
    else:
        discount = 5
    total_price_mobile = price - price * discount / 100
    print("Total price of Mobile is "+str(total_price_mobile))


def purchase_shoe(price,material):
    global total_price_shoe
    if material == "leather" :
        tax = 5
    else:
        tax = 2
    total_price_shoe = price + price * tax / 100
    print("Total price of Shoe is "+str(total_price_shoe))


def return_mobile():
    print("Refund price for Mobile is "+str(total_price_mobile))

def return_shoe():
    print("Refund price for Shoe is "+str(total_price_shoe))
    

purchase_mobile(20000,"Apple")
purchase_shoe(200,"leather")
purchase_mobile(2000,"Samsung")
return_mobile()

# Total price of Mobile is 18000.0
# Total price of Shoe is 210.0
# Total price of Mobile is 1900.0
# Refund price for Mobile is 1900.0


'''
We can see that with our current style of programming,
we quickly run into complications trying to simulate real world scenarios,
like purchasing and returning a product.

The problem arises due to the fact that
in real life everything has some data/characteristic
and behavior associated with it.

We are not able to replicate this in the code.

For example:
- All mobiles have price, brand as its data and purchase, return as its behavior.
- All shoes have price, material as its data and purchase, return as its behavior.

We need a way of programming which allows to club together the data and behavior,
so that it becomes easier to code real world scenarios.'''

# Clubbing data and behavior
'''
            Mobile Charecteristics
            Purchase_mobile()
            Mobile Charecteristics
            Return_mobile()
            Shoe_Charecteristics
            purchase_shoe()
            Shoe_Charecteristics
            return_shoe()
                ||
                ||
                ||
Mobile:            Shoe:
- charecteristics  - charecteristics
- purchase()       - purchase()
- return()         - return()'''


# TEMPLATING:
'''Once we have a template of the data and the related behavior we can use that template to create many copies.'''

'''This style of programming
where we create a template
and create copies from that template
is called "Object Oriented Programming".

This style allows us to code for scenarios closely linked with real life.

The template we create is called a "Class"
and the copies we create out of it is called an "Object".'''

# How many objects can you identify in the below picture? - 16
# How many types of objects can you identify in the below picture? - 2
# Is sound an object? Hint: Think if attributes are possible for sound? - YES







# INTRODUCTION TO OOP:

# Class and Objects:
'''
Objects are real world entities.

Anything you can describe in this world is an object.

Classes on the other hand are not real.

They are just a concept.

A class is a classification of certain objects
and it is just a description of the properties
and behavior all objects of that classification should possess.

Class is a like a recipe
and the object is like the cupcake we bake using it.

All cupcakes created from a recipe share
similar characteristics like shape, sweetness, etc.

But they are all unique as well.

One cupcake may have strawberry frosting
while another might have vanilla.

Similarly, objects of a class share similar characteristics
but they differ in their values for those characteristics.

'''

# What does a Class contain? :

''' What does a recipe contain?

It contains list of ingredients which make up the cake and the directions.

Similarly, a class contains the "properties/attributes" of the object
and the "operations/behavior" that can be performed on an object.'''

'''
Mobile:
- Attributes:
    - Price
    - brand
- Behavior:
    - Purchase
    - Return Ite
'''

'''
we can say that this object is
an example of or instance of the Mobile classification.
Under this classification,
there can be many objects and
the object shown above is an instance of or example of it.'''

# How to define a class?

'''A class is defined using the "class" keyword in python.

For example, the below code creates a class called Mobile without any attributes or behavior.'''

class Mobile1:
    pass


# How to create objects?

'''To create an object, we need a class.

The syntax for creating an object is "<classname>()", where <classname> is the name of the class.

For example, the below code creates three Mobile objects:'''

class Mobile2:
    pass

Mobile2()
Mobile2()
Mobile2()

# Reference variables:
'''
Just like we need variables to access and use values,
we need variables to access and reuse the objects that we create.

Such variables that are used to access objects are called "reference variables".

In the below code, we are creating three objects, each with its own reference variable'''

class Mobile3:
    pass

mob1 = Mobile3()
mob2 = Mobile3()
mob3 = Mobile3()



# Revisiting Python collections :
'''
Like any programming language, python also  has built-in classes.

Some of the built-in classes which you have already used are:
- List
- Date
- Tuple
- Set
'''
# "Object literal" is a special syntax through with objects are created and initialized.

'''For e.g.
for list this syntax is square bracket followed by any number of values of objects separated by comma followed by closing bracket.

So the expression you see on right side of assignment operator is the object literal for list.

Object literal for different objects are different to distinguish from each other.

For example,

- list1 = [1,2,3]
- dict1 = { "name" : "Gopal" , "age": 32 }
- tup1 = ( 1, 2, 3 )'''

# Only some inbuilt objects can be created using "object literals".

# ATTRIBUTES OF AN OBJECT :
'''
How can we create attributes and assign values for those attributes?

This can be done by using the . (dot) operator.

The syntax for creating attribute and value for that is as below:'''

#reference_variable.attribute_name = value

'''For example, in the below code we are creating two attributes price and brand,
and assigning them to the two objects we had created.'''


class Mobile4:
    pass

mob1 = Mobile4()
mob2 = Mobile4()

mob1.price = 20000
mob1.brand = "Apple"

mob2.price = 3000
mob2.brand = "Samsung"


# Accessing the attribute values:
'''We can access the attribute values using the dot operator itself.

The syntax is as shown below:'''

# reference_variable.attribute_name
'''For Example'''
print(mob1.brand)
print(mob2.brand)

# Apple
# Samsung




# ASSIGNING vs UPDATING:
'''
We can update the value of an existing attribute using the dot operator.

For example,
the below code will change the ios_version of mob1 object,
since the mob1 object already has that attribute.'''

mob1.ios_version = 11

'''In python, if we assign a value to a non-existent attribute,
it will create that attribute for that object alone.'''

mob2.android_version = "Marshmallow"

'''If we try to access a non-existing attribute, we will get an Attribute Error.
For example,'''

# print(mob2.ios_version)

# BEST PRACTICE :
'''
The below code will not give an error.

However, mob2 will have an attribute ios_versio.

This spelling mistake creates a new attribute!

Hence be careful when assigning values to attributes of an object.'''

class Mobile5:
    pass

mob1 = Mobile5()
mob2 = Mobile5()

mob1.price = 20000
mob1.brand = "Apple"
mob1.ios_version = 11
print(mob1.ios_version) #11

mob2.price = 3000
mob2.brand = "Apple"
mob2.ios_versio = 11
print(mob2.ios_versio) #11

'''The best practice is to ensure all objects of a class have the same set of attributes.

Very rarely should we create separate set of attributes for different objects.

Also, languages like Java, C# etc do not allow us to create different set of attributes for different objects like python does.'''


# CREATING COMMON ATRRIBUTES:
'''
We have already seen the problem arising out of human error in creating attributes individually for objects.

Apart from this problem we also have to deal with the problem of lack of reuse.

For example if an object has 10 attributes and we have 10 objects,
then we have to write 100 lines of code! There is no reuse at all.

We need a way to mention the attributes of all the objects of a class in one place
so that we can create and initialize the attributes.

Let us see how to do this.'''

# CONSTRUCTOR :

'''When we create an object,
the special method __init__()
inside the class of that object
is invoked automatically.

This special method is called as a "constructor".

Try out the below code and observe the output.'''

class Mobile6:
    def __init__(self, brand, price):
        print("Inside constructor")
        self.brand = brand
        self.price = price

mob1 = Mobile6("Apple", 20000)
print("Mobile 1 has brand ", mob1.brand, " and price ", mob1.price)

mob2 = Mobile6("Samsung", 3000)
print("Mobile 2 has brand", mob2.brand, "and price", mob2.price)


'''Note: self has a special meaning which we will discuss soon.
Also, attributes are created using self.attribute_name.'''

# Constructor :
'''You can also create a contructor without parameters.
But this is rarely useful.

Also note that even though the constructor has a parameter "self",
we don't explicitly have to pass value for that parameter.

This will be discussed more in detail later.

If a constructor takes parameters
and if we invoke it with a different number of parameters,
the error message will indicate
how many parameters were missed out or exceeded.'''

class Mobile7:
    def __init__(self, price, brand):
        print("Price:",price)
        print("Brand:",brand)

#Uncomment each line below. Try it out and observe the output.
#mob1=Mobile7() #Mobile7.__init__() missing 2 required positional arguments: 'price' and 'brand'
#mob1=Mobile7(10000,'Samsung','Android') #Mobile7.__init__() takes 3 positional arguments but 4 were given
#mob1=Mobile7(10000,'Samsung')
# Price: 10000
# Brand: Samsung

# DESTRUCTOR :
'''Destructor is a special method
which will be invoked automatically
when the object gets removed from the memory.'''

class Product:
    def __init__(self,price,brand):
        self.price = price
        self.brand = brand
    def __del__(self):
        print('Deleting the Object')

p1=Product(10000,'Apple')
p2=Product(7000,'Samsung')
del p1

'''The first one,
when object p1 is explicitly deleted using del keyword.

The second one,
when the object p2 is deallocated from the memory implicitly.
'''

# How do we create behavior in a class?

'''We can create behavior in a class by adding methods in a class which are similar to functions.

However, such methods should have a special parameter called self as the first parameter.

self is not a keyword, it is just the reference variable using which the method is being invoked.

However, you can change the name of the first parameter if required.

This is how the purchase method/behavior in a mobile class would look like:'''

class Mobile8:
    def __init__(self):
        print("Inside constructor")

    def purchase(self):
        print("Purchasing a Mobile")

mob1 = Mobile8()
mob1.purchase() #Inbound method invocation, We need not pass the value for self.
Mobile8.purchase(mob1) #Outbound method invocation, We have to pass the object as the value of self.

# METHOD INVOCATION :
'''
We can invoke the methods using the dot operator as shown in the above example.

There are two kinds of method invocations such as'''

# 1.Inbound Invocation:
'''In this type of invocation, the method is called by object reference.
The value for self doesn't need to be passed explicitly.'''

# 2.Outbound Invocation:
'''In this type of method invocation, the method is invoked using class reference.
The value of self should be passed explicitly by the user.'''

# How do we access an attribute in a method?
'''
We can access an attribute in a method by using self.

Value of the attribute accessed inside the method is determined by the object used to invoke the method.

For example, in the code below when we invoke purchase using mob1,
attribute values (Apple and 20000) of mob1 are accessed.
Similarly, when mob2 is used to invoke purchase,
attribute values (Samsung and 3000) of mob2 are accessed in purchase().'''

class Mobile9:
    def __init__(self,brand,price):
        print("Inside constructor")
        self.brand = brand
        self.price = price

    def purchase(self):
        print("Purchasing a Mobile")
        print("This mobile has brand",self.brand,"and price",self.price)

print("Mobile-1")
mob1 = Mobile9("Apple",20000)
mob1.purchase()

print("Mobile-2")
mob2 = Mobile9("Samsung",3000)
mob2.purchase()

# Difference between Function and Method
'''
Function: Is a block of code with a name
Method: Is a part of an object and represents the bhaviour of the object.

Function: It can be invoked using the name of the function and passing parameters Ex: len([1,2,3])
Method: It can be invoked only on an object, using dot operator. Without an object we cannot invoke a method. Ex: [1,2,3].reverse()

Function:Parameters are optional in a function
Method:A method must have atleast one parameter : self'''

# ABSTRACTION:
'''
When we invoke the purchase() on a mobile object,
we don’t have to know the details of the method to invoke it.

We don’t have to know how the reverse() method is working in order to use it in our list.

This ability to use something without having to know the details of how it is working is called as "abstraction".'''

# Summary:
'''
- OOP is a style of programming which allows us to club data and behavior together.

- This is more suited for coding real life scenarios

- Objects are real world entities

- Classes are logcal entities and are used for classification.

- Class is a description of attriutes and behaviour that objects of that classification should posses.

- Common attributes are created using a special method called __init__

- Ojects can be created using ClassName() or using object literals for the built in classes.

- Attributes are created using reference_variable.attribute_name = value    syntax.

- behavior is created by defining a function inside the class having a special parameter called self.'''
