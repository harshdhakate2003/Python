# WAP to program to accept to numbers and perform the operation +, -, *, / 

# n1=int(input("Enter the first number : "))
# n2=int(input("Enter the second number : "))
# op=input("Enter the operation + - * / : ")

# match op:
#     case "+":
#         result=n1+n2
#     case "-":
#         result=n1-n2
#     case "*":
#         result=n1*n2
#     case "/":
#         result=n1/n2
#     case _:
#         print("Invalid opreater")
# print(f"result = {result}")


#--------------------------------------------------------------------
# Traffic ligth program using match-case

# light=input("Enter the traffic light (red/yellow/green) : ").lower()
# match light:
#     case "red":
#         print("STOP")
#     case "yellow":
#         print("WAIT")
#     case "green":
#         print("GO")
#     case _:
#         print("Invalid color")
    


#--------------------------------------------------------------------
# WAP to order something

# print("please select something")
# print("1.Tea\n2.Coffee\n3.Water\n4.Exit")
# choice=int(input("Enter your choice : "))

# match choice:
#     case 1:
#         print("you ordered tea , total bill is 10 rupees")
#     case 2:
#         print("you ordered coffe , total bill is 50 rupees")
#     case 3:
#         print("you ordered water , total bill is 20 rupees")
#     case 4:
#         print("Thanks , have a nice day sir!")



#--------------------------------------------------------------------
# WAP to admission details

print("please select an option ")
print("1. Admission\n2. fees payment\n3. Exit")
choice=int(input("Choose an option : "))
match choice:
    case 1:
        name=input("Enter name : ")
        course=input("enter course : ")
        print(f"admission details")
        print(f"full name : {name}")
        print(f"course name : {course}")
    case 2:
        name=input("Enter name : ")
        amount=int(input("Enter fees amount : "))
        print(f"payment details")
        print(f"full name : {name}")
        print(f"amount : {amount}")
    case 3:
        print("Thanks , have a nice day sir!")
    case _:
        print("Invalid option")