# ----------Multilevel Inheritance----------------

# class Person:
#     def __init__(self,name):
#         self.name=name
#     def display(self):
#         print(f"name : {self.name}")
# class Employee(Person):
#     def __init__(self,name,salary):
#         super().__init__(name)
#         self.salary=salary
#     def display(self):
#         super().display()
#         print(f"salary : {self.salary}")
# class Parttimeemployee(Employee):
#     def __init__(self,name,salary,hours):
#         super().__init__(name, salary)
#         self.hours=hours
#     def display(self):
#         super().display()
#         print(f"number of hours : {self.hours}")

# p=Parttimeemployee("Harsh",15000,5)
# p.display()


#---------------------------------------------------------------------------

# Problem Statement:
# You are given three classes named A, B, and C.

# Class A has a method display1() that prints:
# This is class A
# Class B inherits from A and has a method display2() that prints:
# This is class B
# Class C inherits from B and has a method display3() that prints:
# This is class C

# Create these three classes using multilevel inheritance.
# In the main part of the program:

# Create an object of class C
# Call all three methods (display1, display2, display3) using that single object.

# Input Format
# (No input – just write the classes)
# Output Format
# textThis is class A
# This is class B
# This is class C



# class A:
#     def display1(self):
#         print("This is class A")
# class B(A):
#     def display2(self):
#         print("This is class B")
# class C(B):
#     def display3(self):
#         print("This is class C")

# obj=C()
# obj.display1()
# obj.display2()
# obj.display3()

#---------------------------------------------------------------------

# Question 2 (Slightly More Realistic – with Attributes)
# Problem:
# Implement multilevel inheritance with the following structure:

# Vehicle (base class)
# Attribute: brand
# Method: show_brand() → prints "Brand: {brand}"

# Car inherits from Vehicle
# Additional attribute: model
# Method: show_model() → prints "Model: {model}"

# ElectricCar inherits from Car
# Additional attribute: battery_size (in kWh)
# Method: show_battery() → prints "Battery: {battery_size} kWh"


# Then:

# Read 3 lines of input:
# brand (string)
# model (string)
# battery_size (integer)

# Create an ElectricCar object and call all three show methods in order.

# Sample Input:
# textTesla
# Model S
# 100
# Sample Output:
# textBrand: Tesla
# Model: Model S
# Battery: 100 kWh


# class Vehicle:
#     def __init__(self,brand):
#         self.brand=brand
#     def show_brand(self):
#         print(f"Brand : {self.brand}")
# class Car(Vehicle):
#     def __init__(self,brand,model):
#         super().__init__(brand)
#         self.model=model
#     def show_model(self):
#         print(f"Model : {self.model}")
# class Electric_car(Car):
#     def __init__(self,brand,model,battery_size):
#         super().__init__(brand,model)
#         self.battery_size=battery_size
#     def show_battery_size(self):
#         print(f"Battery size : {self.battery_size}kWh")

# brand=input("Enter a brand name : ")
# model=input("Enter model name : ")
# battery=input("Enter battery size : ")

# obj=Electric_car(brand,model,battery)
# obj.show_brand()
# obj.show_model()
# obj.show_battery_size()


#-------------------------------------------------------------------------

# Task:
# Make Child.speak() print both messages from Parent and GrandParent (in any order), then also print:
# textI am Child
# Possible Output (one valid version):
# textI am Parent
# I am Grandparent
# I am Child


# class Grandparent():
#     def speak(self):
#         print("I am grandparent")
# class Parent(Grandparent):
#     def speak(self):
#         Grandparent.speak(self)
#         print("I am parent")
# class Child(Parent):
#     def speak(self):
#         Parent.speak(self)
#         print("I am child")

# c=Child()
# c.speak()