# class Bank:
#     def __init__(self,a,b):
#         self.accNo=a
#         self.balance = b

# ac1= Bank(100,30000)

# print(ac1.__dict__)


# class Students:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         print("My name is {}".format(self.name))
#         print("and i'm {} years old".format(age))
#         # print("This is Address of self ", id(self))

# s1= Students("Hemant Raj", 19)

# print(id(Students))
# print(id(s1))
# print()


# /------------------------------------------

# Inheritance
# Inheritance is the capability of one class to derive or inherit the properties from another class. The class that derives properties is called the derived class or child class and the class from which the properties are being derived is called the base class or parent class. The benefits of inheritance are:

# It represents real-world relationships well.
# It provides the reusability of a code. We don’t have to write the same code again and again. Also, it allows us to add more features to a class without modifying it.
# It is transitive in nature, which means that if class B inherits from another class A, then all the subclasses of B would automatically inherit from class A.
# Types of Inheritance –
# Single Inheritance:
# Single-level inheritance enables a derived class to inherit characteristics from a single-parent class.

# Multilevel Inheritance:
# Multi-level inheritance enables a derived class to inherit properties from an immediate parent class which in turn inherits properties from his parent class.

# Hierarchical Inheritance:
# Hierarchical level inheritance enables more than one derived class to inherit properties from a parent class.

# Multiple Inheritance:
# Multiple level inheritance enables one derived class to inherit properties from more than one base class.


# class Person:
#     def __init__(self, name, id):
#         self.name = name
#         self.id = id

#     def temp(self):
#         print(self.name)
#         print(self.name)

# # childe class


# class employ(Person):
#     def __init__(self, name, id, location, work):
#         self.location = location
#         self.work = work
#         # inheriting the property
#         Person.__init__(self, name, id)

#     def display(self):
#         print(self.location)
#         print(self.work)


# # p1 = Person()
# e1 = employ("hemant", 587, 'maranga', 'sd1')

# # e1.temp()
# # e1.display()

# print(e1.__dict__)
# # print(p1.__dict__)



class Student:
    def __init__(self,name,id):
        self.name= name
        self.id=id
    def show(self):
        print("My name is {} and".format(self.name))
        print("My id is {} and".format(self.id))
    
        # Student.__init__(self,name,id)

# class Staff(Student):
#     def __init__(self, name, id,position,sealery):
#         self.position=position
#         self.sealery=sealery
#         # self.name=name
#         # self.id= id
#         Student.__init__(self,name,id)

#     def display(self):
#         print(self.name)
#         print(self.id)
#         print(self.position)
#         print(self.sealery)



# s1=Staff('hemant',587,'student',2000)
# s1.display()
# s1.show()
# Staff.__dict__()



# ...........................Calculator........................................



class calculator():
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
class addition(calculator):
    def add(self,num1,num2):
        print("{} + {} = {}".format(num1,num2,num1+num2))
        calculator.__init__(self,num1,num2)
class subtractions(calculator):
    def sub(self,num1,num2):
        print("{} - {} = {}".format(num1,num2,num1-num2))
        calculator.__init__(self,num1,num2)
class multiplication(calculator):
    def multi(self,num1,num2):
        print("{} x {} = {}".format(num1,num2,num1*num2))
        calculator.__init__(self,num1,num2)


num1=int(input())
num2=int(input())

cl=addition(num1,num2)
cl.add()