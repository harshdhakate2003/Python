# positional argument in function

# def add(a,b):
#     print(f"a = {a}")
#     print(f"b = {b}")
#     result = a + b
#     print(result)

# add(3,5)

#---------------------------------------------
# keyword argument in function

# def add(a,b):
#     print(f"a = {a}")
#     print(f"b = {b}")
#     result = a + b
#     print(result)

# add(b=2,a=7)

#---------------------------------------------
# defualt argument in function

# def greet(name,msg="Hello"):
#     print(f"Name : {name}")
#     print(f"Greetings : {msg}")

# greet("Harsh")

#---------------------------------------------
# defualt argument in function

# def si(principal,year,interest=5):
#     result = (principal*year*interest) / 100
#     print(f"Simple Interset : {result}")
#     print(f"Total amount you have to pay : {principal+result}")


# ch="yes"
# while ch=="yes":
#     p=int(input("Enter the principal amount : "))
#     y=int(input("Enter the number of years : "))
#     ans=input("Do you want to enter the rate of interest press yes or no : ")

#     if ans=="yes":
#         r=int(input("Enter a rate of interest : "))
#         si(p,y,r)
#     else:
#         si(p,y)
    
#     ch=input("Do you want to continue press yes or no : ")

#----------------------------------------------------------------------------------
# variable length argumemt in function

def cal(*args):
    print(type(args))
    print(args)
    l=len(args)
    print(f"lenght of args is { l }")
    sum=0
    print("elements in args are ")
    for i in range(l):
        print(args[i])
        sum=sum+args[i]
    print(f"sum of elements are {sum}")
cal(1,2,3)


