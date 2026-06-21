# hierarchical inheritance

# class account:
#     def __init__(self,actno,bal):
#         self.actno=actno
#         self.bal=bal
#     def deposit(self,amount):
#         print("deposited method of class")
#     def showbalance(self):
#         return f"bal is {self.bal}"
# class saving(account):
#     def deposit(self, amount):
#         interest=500
#         self.bal=self.bal + amount + interest
#         print("Amount deposited successfully with interest")
# class current(account):
#     def deposit(self, amount):
#         self.bal=self.bal + amount
#         print("Amount deposited successfully without interest")

# a=int(input("Enter account number : "))
# ib=int(input("Enter initial balance : "))
# amt=int(input("Enter amount to be deposited : "))
# acttype=input("Enter account type saving or current : ")

# if acttype=="saving":
#     s=saving(a,ib)
# elif acttype=="current":
#     s=current(a,ib)
# else:
#     print("Invalid account type")

# s.deposit(2000)
# print(s.showbalance())


#-------------------------------------------------------------------------------------

# example of hierarchical inheritance

class Person:
    def __init__(self,name):
        self.name=name
    def display(self):
        return f"name : {self.name}"

# child class
class Employee(Person):
    def __init__(self, name, empid):
        super().__init__(name)
        self.empid=empid
    def display(self):
        return f"empid : {self.empid}, name : {self.name}"
    
# child class2
class Student(Person):
    def __init__(self, name, rollno):
        super().__init__(name)
        self.rollno=rollno
    def display(self):
        return f"rollno : {self.rollno}, name : {self.name}"
    
#creating ojbect
print("employee details")
emp=Employee("rajesh",121)
print(emp.display())
print("student details")
stud=Student("ranjan",222)
print(stud.display())
