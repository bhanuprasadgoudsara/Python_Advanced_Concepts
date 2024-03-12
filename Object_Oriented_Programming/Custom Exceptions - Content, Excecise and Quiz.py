# Exception handling and OOP:
'''There are two types of exceptions:

- BUILT-IN EXCEPTIONS: which are readily available with Python.
  Example: ValueError, TypeError, NameError

- USER-DEFINED EXCEPTIONS: are the ones which are created by users based on the requirement.

Now we will take a look at how the user defined exceptions are created and handled in python.'''

# Raise exception:
'''Let us consider a scenario where a customer can have many credit cards which he can use for purchasing.
Each credit card has a number and a balance.

Let us consider a purchase_item() method which takes the price of the item and card number as an input.

In case price is invalid or price is beyond the credit card balance,
we can transfer the control to an except block by raising an exception.

In Python, we can raise exception by using the raise keyword.'''

class CreditCard:
    def __init__(self, card_no, balance):
        self.card_no = card_no
        self.balance = balance

class Customer:
    def __init__(self, cards):
        self.cards = cards

    def purchase_item(self, price, card_no):
        if price < 0:
            raise Exception()
        if card_no not in self.cards:
            raise Exception()
        if price > self.cards[card_no].balance:
            raise Exception()

card1 = CreditCard(101, 800)
card2 = CreditCard(102, 2000)
cards = { card1.card_no : card1, card2.card_no : card2 }
c = Customer(cards)

while(True):
    card_no = int(input("Please enter a card number:"))
    try:
        c.purchase_item(1200, card_no)
        break
    except Exception as e:
        print("Something went wrong. " + str(e))

'''What if we want to treat these exceptions differently,
let’s say if the price is invalid,
then we should just print a message
and if the price is beyond the credit card balance,
we have to ask the customer to use another card.'''

class CreditCard:
    def __init__(self, card_no, balance):
        self.card_no = card_no
        self.balance = balance

class Customer:
    def __init__(self, cards):
        self.cards = cards

    def purchase_item(self, price, card_no):
        if price < 0:
            raise Exception()
        if card_no not in self.cards:
            raise Exception()
        if price > self.cards[card_no].balance:
            raise Exception()

card1 = CreditCard(101, 800)
card2 = CreditCard(102, 2000)
cards = { card1.card_no : card1, card2.card_no : card2 }
c = Customer(cards)

while(True):
    card_no = int(input("Please enter a card number:"))
    try:
        c.purchase_item(1200, card_no)
        break
    except Exception as e:
        print("Something went wrong. " + str(e))

# Raise exception with message
'''We can do this by raising exception with a message as shown.
In this approach, the print statements are not mixed with the business logic.
If we don’t use exceptions.'''

class CreditCard:
    def __init__(self, card_no, balance):
        self.card_no = card_no
        self.balance = balance

class Customer:
    def __init__(self, cards):
        self.cards = cards

    def purchase_item(self, price, card_no):
        if price < 0:
            raise Exception("Invalid Price")
        if card_no not in self.cards:
            raise Exception("Wrong card")
        if price > self.cards[card_no].balance:
            raise Exception("Wrong card")

card1 = CreditCard(101, 800)
card2 = CreditCard(102, 2000)
cards = { card1.card_no : card1, card2.card_no : card2 }
c = Customer(cards)

while(True):
    card_no = int(input("Please enter a card number:"))
    try:
        c.purchase_item(1200, card_no)
        break
    except Exception as e:
        if str(e) == "Invalid Price":
            print("Product price is wrong")
            break
        if str(e) == "Wrong card":
            continue

'''But even this approach of sending messages with exceptions is not ideal as we end up writing
if/else conditions in our except block.
    Such logic is prone to errors.'''

# Create custom exceptions:
'''The solution is to create custom exceptions.
Exception is an inbuilt class in python and
we can create our own exception by inheriting the Exception class as shown:'''

class InvalidPrice(Exception):
    pass

class WrongCard(Exception):
    pass

'''Here we are creating two exception classes which inherit the Exception class.
Only classes of type Exception can be used along with the raise keyword.'''

# Using custom exception:
'''We can use raise these custom exceptions and handle them differently in our except block as shown:'''

class InvalidPrice(Exception):
    pass

class WrongCard(Exception):
    pass

class CreditCard:
    def __init__(self, card_no, balance):
        self.card_no = card_no
        self.balance = balance

class Customer:
    def __init__(self, cards):
        self.cards = cards

    def purchase_item(self, price, card_no):
        if price < 0:
            raise InvalidPrice("The price is wrong")
        if card_no not in self.cards:
            raise WrongCard("Card is invalid")
        if price > self.cards[card_no].balance:
            raise WrongCard("Card has inufficient balance")

card1 = CreditCard(101, 800)
card2 = CreditCard(102, 2000)
cards = { card1.card_no : card1, card2.card_no : card2 }
c = Customer(cards)

while(True):
    card_no = int(input("Please enter a card number:"))
    try:
        c.purchase_item(1200, card_no)
        break
    except InvalidPrice as e:
        print(str(e))
        break
    except WrongCard as e:
        print(str(e))
        continue
    except Exception as e:
        print("Something went wrong. " + str(e))

# Custom exceptions with constructor overriding
'''The custom exception class can override the default constructor provided by the Exception class as shown below'''

class InvalidUsername(Exception):
    def __init__(self, username):
        msg = "The given username " + username + " is invalid"
        super().__init__(msg)

try:
    username = "1abc"
    if not username[0].isalpha():
        raise InvalidUsername(username)
except InvalidUsername as e:
    print(e)

# Order of except:
'''Here we can see that the except block of Exception is executed,
even though we are raising InvalidPrice.

This is because a parent class except block will be able to handle all the child class except blocks also.

Since Exception is parent class to InvalidPrice it can handle the exception of type InvalidPrice.

Therefore, the parent class except blocks must always come after the child class except block.'''

class InvalidPrice(Exception):
    pass
class WrongCard(Exception):
    pass

try:
    raise InvalidPrice()
except InvalidPrice:
    print("InvalidPrice")
except WrongCar:
    print("WrongCard")
except Exception as e:
    print("Exception")

# SUMMARY:
'''
- Custom exceptions are created by inheriting the Exception class
- Custom exception classes give greater flexibility in handling exceptions
- The parent class exceptions must come after the child class exceptions in the except clause.'''
