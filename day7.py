# WAP to check number is even or odd

# num=int(input("Enter number : "))
# if num>0:
#     if num%2==0:
#         print("Even number")
#     else :
#         print("Odd number")
# else:
#     print("Number is nagative or Zero")



#------------------------------------------------------
# WAP to check person is eligible to drive or not

# age=int(input("Enter your age : "))
# lic=bool(input("Enter you have license or not in true false : "))
# if (age>=18) and (lic==True):
#     print("You can drive")
# else:
#     print("You cannot drive")




# -------------------------------------------------------
# WAP for Match-Case

# day_no=int(input("Enter the day number from 1 to 7 : "))

# match day_no:
#     case 1:
#         print("Monday")
#     case 2:
#         print("Tuesday")
#     case 3:
#         print("Wednesday")
#     case 4:
#         print("Thursday")
#     case 5:
#         print("Friday")
#     case 6:
#         print("Saturday")
#     case 7:
#         print("Sunday")
#     case _:
#         print("Invalid number")



# -------------------------------------------------------
# WAP to accept the character and print whether vowel or not

# ch=input("Enter a character : ")
# match ch :
#     case 'a'|'e'|'i'|'o'|'u':
#         print("The character is vowel")
#     case _ :
#         print("The character is not vowel")

# ----------------Another way-------------------------

# ch=input("Enter a character : ")
# if ch in 'aeiou':
#     print("Vowel")
# else:
#     print("Not Vowel")



# -------------------------------------------------------
# WAP to accept month number and print no. of days

month=int(input("Enter the month number : "))
match month:
    case 1|3|5|7|8|10|12:
        print("31 days")
    case 2:
        print("28 or 29 days")
    case _:
        print("30 days")

