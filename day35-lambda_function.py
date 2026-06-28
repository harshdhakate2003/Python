# lambda function is a anomonys function
# used for small operation
# use case : higher order function - It takes function as argument


# cube=lambda x:x**3
# print(cube(3))

# sqr=lambda y:y**2
# print(sqr(4))

# add=lambda x,y:x+y
# print(add(2,8))

# sub=lambda x,y:x-y
# print(sub(10,5))

# mul=lambda x,y:x*y
# print(mul(10,10))

# div=lambda x,y:x/y
# print(div(100,5))

#-----------------------------------------------------------------------
# There are three types of higher order function
# filter function
# map funtion
# reduce funtion

#------------------MAP-FUNCTION-------------------------------------

#-----------with use of function

# a=[2,3,4,5]
# def cube(x):
#     return x**3
# newl=list(map(cube,a))
# print(newl)

#------------with use of lambda function

# a=[2,3,4,5]
# newl=list(map(lambda x:x**3,a))
# print(newl)


# ------------for calculating square----------------

#-----------with use of function

# b=[2,3,4,5]
# def sqr(x):
#     return x**2
# s=list(map(sqr,b))
# print(s)


#------------with use of lambda function

# b=[2,3,4,5]
# sqr=list(map(lambda x:x**2,b))
# print(sqr)


#------------------FILTER-FUNCTION-------------------------------------
# wap to find greater than 4 in list

# a=[1,2,3,4,5,6,7]
# def condition(x):
#     return x>4
# newl=list(filter(condition,a))
# print(newl)

# a=[1,2,3,4,5,6,7]
# newl=list(filter(lambda x:x>4,a))
# print(newl)


#------wap to find greater than 7 in tuple

# a=(1,57,964,61,1,45,6,2,1)
# def condition(x):
#     return x>7
# newl=tuple(filter(condition,a))
# print(newl)


# a=(1,57,964,61,1,45,6,2,1)
# newl=tuple(filter(lambda x:x>7,a))
# print(newl)


#------wap to find even number in a list

# l=[1,2,3,4,5,6,7,8,9,10]
# def even(x):
#     if x%2==0:
#         return x
# newl=list(filter(even,l))
# print(newl)


# l=[1,2,3,4,5,6,7,8,9,10]
# newl=list(filter(lambda x:x%2==0,l))
# print(newl)


#------wap to find odd number in a list

# l=[1,2,3,4,5,6,7,8,9,10]
# def even(x):
#     if x%2!=0:
#         return x
# newl=list(filter(even,l))
# print(newl)


# l=[1,2,3,4,5,6,7,8,9,10]
# newl=list(filter(lambda x:x%2!=0,l))
# print(newl)

#------------------Reduce-FUNCTION-------------------------------------
# reduce function reduce the sequence into single number

# from functools import reduce
# a=[1,23,4,5,68,79]
# def condition(x,y):
#     return x+y
# newl=reduce(condition,a)
# print(newl)


# from functools import reduce
# a=[1,23,4,5,68,79]
# newl=reduce(lambda x,y:x+y,a)
# print(newl)


# from functools import reduce
# a=[1,23,4,5,68,79]
# newl=reduce(lambda x,y:x-y,a)
# print(newl)


# from functools import reduce
# a=[1,2,3,4]
# newl=reduce(lambda x,y:x*y,a)
# print(newl)

# from functools import reduce
# a=[85,9,2,3,8,1]
# newl=reduce(lambda x,y:x/y,a)
# print(newl)

# from functools import reduce
# a=(78,16,22)
# newl=(reduce(lambda x,y:x+y,a))
# print(newl)

# from functools import reduce
# a=(456,152,80)
# newl=reduce(lambda x,y:x-y,a)
# print(newl)

# from functools import reduce
# a=(78,1,5,2)
# newl=(reduce(lambda x,y:x*y,a))
# print(newl)

# from functools import reduce
# a=(595,256,2)
# newl=(reduce(lambda x,y:x/y,a))
# print(newl)

# from functools import reduce
# a={5,6,4,10}
# newl=reduce(lambda x,y:x+y,a)
# print(newl)

# from functools import reduce
# a={15,5,2,6}
# newl=reduce(lambda x,y:x-y,a)
# print(newl)

# from functools import reduce
# a={20,2,1,3}
# newl=reduce(lambda x,y:x*y,a)
# print(newl)

# from functools import reduce
# a={120,2,3}
# newl=reduce(lambda x,y:x/y,a)
# print(newl)


#-----------WAP to print all the number greater than 10

# a=[2,10,11,13,3]
# newl=list(filter(lambda x:x>10,a))
# print(newl)

#-----------WAP count how many number are greater than 10 use filter and len

# a=[2,10,11,13,3]
# newl=len(list(filter(lambda x:x>10,a)))
# print(newl)


#-----WAP find sum of squares using map + reduce. square each number and then find the sum.

# from functools import reduce
# a=[2,10,11,13,3]
# sqr=list(map(lambda x:x**2,a))
# sum=reduce(lambda x,y:x+y,sqr)
# print(sqr)
# print(sum)

#-----WAP get squares of only even numbers 

a=[12,3,4,5,8,9]
even=list(filter(lambda x:x%2==0,a))
sqr=list(map(lambda x:x**2,even))
print(even)
print(sqr)


