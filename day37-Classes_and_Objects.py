# create a class student with attributes name and marks print student details

# class Student:
#     name="Harsh"
#     marks=80
#     print("Name of student is : ",name)
#     print("Marks of student is : ",marks)
# obj=Student()

#-----------------------------------------------------------------
# create a class rectangle to find area and perimeter

class Rectangle:
    def area(self,l,b):
        a=l*b
        print("Area of rectangle is : ",a)
    def peri(self,l,b):
        p=2*(l*b)
        print("Perimeter of rectangle :",p)
obj=Rectangle()
obj.area(5,4)
obj.peri(5,9)

#-----------------------------------------------------------------
# create a class bank account with diposite and withdraw method

# class Bank:
#     def __init__(self,bal):
#         self.bal=bal
#     def dipo(self,amt):
#         self.bal+=amt
#         print("After diposite balance is:",self.bal)
#     def withdr(self,amt):
#         self.bal-=amt
#         print("After withdraw balance is:",self.bal)
# obj=Bank(1000)
# obj.dipo(500)
# obj.withdr(200)


#-----------------------------------------------------------------
# Make a class student with method form and attribute name, age, rollno, course

# class Student:
#     def form(self,name,age,roll,course):
#         self.name=name
#         self.age=age
#         self.roll=roll
#         self.course=course
#         print("Name of Student:",self.name)
#         print("age of Student:",self.age)
#         print("roll of Student:",self.roll)
#         print("course of Student:",self.course)
# obj=Student()
# obj.form("Harsh",22,156,"python")


#-----------------------------------------------------------------
# create a class library with method show and attribute bookname, author, year and display method to print it

# class Library:
#     def show(self,bookname,author,year):
#         self.bookname=bookname
#         self.author=author
#         self.year=year
#     def display(self):
#         print(f"Name of book is {self.bookname}")
#         print(f"Author of book is {self.author}")
#         print(f"Year of book is {self.year}")
# obj=Library()
# obj.show("Ocean","Harsh",2026)
# obj.display()

#-----------------------------------------------------------------
# create a class rectangle with method area that print area of rectangle 

# class Rectangle:
#     def area(self,l,b):
#         self.l=l
#         self.b=b
#     def display(self):
#         area=self.l*self.b
#         print(f"The area of rectangle is {area}")
# obj=Rectangle()
# obj.area(5,5)
# obj.display()

#-----------------------------------------------------------------
# create a class circle with method area and perimeter 

# class Circle:
#     def area(self,r):
#         a=3.14*(r**2)
#         print(f"Area of circle is {a}")
#     def peri(self,r):
#         p=2*3.14*r
#         print(f"Perimeter of circle is {p}")
# obj=Circle()
# obj.area(30)
# obj.peri(30)

#-----------------------------------------------------------------
# create a class newletter with method article and attribute articalname, articalnumber, heading

# class News:
#     def artical(self,artname,artnum,head):
#         self.artname=artname
#         self.artnum=artnum
#         self.head=head
#     def show(self):
#         print(f"The name of artical is {self.artname}")
#         print(f"The number of artical is {self.artnum}")
#         print(f"The heading of artical is {self.head}")
# obj=News()
# obj.artical("Rivers",852,"Polution on river")
# obj.show()


#-----------------------------------------------------------------
# create a class employee with method info and attributes empname and empid and empsalary

# class Employee:
#     def info(self,empname,empid,empsalary):
#         self.empname=empname
#         self.empid=empid
#         self.empsalary=empsalary
#     def show(self):
#         print(f"The name of employee is {self.empname}")
#         print(f"The id of employee is {self.empid}")
#         print(f"The salary of employee is {self.empsalary}")
# obj=Employee()
# obj.info("Harsh",512,15000)
# obj.show()

#-----------------------------------------------------------------
# create a class person with method personinfo and attribute

class Person:
    def personinfo(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def show(self):
        print(f"The name of person is {self.name}\nThe age of person is {self.age}\nThe gender of person is {self.gender}")

o=Person()
o.personinfo("Harsh",22,"male")
o.show()