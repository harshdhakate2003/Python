# List comprehension - It is a concise way (Shortcut) to create new list.

#-----for creating list of square------
# newl=[x**2 for x in range(1,11)]
# print(newl)

#-----for creating list of cube------
# newl=[x**3 for x in range(1,201)]
# print(newl)

#-----for creating list of double------
# newl=[x*2 for x in range(200,501)]
# print(newl)


#-----------------------------------------------------------------
# Condition Statement in list comprehension

# 1 to 100 square of only even number
# new=[x*x for x in range(1,101) if x%2==0]
# print(new)


# 1 to 51 cube of only odd number
# new=[x**3 for x in range(1,51) if x%2!=0]
# print(new)


# 5 to 501 double of only even number
# new=[x*2 for x in range(5,501) if x%2==0]
# print(new)


#-------------------------------------------------------
# List comprehension with function


# def square(x):
#     return x**2
# sq=[square(num) for num in range(1,11)]
# print(sq)


# def cube(x):
#     return x**3
# cu=[cube(num) for num in range(1,101)]
# print(cu)

#------------------------------------------------------------

#-------------rint all the even numbers from 1 to 500.
# new=[x for x in range(1,501) if x%2==0]
# print(new)

#------------print all the odd numbers from 1 to 500.
# new=[x for x in range(50,1001) if x%2!=0]
# print(new)

#------------print all positive numbers in the list
# lst=[-1,3,5,-7,-9,10]
# newl=[x for x in lst if x>0]
# print(newl)


#------------find the length of the items given in the list
# var=["apple","banana","lichi","kiwi"]
# newl=[len(x) for x in var]
# print(newl)


#------------convert integer into string
# a=[1,2,3,4]
# newl=[str(x) for x in a]
# print(newl)

#------------convert words in the list to capital letter
# var=["apple","banana","lichi","kiwi"]
# cp=[x.upper() for x in var]
# print(cp)

#------------convert words in the list to small letter
# var=["PRIYANKA","HARSH","RITI","AYUSH"]
# low=[x.lower() for x in var]
# print(low)

#------------print the number from 1 to 50 which is divisible by 3 and 5
# newl=[x for x in range(1,51) if x%3==0 and x%5==0]
# print(newl) 

#------------print the words which length is greater than 4
# var=["car","dog","peacock","lichi","captain","ship"]
# newl=[x for x in var if len(x)>4]
# print(newl)

#------------double all the odd number in the list
# a=[2,3,4,5,6,7]
# newl=[x*2 for x in a if x%2!=0]
# print(newl)

#------------cube all the even number in the given list
# a=[2,3,4,5,6,7]
# newl=[x**3 for x in a if x%2==0]
# print(newl)

#------------square all the odd number in above list 
# a=[2,3,4,5,6,7]
# newl=[x**2 for x in a if x%2!=0]
# print(newl)

#------------convert list element to float in given list b
# b=[33,55,57,776,463,353,3622,2455]
# newl=[float(x) for x in b]
# print(newl)

#------------square the number which is greater than 10
# c=[2,4,55,66,3,11,454,45,4]
# newl=[x**2 for x in c if x>10]
# print(newl)

#------------string to list of character
# str="python"
# newl=[x for x in str]
# print(newl)

#------------print pass to marks which marks is greater than 40
# result=[20,44,55,66,9]
# newl=["pass" for x in result if x>40]
# print(newl)

