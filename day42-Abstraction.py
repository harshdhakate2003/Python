'''Abstraction'''

'''Abstraction is the concept of hiding the internal implementation details 
and showing only the functionality to the user.

Note: We can not instantiate (create) an object of an abstact class in python'''


# from abc import ABC, abstractmethod
# # abc -> abstract base class
# class Vehicle(ABC):
#     @abstractmethod
#     def start_engine(self):
#         print("anjali")

# class Car(Vehicle):
#     def start_engine(self):
#         print("Car engine started")

# car=Car()
# car.start_engine()


#-----------------------------------------------------------------------
# WAP to make abstract base class ATM with function withdraw 

# from abc import ABC,abstractmethod
# class ATM(ABC):
#     @abstractmethod
#     def withdraw(self):
#         print("Amount has been withdraw")
# class User(ATM):
#     def withdraw(self):
#         print("Amount is withdraw")
# a=User()
# a.withdraw()


#-----------------------------------------------------------------------
# Create abstact base class vehicle with method start and stop

# from abc import ABC, abstractmethod
# class Vehicle(ABC):
#     @abstractmethod
#     def start(self):
#         print("Bike is started")
    
#     @abstractmethod
#     def stop(self):
#         print("Bike is stoped")

# class Driver(Vehicle):
#     def start(self):
#         print("Car is started")
    
#     def stop(self):
#         print("Car is stoped")

# d=Driver()
# d.start()
# d.stop()


#-----------------------------------------------------------------------
# Create an abtract class Shape with method area that calculates area of a circle

# from abc import ABC, abstractmethod
# class Shape(ABC):
#     @abstractmethod
#     def area(self,r):
#         self.r=r
#         print(f"Area of a Small circle is {3.14*self.r*self.r}")
# class Circle:
#     def area(self,r):
#         self.r=r
#         print(f"Area of a Big circle is {3.14*self.r*self.r}")
# c=Circle()
# c.area(5)

#-----------------------------------------------------------------------
# Write a python program using abstraction for a "Payment" system with method pay()
# and generate_invoice()

# from abc import ABC, abstractmethod
# class Payment(ABC):
#     @abstractmethod
#     def pay(self, amount):
#         pass

#     def generate_invoice(self):
#         print("Invoice generated")

# class CreaditCardPayment(Payment):
#     def pay(self,amount):
#         print(f"Paid {amount} using Credit Card.")

# c=CreaditCardPayment()
# c.pay(500)
# c.generate_invoice()


#-----------------------------------------------------------------------
'''Constructor with Abstraction'''

# from abc import ABC, abstractmethod
# class Animal(ABC):
#     def __init__(self, name):
#         self.name=name
    
#     def sleep(self):
#         print(f"{self.name} is sleeping")
    
#     @abstractmethod
#     def make_sound(self):
#         print("Alpesh wants to go home")
# class Dog(Animal):
#     def make_sound(self):
#         print("Alpesh cant to go home")
# d=Dog("Harsh")
# d.make_sound()
# d.sleep()