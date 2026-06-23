# Q1. Decision Making (6 marks)
# a) Write a program that takes a number from user and prints whether it is: "Positive", "Negative" or "Zero" using if-elif-else 

# num=int(input("Enter a number : "))
# if num>0:
#     print("Positive")
# elif num<0:
#     print("Negative")
# else:
#     print("Zero")


# b) Write the same program using match-case statement 

# num=int(input("Enter a number : "))
# match num:
#     case 0:
#         print("Zero")
#     case _ if num>0:
#         print("Positive")
#     case _:
#         print("Negative")


# c) Accept percentage from user and print grade using if-elif ladder: ≥90 → A+ ≥80 → A ≥70 → B ≥60 → C ≥50 → D <50 → Fail 

# per=int(input("Enter the percent of student : "))
# if(per>=90):
#     print("A+ grade")
# elif(per>=80):
#     print("A grade")
# elif(per>=70):
#     print("B grade")
# elif(per>=60):
#     print("C grade")
# elif(per>=50):
#     print("D grade")
# elif(per<50):
#     print("Fail")



# Q2. Loops (8 marks)
# a) Print following pattern using nested for loop 
# * * * * *  * * * *    * * *      * *        *

# for i in range(6,1,-1):
#     for x in range(1,i):
#         print("*",end=" ")
#     print("\n")


# b) Write a program to find sum of all odd numbers between 1 to N (take N from user) using while loop 

# n=int(input("Enter the number : "))
# sum=0
# i=1
# while i<=n:
#     if i%2!=0:
#         sum=sum+i
#     i+=1
# print(sum)


# c) Print first 10 numbers of Fibonacci series using for loop (2 marks)

# n1=0
# n2=1
# print(n1)
# print(n2)
# for i in range(1,9):
#     n3=n1+n2
#     print(n3)
#     n1=n2
#     n2=n3


# Q3. Functions (8 marks)
# a) Write a function is_prime(n) that returns True if number is prime, False otherwise. 

# def is_prime(n):
#     for i in range(2,n):
#         if n%i==0:
#             return False
#             break
#     return True

# print(is_prime(3))


# b) Write a function count_vowels(text) that returns number of vowels present in the string. (Vowels = a,e,i,o,u,A,E,I,O,U) 

# def count_vowels(str):
#     count=0
#     for i in str:
#         if i=="a" or i=="e" or i=="i" or i=="o" or i=="u" or i=="A" or i=="E" or i=="I" or i=="O" or i=="U" :
#             count+=1
#     return count

# print(count_vowels("IceCream"))


# c) Write a function reverse_list(lst) that returns a new list which is reverse of given list without using [::-1] or reverse() method (2 marks)

# def reverse_list(lst):
#     copy=[]
#     le=len(lst)
#     for i in range(le-1,-1,-1):
#         copy.append(lst[i])
#     return copy

# print(reverse_list([1,2,3,4,5,8,9]))


# Q4. List, Tuple, Set, Dictionary (10 marks)
# a) Create a list of 8 city names. Perform following operations in sequence: i) Add "Nagpur" at position 3 ii) Remove third city iii) Sort the list alphabetically iv) Print final list and its length (3 marks)

# lst=["nashik","mumbai","pune","paris","london","tokyo","rome","berlin"]
# lst.insert(3,"nagpur")
# lst.remove("pune")
# lst.sort()
# print(lst)
# print(len(lst))


# b) Create a tuple of 6 fruits. Convert it into list, add 2 more fruits, then convert back to tuple and print. (2 marks)

# t=("mango","apple","kiwi","orange","banana","chiku")
# t=list(t)
# t.append("strawberry")
# t.append("pineapple")
# t=tuple(t)
# print(t)


# c) Create two sets: setA = {10, 20, 30, 40, 50} setB = {30, 40, 50, 60, 70} Print: i) Union ii) Intersection iii) Difference (setA - setB) (2 marks)

# setA = {10, 20, 30, 40, 50}
# setB = {30, 40, 50, 60, 70}
# print(setA.intersection(setB))
# print(setA.union(setB))
# print(setA - setB)


# d) Create a dictionary to store student information (roll no as key):
# Python
# students = {    101: {"name":"Rahul", "marks":[78,85,92]},    102: {"name":"Priya", "marks":[65,72,68]},    ...}
# Write program to: i) Add new student (roll 105) ii) Print name and average marks of roll no 101 (3 marks)

# students = { 
#                 101: {"name":"Rahul", "marks":[78,85,92]},
#                 102: {"name":"Priya", "marks":[65,72,68]},
#                 103: {"name": "Amit", "marks": [80, 75, 70]},
#                 104: {"name": "Neha", "marks": [90, 88, 95]}
#             }
# students[105]={"name":"Harsh", "marks":[55,69,78]}
# name = students[101]["name"]
# marks = students[101]["marks"]
# average = sum(marks) / len(marks)
# print(f"Name of students {name}")
# print(f"average marks of student is {average}")



# Q5. Object Oriented Programming (Basic) (8 marks)
# a) Create a class Rectangle with following features:
# •	Two instance variables: length, breadth
# •	Constructor to initialize them
# •	Method area() → returns area
# •	Method perimeter() → returns perimeter
# •	Method is_square() → returns True if rectangle is square
# Create two rectangle objects and print their area, perimeter and check if they are square. (5 marks)


# class Rectangle:
#     def __init__(self,l,b):
#         self.l=l
#         self.b=b
#     def area(self):
#         a=self.l*self.b
#         return a
#     def perimeter(self):
#         peri=2*(self.l+self.b)
#         return peri
#     def is_square(self):
#         if self.l==self.b:
#             return True
#         else:
#             return False

# r1=Rectangle(5,10)
# print(r1.area())
# print(r1.perimeter())
# print(r1.is_square())

# r2=Rectangle(15,30)
# print(r2.area())
# print(r2.perimeter())
# print(r2.is_square())



# b) Create a simple class BankAccount with:
# •	Attributes: account_holder (str), balance (float)
# •	Methods:
# o	deposit(amount)
# o	withdraw(amount) → should check sufficient balance
# o	get_balance()
# Create one object, do some deposit/withdraw operations and show final balance. (3 marks)


# class BankAccount:
#     def __init__(self,name,bal):
#         self.name=name
#         self.bal=bal
#     def deposit(self,amt):
#         self.bal=self.bal+amt
#         print(f"Deposit amount {amt}")
#     def withdraw(self,amt):
#         if amt <= self.bal:
#             self.bal -= amt
#             print(f"Withdraw amount {amt}")
#         else:
#             print("Insufficient balance")
#     def get_balance(self):
#         print(self.bal)

# a=BankAccount("Harsh", 5000)
# a.deposit(2000)
# a.withdraw(1500)
# a.get_balance()