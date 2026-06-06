# List methods 
co=[]

# append
c=input("Enter the cousre name : ")
co.append(c)
print(co)

# extend
cl=["python","html","java","go","c"]
co.extend(cl)
print("After extending")
print(co)

# insert
co.insert(1,"javascript")
print("after inserting at position")
print(co)

# remove
co.remove("javascript")
print("after removing")
print(co)

# pop
p=co.pop(1)
print("after pop")
print(f"pop item {p}")
print(co)

# index
i=co.index("html")
print(f"index of html is {i}")

# count
c=co.count("java")
print(f"count of java : {c}")

# sort
co.sort()
print("after sorting")
print(co)

# reverse
co.reverse()
print("after reversing")
print(co)

# concatination in list
num1=[1,2,3]
num2=[4,5,6]
n = num1 + num2
print(n)

