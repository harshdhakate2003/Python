# creating the constructor in the base class of single inheritance

# class Account:
#     actno=0
#     bal=0
#     def __init__(self,actno,bal):
#         print("constructor of account class is called")
#         self.actno=actno
#         self.bal=bal
        
# class Saving(Account):
#     def deposit(self,amount):
#         self.bal=self.bal+amount
#         print("amount deposited successfully")

# actno=int(input("enter account number : "))
# s=Saving(actno,1000)
# amt=int(input("enter amount to be deposited : "))
# s.deposit(amt)
# print(f"actno : {s.actno}")
# print(f"balance : {s.bal}")


#------------------------------------------------------------------------
# creating the contructor in both parent and child class

# class Person:
#     def __init__(self):
#         print("Person constructor")
# class Student(Person):
#     def __init__(self):
#         super().__init__() #super is used to call parent class constructor
#         print("Student constuctor")
# s=Student()

#------------------------------------------------------------------------
# Both classes have there own methods

# class Person:
#     def __init__(self):
#         print("Person constructor")
#     def displayperson(self):
#         print("display method of person class")

# class Student(Person):
#     def __init__(self):
#         super().__init__() #super is used to call parent class constructor
#         print("Student constuctor")
#     def displaystudent(self):
#         print("display method of student class")

# s=Student()
# s.displayperson()
# s.displaystudent()


#------------------------------------------------------------------------
# both classes have same name methods so calling the parent class method using super method.

# class person:
#     def __init__(self):
#         print("person constructor")
#     def display(self):
#         print("display method of person class")

# class student(person):
#     def __init__(self):
#         super().__init__() #super is used to call parent class constructor
#         print("student constructor")
#     def display(self):
#         super().display()
#         print("display method of student class")
        
# s=student()
# s.display()