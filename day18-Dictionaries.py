# ----------Dictionaries-------------------

# my= {"name": "Harsh", "age":22, "city":"Nagpur"}
# print(my)

# # using dict() constructor
# dic=dict(name="Bob", age=30)
# print(dic)

# # Accessing with square brackets
# print(f"Name is {my["name"]}")       # output : Name is Harsh

# # Accessing with get()
# print(f"age is {my.get("age")}")      # output : age is 22
# print(my.get("citys", "citys key does not exist"))          # output : citys key does not exist



#------------------------------------------------------------------------- 
# set is present inside the dictionarie, convert the set to list and print.

# stud={"name": "ravi", "course": {"java", "python"}}
# print(type(stud))

# n=stud["name"]
# print(f"name = {n}")

# c=stud["course"]
# print(type(c))

# c1=list(c)
# print(f"Course 1 : {c1[0]}")
# print(f"Course 1 : {c1[1]}")


#----------------------------------------------------------------------- 

n=input("Enter your name : ")
c1=input("Enter course 1 : ")
c2=input("Enter course 2 : ")

stud={"name" : n, "course": {c1,c2}}

print("Student details : ")
n=stud["name"]
print(f"Name = {n}")

c=stud["course"]
print(type(c))

c1=list(c)
print(f"course 1 : {c1[0]}")
print(f"course 2 : {c1[1]}")

