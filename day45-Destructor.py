'''Destructor'''
# A distructor is a special method called automatically when an object is about to be destroyed
# In python the destructor method is defined using __del__()
# del keyword is used to delete whole object
# __del__() is used to delete the field of objects


# class Student:
#     def __init__(self,name):
#         self.name=name
#         print(f"{self.name} created")

#     def __del__(self):
#         print(f"{self.name} destroyed")

# s1= Student("Harsh")
# del s1
# print(s1.name)


#------------------------------------------------------------
# Q1)Write a Python program to create a class Demo that prints a message
#  when the constructor and destructor are called.

# class Demo:
#     def __init__(self):
#         print("Constructor is called")
    
#     def __del__(self):
#         print("Destructor is called")

# d=Demo()
# del d

#------------------------------------------------------------
# Q2)Create a class Student with attributes name and roll_no.
# Print a message when the object is created and when it is destroyed using a destructor

# class Student:
#     def __init__(self,name,roll):
#         self.name=name
#         self.roll=roll
#         print(f"Object is created for {self.name} and its roll no is {self.roll}")

#     def __del__(self):
#         print("Object is destroyed")

# s=Student("Harsh",50)
# del s


#--------------------------------------------------------------
# Q3)Create a class Employee with attributes name and salary.
# Display a message when the employee object is deleted.

# class Employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#         print(f"Name is {self.name} and salary is {self.salary}")
    
#     def __del__(self):
#         print("Objects is destroyed")

# e=Employee("Ayush",70000)
# del e


#--------------------------------------------------------------
# Q4)Write a program that creates three objects of a class Test and deletes them one by one.
# Display a message from the destructor when each object is destroyed.

# class Test:
#     def __init__(self,marks):
#         self.marks=marks
#         print(f"Marks is {self.marks}")

#     def __del__(self):
#         print("Object is destroyed")
# t1=Test(80)
# t2=Test(75)
# t3=Test(50)

# # Deleting objects one by one
# del t1
# del t2
# del t3

#--------------------------------------------------------------
# Q5)Write a Python program that creates an object of class Car and deletes it using del keyword.
# Print a message from the destructor.

# class Car:
#     def __init__(self,name):
#         self.name=name
#         print(f"Car name is {self.name}")

#     def __del__(self):
#         print("Object is destroyed")
# c=Car("Audi")
# del c


#--------------------------------------------------------------
# Q6)Create two classes A and B each having constructors and destructors.
# Create objects of both classes and observe the order of destructor calls.


# class A:
#     def __init__(self):
#         print("First constructor is called")
    
#     def __del__(self):
#         print("First destuctor is called")

# class B:
#     def __init__(self):
#         print("Second constructor is called")
    
#     def __del__(self):
#         print("Second destuctor is called")
# a=A()
# b=B()
# del a
# del b


#--------------------------------------------------------------
# Q7: Create a class FileHandler that prints when a file is opened and closed using constructor and destructor.

# class FileHandler:
#     def __init__(self):
#         print("File is opened")
    
#     def __del__(self):
#         print("File is closed")

# f=FileHandler()
# del f