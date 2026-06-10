#------------Built in module--------------------------

# import math

# print(dir(math))

# s=math.sqrt(9)
# print(f"square root of 9 is {s}")

# pi=math.pi
# print(f"value of pi is {pi}")

#---------------------------------------------------------

# import random

# ans=input("Enter above or below : ")
# r=random.randint(1,10)
# print(f"Random number : {r}")

# if(r<5):
#     if ans=="below":
#         print("You win")
#     else:
#         print("You loose, try again")
# elif(r>5):
#     if ans=="above":
#         print("You win")
#     else:
#         print("You loose, try again")
# else:
#     print("random number is 5")


#---------------------------------------------------------

# from math import sqrt, pi 
# from random import randint

# print(sqrt(4))
# print(randint(1,10))
# print(pi)

#---------------------------------------------------------

# from math import sqrt as s
# from random import randint as r

# print(s(4))
# print(r(1,10))

#-----------------custom module---------------------------

def display(name):
    return f"Hello {name}"

