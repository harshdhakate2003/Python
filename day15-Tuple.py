#-----------Tuple----------
# Tuples are immutable

# student=(50,"Harsh",600.50)
# print(type(student))
# print("Student Details : ")
# print(student)
# print(f"Roll no : {student[0]}")
# print(f"Name : {student[1]}")
# print(f"Fees paid : {student[2]}")

#-------------------------------------------------------------------------
# WAP to accept contact details store it into tuple and the display it.

# fName=input("Enter your full name : ")
# phone=int(input("Enter your mobile number : "))
# city=input("Enter your city : ")
# contact=(fName,phone,city)

# print("Contact Details : ")
# print(f"Full name : {contact[0]}")
# print(f"Mobile number : {contact[1]}")
# print(f"City : {contact[2]}")

#--------------------------------------------------------------------------
# Slicing in Tuple

# #         0  1  2  3  4  5
# numbers=(10,11,12,13,14,15)

# # slicing
# print(numbers[1:4])      #(11, 12, 13)
# print(numbers[:3])       #(10, 11, 12)
# print(numbers[3:])       #(13, 14, 15)
# print(numbers[::2])      #(10, 12, 14)
# print(numbers[::-1])     #(15, 14, 13, 12, 11, 10)

#--------------------------------------------------------------------------
# There are only 2 method are present in the tuple due to thier immutibility

numbers=(10,11,12,13,11,14,15)

# count method
print(numbers.count(11))

# index method
print(numbers.index(13))

n=len(numbers)
print(n)
for i in range(n):
    print(numbers[i])

