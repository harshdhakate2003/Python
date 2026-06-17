#------------------Inheritance-----------------

# class Account:
#     actno=0
#     bal=1000

# class Saving(Account):
#     def deposit(self,amount):
#         self.bal=self.bal+amount
#         print("amount deposited successfully")

# s=Saving()
# s.actno=int(input("enter account number : "))
# amt=int(input("enter amount to be deposited : "))
# s.deposit(amt)
# print(f"actno : {s.actno}")
# print(f"balance : {s.bal}")

#--------------------------------------------------------------------------

class Person:
    name="Harsh"
    address="annpurna nagar"

class Student(Person):
    def display(self,roll,course):
        self.roll=roll
        self.course=course

s=Student()
r=int(input("Enter a roll number : "))
c=input("Enter the course name : ")
s.display(r,c)
print(f"name : {s.name}")
print(f"address : {s.address}")
print(f"roll : {s.roll}")
print(f"course : {s.course}")

