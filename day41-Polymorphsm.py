'''Polymorphism -> one name many form.'''
# 1) Duck Typing
# 2) Operater Overloading
# 3) Method Overloading
# 4) Method Overridinng (only used in inheritance)


#-------------------------------------------------------------------------
'''Duck Typing'''

# class Bird:
#     def makesound(self):
#         return "Chirp chirp"
# class Dog:
#     def makesound(self):
#         return "bark bark"
# class Cat:
#     def makesound(self):
#         return "Meow meow"
# class Sheep:
#     def makesound(self):
#         return "humb humb"
    
# def animalsound(animal):
#     print(animal.makesound())

# b=Bird()
# d=Dog()
# c=Cat()
# s=Sheep()

# animalsound(b)
# animalsound(d)
# animalsound(c)
# animalsound(s)


#--------------------------------------------------------------
'''Operater Overloading'''

# Program for substraction

# class Point:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
    
#     # Operater Overloading
#     def __sub__(self,other):
#         return Point(self.x-other.x, self.y-other.y)
    
#     def __str__(self):
#         return f"Point({self.x},{self.y})"
    
# # creating point object
# p1=Point(10,7)
# p2=Point(5,9)

# # using the overloaded - operator
# result = p1 - p2
# print(result)


#--------------------------------------------------------------
# Program for Addittion

# class Point:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
    
#     def __add__(self,other):
#         return Point(self.x + other.x, self.y + other.y)
    
#     def __str__(self):
#         return f"Point({self.x},{self.y})"
    
# p1=Point(10,5)
# p2=Point(5,9)

# result=p1+p2
# print(result)

#--------------------------------------------------------------
# Program for Division

# class Point:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
    
#     def __truediv__(self,other):
#         return Point(self.x / other.x, self.y / other.y)
    
#     def __str__(self):
#         return f"Point({self.x},{self.y})"
    
# p1=Point(10,5)
# p2=Point(5,9)

# result=p1/p2
# print(result)

#--------------------------------------------------------------
# Program for Multiplication

# class Vector:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
    
#     # Overloading the * operator for scaler multiplication
#     def __mul__(self,scaler):
#         return Vector(self.x * scaler, self.y * scaler)
    
#     def __str__(self):
#         return f"Point({self.x},{self.y})"
    
# v=Vector(10,5)

# result = v * 4
# print(result)

#--------------------------------------------------------------
'''Method Overloading'''
# program for addittion

# class Calculator:
#     def add(self,a=0,b=0,c=0):
#         return a+b+c
# c=Calculator()
# print(c.add())
# print(c.add(2))
# print(c.add(2,8))
# print(c.add(5,8,2))

#-----------------------------------------------------------
# program using variable length argument (*args)

# class Calculator:
#     def add(self,*args):
#         return sum(args)

# cal=Calculator()
# print(cal.add(1,5))
# print(cal.add(1,5,4))
# print(cal.add(1,5,4,10))

#-----------------------------------------------------------
# program using variable length argument (**kwargs)

# class info:
#     def information(self,**kwargs):
#         for key,value in kwargs.items():
#             print(f"{key},{value}")
# i=info()
# i.information(name="aditya",age=22,gender="male")
# i.information(name="Harsh",age=22,)


#--------------------------------------------------------------
'''Method Overriding'''

# Method overridding on single inheritence

# class Animal:
#     def speak(self):
#         print("Animal speak")
# class Dog(Animal):
#     def speak(self):
#         print("Dog barks")

# d=Dog()
# d.speak()

#-----------------------------------------------------
# Method overridding on multilevel inheritence

# class Animal:
#     def speak(self):
#         print("Animal speak")
# class Dog(Animal):
#     def speak(self):
#         print("Dog barks")
# class Cat(Dog):
#     def speak(self):
#         print("Cat barks")
# c=Cat()
# c.speak()


#-------------------------------------------------------------
# Method overridding on Multiple inheritence

# class Father:
#     def own(self):
#         print("House")
# class Mother:
#     def own(self):
#         print("Car")
# class Son(Father,Mother):
#     def own(self):
#         print("Bike")

# s=Son()
# s.own()

#-------------------------------------------------------------
# Method overridding on Heirarchical inheritence

# class Parent:
#     def skill(self):
#         print("Cooking")
# class Son(Parent):
#     def skill(self):
#             print("Cricket")
# class Daughter(Parent):
#     def skill(self):
#             print("Singing")

# s=Son()
# s.skill()
# d=Daughter()
# d.skill()

#-------------------------------------------------------------
# Method overridding on Hybrid inheritence


# class A:
#     def feature(self):
#         print("This is feature from A")
# class B(A):
#     def feature(self):
#         print("This is feature form B")
# class C(A):
#     def feature(self):
#         print("This is feature form C")
# class D(B,C):
#     def feature(self):
#         print("This is feature form D")

# obj=D()
# obj.feature()

