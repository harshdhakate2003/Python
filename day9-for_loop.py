# ------------for-loop----------------------------------

# for i in range(3):
#     print(i,end=" ")

# ------------------------------------------------------

# print("\nPrint form 1 to 5") 
# for i in range(1,6):     # range(start,end)
#     print(i,end=" ")

# ------------------------------------------------------

# print("\nPrint form 1, 3, 5, 7, 9")
# for i in range(1,10,2):  # range(start,end,increament)
#     print(i,end=" ")

# ------------------------------------------------------

# print("\nPrint form 10, 8, 6, 4, 2")
# for i in range(10,0,-2):  # range(start,end,decreament)
#     print(i,end=" ")

# print("\n")

#----------------loop on string------------------------------

# str1="itprenuer"
# for i in str1:
#     print(i,end=" ")

# -------------------------------------------------------

# str2=input("Enter your name : ")
# for i in range(5):
#     print(str2,end=" ")
# print(f"\nlength of string is : {len(str2)}")

# for i in range(len(str2)):
#     print(str2[i],end=" ")


# ------------------------------------------------------
# WAP to print the sum of first 5 natural number

# sum=0
# for i in range(1,6):
#     sum=sum+i
# print(sum)

# ------------------------------------------------------
# WAP to accept number and print the table 

# num=int(input("Enter the number for table : "))
# for i in range(1,11):
#     result=num*i
#     print(f"{num} x {i} = {result}")

# ------------------------------------------------------
# WAP to accept marks of 5 subjects and print total, percent and distinction

# total=0
# for i in range(5):
#     marks=int(input("Enter the marks : "))
#     total=total+marks
# print(f"total = {total}")
# percent=(total/500)*100
# print(f"Percent = {percent}")

# if percent>=75:
#     print("Distinction")
# elif percent>=60:
#     print("First class")
# elif percent>=50:
#     print("Second class")
# else:
#     print("Fail")