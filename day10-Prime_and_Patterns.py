# WAP to accept a number and print the factorial of number

# num=int(input("Enter a number : "))
# fact=1
# for i in range(1,num+1):
#     fact=fact*i
# print(f"Factorial of {num} is {fact}")


#--------------------------------------------------------------
# WAP to accept number and print whether number is prime or not

# num=int(input("Enter a number : "))
# for i in range(2,num):
#     if(num%i==0):
#         print(f"{num} is not a prime number")
#         break
# if num==i+1:
#     print(f"{num} prime number")


#--------------------------------------------------------------
# WAP to print all prime number up to num

# for num in range(11):
#     i=0
#     for i in range(2,num):
#         if(num%i==0):
#             break
#     if num==i+1:
#         print(f"{num} prime number")


#--------------------------------------------------------------
# Pattern Program
# 1 1 1 
# 2 2 2 
# 3 3 3

# for i in range(1,4):
#     for j in range(1,4):
#         print(i, end=" ")
#     print()


#--------------------------------------------------------------
# Pattern Program
# 1 2 3 
# 1 2 3 
# 1 2 3

# for i in range(1,4):
#     for j in range(1,4):
#         print(j, end=" ")
#     print()


#--------------------------------------------------------------
# Pattern Program
# 1 
# 2 2 
# 3 3 3

# for i in range(1,4):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()


#--------------------------------------------------------------
# Pattern Program
# 1 
# 2 3 
# 4 5 6

# k=1
# for i in range(1,4):
#     for j in range(1,i+1):
#         print(k,end=" ")
#         k=k+1
#     print()


#--------------------------------------------------------------
# Pattern Program
# 1 
# 3 5 
# 7 9 11

# k=1
# for i in range(1,4):
#     for j in range(1,i+1):
#         print(k,end=" ")
#         k=k+2
#     print()


#--------------------------------------------------------------
# Pattern Program
# 1 2 3
# 1 2 
# 1


for i in range(3,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
