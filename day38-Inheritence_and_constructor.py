# Singel level inheritance

# class Parent:
#     def house(self):
#         print("Owns House")
# class Child(Parent):
#     def bike(self):
#         print("Owns Bike")
# obj=Child()
# obj.house()
# obj.bike()


#---------------------------------------------------------
# Multilevel inheritance

# class GrandFather:
#     def land(self):
#         print("Owner of land")
# class Father(GrandFather):
#     def house(self):
#         print("Owner of house")
# class Child(Father):
#     def bike(self):
#         print("Owner of bike")
# o=Child()
# o.land()
# o.house()
# o.bike()


#---------------------------------------------------------
# Multiple inheritance

# class Father:
#     def land(self):
#         print("Father have land")
# class Mother:
#     def house(self):
#         print("Mother have house")
# class Child(Father,Mother):
#     def car(self):
#         print("Child have a car")
# o=Child()
# o.land()
# o.house()
# o.car()

#---------------------------------------------------------
# Create a class writter and method write(). 
# create a class speaker with method speak(). 
# create a class person that inherits both and has method show()

# class Writter:
#     def write(self):
#         print("Writting a letter")
# class Speaker:
#     def speak(self):
#         print("Speaking with friend")
# class Person(Writter,Speaker):
#     def show(self):
#         print("Showing a certificate")
# o=Person()
# o.write()
# o.speak()
# o.show()


#---------------------------------------------------------
# heirarchical inheritance

# class Parent:
#     def Sname(self):
#         print("Sirname is Dhakate")
# class Son(Parent):
#     def hobby(self):
#         print("Playing Cricket")
# class Daugher(Parent):
#     def hobby(self):
#         print("Playing Chess")
# s=Son()
# s.Sname()
# s.hobby()

# d=Daugher()
# d.Sname()
# d.hobby()


#---------------------------------------------------------
# Create a parent class shape with method display() "This is shape"
# child classes 
# 1. circle-circlearea()-"this is circle area"
# 2. square-squareare()-"this is square area"


# class Shape:
#     def display(self):
#         print("This is shape")
# class Circle(Shape):
#     def circlearea(self,r):
#         self.r=r
#         print(f"The area of circle is {3.14*self.r*self.r}")
# class Square(Shape):
#     def squarearea(self,side):
#         self.side=side
#         print(f"The area of circle is {self.side*self.side}")
# c=Circle()
# c.display()
# c.circlearea(5)

# s=Square()
# s.display()
# s.squarearea(20)

#---------------------------------------------------------
# hybrid inheritence
# combination of two or more types of inheritence

# class A:
#     def feature1(self):
#         print("This is feature1 from A")
# class B(A):
#     def feature2(self):
#         print("This is feature2 form B")
# class C(A):
#     def feature3(self):
#         print("This is feature3 form C")
# class D(B,C):
#     def feature4(self):
#         print("This is feature4 form D")

# obj=D()
# obj.feature1()
# obj.feature2()
# obj.feature3()
# obj.feature4()


#---------------------------------------------------------
# Constructor

# create a class Mobile with Constructor to initialize brand, storage, price.
# create one object and print all values

# class Mobile:
#     def __init__(self,brand,storage,price):
#         self.brand=brand
#         self.storage=storage
#         self.price=price
# m=Mobile("Apple",128,100000)
# print(m.brand)
# print(m.storage)
# print(m.price)


#---------------------------------------------------------
# create a class employee with constructor to initialize name, salary, designation(take form user)

# class Employee:
#     def __init__(self,name,salary,designation):
#         self.name=name
#         self.salary=salary
#         self.designation=designation
# n=input("Enter the name: ")
# s=int(input("Enter the salary: "))
# d=input("Enter the designation: ")
# obj=Employee(n,s,d)
# print(f"The name of employee is {obj.name}")
# print(f"The salary of employee is {obj.salary}")
# print(f"The designation of employee is {obj.designation}")
    

#---------------------------------------------------------
# create a class book with constuctor to initialize tittle, author, price

# class Book:
#     def __init__(self,tittle,author,price):
#         self.tittle=tittle
#         self.author=author
#         self.price=price
#         print(f"The tittle of book is {self.tittle}")
#         print(f"The author of book is {self.author}")
#         print(f"The price of book is {self.price}")
# o=Book("Galaxy","Harsh",500)


#---------------------------------------------------------
# create a class Person that takes name and age as input and prints them using a method show()

# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def show(self):
#         print(f"The name of person is {self.name}")
#         print(f"The age of person is {self.age}")
# p=Person("Harsh",22)
# p.show()

#---------------------------------------------------------
# Create a class rectangle with attributes length and breath. 
# add a method area() that returns the area of rectangle

# class Rectangle:
#     def __init__(self,length,breath):
#         self.length=length
#         self.breath=breath
#     def area(self):
#         print(f"The area of rectangle is {self.length*self.breath}")
# r=Rectangle(15,20)
# r.area()