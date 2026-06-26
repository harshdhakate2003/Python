# a=5
# for i in range(0,a+1):
#     for j in range(0,i):
#         print("*",end=" ")
#     print()


# a=5
# for i in range(1,a+1):
#     for j in range(0,a-i):
#         print(" ",end="")
#     for k in range(0,i):
#         print("*",end=" ")
#     print()


a=10
for i in range(1,a+1,2):
    for j in range(0,a-i):
        print(" ",end="")
    for k in range(0,i):
        print("*",end=" ")
    print()
    
# for i in range(0,a):
#     print("*",end=" ")
# print()
# for i in range(1,a+1,2):
#     for j in range(0,i):
#         print(" ",end="")
#     for k in range(0,a-i):
#         print("*",end=" ")
#     print()
# for i in range(1,a+1,2):
#     for j in range(0,a-i):
#         print(" ",end="")
#     for k in range(0,i):
#         print("*",end=" ")
#     print()