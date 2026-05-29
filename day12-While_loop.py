#-------------While loop------------------
# using True  

# num=1
# while True:
#     print(num)
#     num+=1
#     if(num==6):
#         break
# print("bye")

#------------------------------------------
# program to print num from 1 to 5
# Without using True

# num=1
# while num<=5:
#     print(num)
#     num+=1
# print("bye")

#------------------------------------------
# program to print num from 5 to 1

# num=5
# while num>=1:
#     print(num)
#     num-=1
# print("bye")


#------------------------------------------
# using continue

# num=0
# while num<10:
#     num+=1
#     if(num%2==0):
#         continue
#     print(num)
# print("bye")

#------------------------------------------
# factorial using while loop

# num=int(input("Enter the number : "))
# fact=1
# while num>0:
#     fact=fact*num
#     num-=1
# print(f"factorial is {fact}")

#------------------------------------------
# print factorial of number using while loop until user say no

# ch="yes"
# while ch=="yes":
#     num=int(input("Enter the number : "))
#     fact=1
#     while num>0:
#         fact=fact*num
#         num-=1
#     print(f"factorial is {fact}")
#     ch=input("Do you wants to continue press yes or no : ")
# print("bye")

#------------------------------------------
# print the table of number using while loop until user say no

# ch="yes"
# while ch=="yes":
#     num=int(input("Enter the number : "))
#     i=1
#     while i<=10:
#         result=num*i
#         print(f"{num} x {i} = {result}")
#         i+=1
#     ch=input("do you want to continue press yes or no : ")
# print("bye")

#------------------------------------------
# print the number is prime or not using while loop

# ch="yes"
# while ch=="yes":
#     num=int(input("Enter a number : "))
#     i=2
#     while i<num:
#         if(num%i==0):
#             print(f"{num} is not prime")
#             break
#         i+=1
#     if(i==num):
#         print(f"{num} is prime")
#     ch=input("do you want to continue press yes or no : ")
# print("bye")

#------------------------------------------
#sum of first 5 natural no.

# num=1
# sum=0
# while num<=5:
#     sum=sum+num
#     num+=1
# print(sum)


#---------------------------
#product of first 5 natural no.

# num=1
# pro=1
# while num<=5:
#     pro=pro*num
#     num+=1
# print(pro)

#---------------------------
#accept 3 subject marks using while then print total,per and grade

# num=3
# total=0
# while num>=1:
#     sub=int(input("Enter a marks of subject : "))
#     total=total+sub
#     num-=1
# percent=(total/300)*100

# print(f"Total = {total}")
# print(f"percent = {percent}")

# if(percent>=85):
#     print("Grade A")
# elif percent>=70:
#     print("Grade B")
# elif percent>=50:
#     print("Grade C")
# else:
#     print("Grade F")


