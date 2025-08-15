# _______________ Classes _______________

#class creation
"""class Student:
    name = "Shehaan Khurram"
    age = 20


#object creation
s1 = Student()
print(s1.name)
print(s1.age)"""


# _______________ Constructor _______________
# All classes have a function called __init__(), which is always executed when
# the object is created

"""class Student:
    
    Institute = "UCP" #class attribute

    #default constructor -> no need to make
    def __init__(self):
        pass

    #parameterized constructor
    def __init__(self, fullname, Age):   # self(in python) = this(in C++)
        self.name = fullname      # instance attribute
        self.age = Age              


#object creation
s1 = Student("Shehaan Khurram", 20) 
print(s1.name, s1.age, s1.Institute)

s2 = Student("Frenzy", 16)
print(s2.name, s2.age, s2.Institute)"""


# _______________ Methods _______________
# Functions inside a Class

"""class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_marks(self):    # method to get marks  
        return self.marks

    def display(self):      # method to display student details
        print("Name: ", self.name)
        print("Marks: ", self.marks)

s1 = Student("Shehaan Khurram", 95)
s1.display()"""


# _______________ Static Methods _______________
# Methods that do not use a self parameter (Work at class level)
# using decorators: 

"""class Student:
    @staticmethod    #decorator
    def hello():
        print("Hello")
            
s1 = Student()
s1.hello()"""


# _______________ Question _______________
# Create a class that takes name and marks of three subjects as argument in constructor.Then create a method to print the average.

"""class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def cal_avg(self):
        sum = 0
        for i in self.marks:
            sum += i
        avg = sum / len(self.marks)
        return avg

s1 = Student("Shehaan Khurram", [97, 98, 96])
avg = s1.cal_avg()
print("Average Marks:",avg)"""


# ___________________________________________ Abstraction ___________________________________________
# Hiding the implementation(unnecessary for the user) details of a class and only showing the essential features to the user.

"""class Car:
    def __init__(self):
        self.acc = False    #accelerator
        self.brk = False    #break 
        self.clutch = False #clutch of a car

    def start(self):
        self.clutch = True
        self.acc = True
        print("car started...")

c1 = Car()
c1.start()"""

# In this code: Implementaion is hidden in the output i.e pressing clutch and accelerator.

# ___________________________________________ Encapsulation ___________________________________________
# Wrapping data and functions into a single unit(object)

"""class Car:
    def __init__(self, make, model, color):
        self.make = make
        self.model = model
        self.color = color

    def display(self):
        print("Make:", self.make)
        print("Model:", self.model)
        print("Color:", self.color)

c1 = Car("toyota", "Grande", "Grey")
c1.display()"""

# In this code: All the data and methods are wrapped into a single class Car and it's object c1.


# _______________ Question _______________
# Create Account class with 2 attributes: balance & account no.
# Create Methods for Credit, Debit and print the balance.
"""
class Account:
    def __init__(self, bal, accNo):
        self.balance = bal
        self.accountNo = accNo
    
    def debit(self,amount):   #debit -> outgoing money
        self.balance -= amount
        print("Rs.",amount,"was debited.")
        print("Total Balance:",self.get_balance())


    def credit(self, amount):   #credit -> incoming money
        self.balance += amount
        print("Rs.",amount,"was credited.")
        print("Total Balance:",self.get_balance())
    
    def get_balance(self):
        return self.balance

    def display(self):
        print("Account Number:",self.accountNo)
        print("Total Balance:",self.balance)
    
acc1 = Account(5000, 12345)
acc1.display()

acc1.credit(1000)
acc1.debit(500)"""



# _______________ del keyword _______________
# Used to delete object properties or object itself
# del s1.name
# del s1
"""
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Shehaan", 20)
print(s1.name, s1.age)
del s1.age
print(s1.name) # cannot print age now after deletion
del s1 #delete object itself

"""



# _______________ Private(like) attributes & methods _______________
# Private attributes and methods are meant to be used only within the class and are not accessible from outside the class.

# _____________ Private Attributes _____________
"""
class Account:
    def __init__(self, accNo, acc_pass):
        self.accNo = accNo       #public attribute
        self.__acc_pass = acc_pass #private attribute by adding double underscore at start i.e "__" 


    def displayPass(self):
        print(self.__acc_pass)


acc1 = Account("12345", "abcde")
print(acc1.accNo)
acc1.displayPass()"""


# _____________ Private Methods _____________
"""
class Calculation:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def __Sum(self):
        return self.a + self.b

    def average(self):
        s = self.__Sum()
        avg = s / 2
        return avg

nums = Calculation(10,20)
print("Average = ",nums.average())"""



# ___________________________________________ Inheritance ___________________________________________
# When one class(child/derived) derives the properties and methods of another class(parent/base).

#1. _____________ Single Inheritance _____________
"""
class Car:
    @staticmethod
    def start():
        print("car started.")

    @staticmethod
    def stop():
        print("car stopped.")


class ToyotaCar(Car):
    def __init__(self, name):
        self.name = name


car1 = ToyotaCar("Fortuner")
car2 = ToyotaCar("Grande")


print(car1.name)
car1.start()
"""

#2. _____________ Multi-level Inheritance _____________

"""
class Car:     #class 1
    @staticmethod
    def start():
        print("car started.")

    @staticmethod
    def stop():
        print("car stopped.")


class ToyotaCar(Car):  #class 2
    def __init__(self, brand):
        self.brand = brand



class Fortuner(ToyotaCar): #class 3
    def __init__(self,type):
        self.type = type


car1 = Fortuner("Electric") #object of class 3
car1.start() #method of class 1 using object of class 3
"""

#3. _____________ Multi-level Inheritance _____________
# one class inherited by other 2 different classes.
"""
class A:
    varA = "Welcome to class A."

class B:
    varB = "Welcome to class B."

class C(A,B):
    varC = "Welcome to class C."

c1 = C()
print(c1.varA)
print(c1.varB)
print(c1.varC)

"""

# _____________ Super Method _____________
# super() mthod is used to access methods of parent class.
"""
class Car:
    def __init__(self, Type):
        self.type = Type

    @staticmethod
    def start():
        print("car started.")

    @staticmethod
    def stop():
        print("car stopped.")


class ToyotaCar(Car):
    def __init__(self, name, type):
        super().__init__(type)  #parent method calling using super() method.
        self.name = name


car1 = ToyotaCar("Fortuner", "Electric")
print(car1.name)
car1.start()
print(car1.type)"""


# _____________ Class Method _____________
# A class method is bound to the class and receives te class as an implicit first argumant.
# @classmethod -> decorator like @staticmethod
"""
class Person:
    name = "Shehaan"


    @classmethod
    def changeName(cls, name):
        cls.name = name


p1 = Person()
print(p1.name)
p1.changeName("Frenzy")
print(p1.name)
"""

# _____________ Property Decorator_____________
# @property decorator is used in any method in the class to access latest value change. 
"""
class Student:
    def __init__(self, phy, chem, com):
        self.phy = phy
        self.chem = chem
        self.com = com

    @property
    def cal_percentage(self):
        return str((self.phy + self.chem + self.com) / 3) + "%"

st1 = Student(98,97,96)
print(st1.cal_percentage)

st1.phy = 89
print(st1.cal_percentage)
"""


# ___________________________________________ Polymorphism ___________________________________________
# When the same operator is allowed to have different meaning according to the context.
# Operator overloading
# Dunder Functions (important)

#___________ Syntax ___________
"""class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def add(self, num2): #self method including new logic of addition. It is not a Dunder Function.
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)

    def __sub__(self, num2): #self method including new logic of Subtraction. It is a Dunder Function.
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return Complex(newReal, newImg)

    def display(self):
        print(f"{self.real}i + {self.img}j")

c1 = Complex(5, 7)
c2 = Complex(3, 2)

c1.display()
c2.display()

c3 = c1.add(c2) #calling here
c3.display()

c4 = c1 - c2
c4.display()"""



# ____________________ Practice Questions ____________________

# _______________ Question 01 _______________
# create a class Circle and find it's area and parimeter using radius as an attribute.
"""
class Circle:
    pi = 3.14
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.pi * (self.radius**2)

    def perimeter(self):
        return 2 * self.pi * self.radius

c = Circle(21)
print("Area:",c.area())
print("Perimeter:",c.parameter())"""


# _______________ Question 02 _______________
# Create a class Employee with class attribute role, department, salary.
# Create showDetails() method
# Create an Engineer class that inherits properties from employee and has additional attributes name, age.

"""
class Employee:
    def __init__(self,role, dep, salary):
        self.role = role
        self.dep = dep
        self.salary = salary

    def showDetails(self):
        print("Role:",self.role)
        print("Department:",self.dep)
        print(f"Salary: {self.salary}$")


class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "IT", 75000)

    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        self.showDetails()

e1 = Engineer("Shehaan", 20)
e1.display()"""



# _______________ Question 03 _______________
# Create a class called Order which stores item & it's price
# Use Dunder Function __gt__() to convey that: order1 > order2 if order1.price > order2.price
"""
class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, order2):
        return self.price > order2.price

order1 = ("Lays", 30)
order2 = ("Biscuit", 20)

print(order1 > order2) #True in output"""