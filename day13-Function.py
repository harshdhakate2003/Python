# function without argument

# def display():
#     print("Welcom to ITP")
#     print("python nov batch")
#     print("timing 2 to 3 pm")
# display()

#----------------------------------------------------

# def greet():
#     print("Hello Everyone")
#     print("Good afternoon")

# greet()

#----------------------------------------------------
# function with argument

# def calculate(n1,n2,op):
#     result=0

#     if op=="+":
#         result=n1+n2
#     elif op=="-":
#         result=n1-n2
#     elif op=="*":
#         result=n1*n2
#     elif op=="/":
#         result=n1/n2
#     elif op=="**":
#         result=n1*n2
    
#     print(f"Result = {result}")

# n1=int(input("Enter a number : "))
# n2=int(input("Enter a number : "))
# op=input("Enter a oprater +,-,*,/,** : ")
# calculate(n1,n2,op)
    
#----------------------------------------------------
# function using return keyword

# def calculate(n1,n2,op):
#     result=0

#     if op=="+":
#         result=n1+n2
#     elif op=="-":
#         result=n1-n2
#     elif op=="*":
#         result=n1*n2
#     elif op=="/":
#         result=n1/n2
#     elif op=="**":
#         result=n1*n2
    
#     return result

# n1=int(input("Enter a number : "))
# n2=int(input("Enter a number : "))
# op=input("Enter a oprater +,-,*,/,** : ")

# r = calculate(n1,n2,op)
# print(f"Result = {r}")

#----------------------------------------------------
# WAP to calculate a factorial using function

def factorial(n):
    fact=1
    while(n>0):
        fact=fact*n
        n-=1
    return fact

n=int(input("Enter a number : "))
r=factorial(n)
print(f"Result = {r}")