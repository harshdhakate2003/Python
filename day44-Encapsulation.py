'''Encapsulation'''
''' Encapsulation is the process of wrapping data and methods together in a class
    and restricting direct access to data. It is achieved using private variables
    and getter/setter methods in Python.'''

# There are three types of access modifier
# 1. public
# 2. protected
# 3. private

#-------------------------------------------
'''Public access modifier'''

# class Student:
#     def __init__(self):
#         self.name = "Rahul"   # Public variable

# obj = Student()
# print(obj.name)   # Accessible

#-------------------------------------------
'''Protected access modifier'''

# class Student:
#     def __init__(self):
#         self._age = 20   # Protected variable

# class Child(Student):
#     def show(self):
#         print(self._age)   # Accessible in subclass

# obj = Child()
# obj.show()

# print(obj._age)   # Possible but not recommended


#---------------------------------------------------------------------
'''Private access modifier using getter and setter'''

# class Student:
#     def __init__(self):
#         self.__marks=80         # private variable

#     def get_marks(self):        # Getter
#         return self.__marks
    
#     def set_marks(self,m):      # Setter
#         if m>0:
#             self.__marks=m
#             print(f"marks after updation {self.__marks}")
#         else:
#             print("Invalid marks")

# s=Student()
# print(s.get_marks())
# s.set_marks(60)


#---------------------------------------------------------------------
# Create a class bankaccount with private variable balance and set balance if amount is greater than hundred

# class Bankaccount:
#     def __init__(self):
#         self.__balance=100
    
#     def get_balance(self):
#         return self.__balance
    
#     def set_balance(self,a):
#         if a>100:
#             self.__balance=a
#             print(f"Updated amount is ",self.__balance)
#         else:
#             print("Amount is not greater than 100")

# b=Bankaccount()
# print(b.get_balance)
# b.set_balance(500)


#---------------------------------------------------------------------
# Create a class laptop where price is read only without setter

# class Laptop:
#     def __init__(self):
#         self.__price=60000
    
#     def get_price(self):
#         return self.__price

# l=Laptop()
# print(l.get_price())


#---------------------------------------------------------------------
# Create a class person with private variable name set new name only if name length is grater than 2

# class Person:
#     def __init__(self):
#         self.__name="Alpesh"
    
#     def get_name(self):
#         return(self.__name)

#     def set_name(self,n):
#         if len(n)>2:
#             self.__name=n
#             print(f"Updated name is {self.__name}")
#         else:
#             print("Name is too short")

# p=Person()
# print(p.get_name())
# p.set_name("Harsh")


#---------------------------------------------------------------------
# Create a class password and private variable pwd update the private variable if length is greater than or equal to 6

# class Password:
#     def __init__(self):
#         self.__pwd="Harsh@123"
    
#     def get_pwd(self):
#         return self.__pwd
    
#     def set_pwd(self,p):
#         if len(p)>=6:
#             self.__pwd=p
#             print(f"Updated password is {self.__pwd}")
#         else:
#             print("password is to short")
# p=Password()
# print(p.get_pwd())
# p.set_pwd("Alpha@123")

