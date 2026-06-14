# lst=[]
# n=int(input("Enter the number of command : "))

# for j in range(n):
#     command = input().strip().split()
#     cmd = command[0]

#     if cmd == "insert":
#         i,e = int(command[1]) , int(command[2])
#         lst.insert(i,e)
#     elif cmd == "print":
#         print(lst)
#     elif cmd == "remove":
#         e = int(command[1])
#         lst.remove(e)
#     elif cmd == "append":
#         e = int(command[1])
#         lst.append(e)
#     elif cmd == "pop":
#         lst.pop()
#     elif cmd == "reverse":
#         lst.reverse()


#--------------------------------------------------------------------

# n = int(input("Enter the number of compititer : "))
# arr = list(map(int, input().split()))
# max_score = max(arr)
# runner_up = max(x for x in arr if x != max_score)
# print(runner_up)


#--------------------------------------------------------------------

x = int(input("Enter the number : "))
y = int(input("Enter the number : "))
z = int(input("Enter the number : "))
n = int(input("Enter the number : "))

result = [[i,j,k] for i in range(x+1)
                    for j in range(y+1)
                    for k in range(z+1)
                    if i + j + k != n
        ]

print(result)



