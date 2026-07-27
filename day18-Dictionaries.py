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


# Dictionary
student = {
    "name": "Harsh",
    "age": 23,
    "course": "Python Full Stack",
    "city": "Nagpur"
}

print("Original Dictionary:", student)

# 1. get() - Get the value of a key
print("\n1. get():")
print(student.get("name"))

# 2. keys() - Get all keys
print("\n2. keys():")
print(student.keys())

# 3. values() - Get all values
print("\n3. values():")
print(student.values())

# 4. items() - Get key-value pairs
print("\n4. items():")
print(student.items())

# 5. update() - Add or update key-value pairs
print("\n5. update():")
student.update({"email": "harsh@gmail.com"})
print(student)

# 6. pop() - Remove a specific key
print("\n6. pop():")
student.pop("city")
print(student)

# 7. popitem() - Remove the last key-value pair
print("\n7. popitem():")
student.popitem()
print(student)

# 8. setdefault() - Add key if it does not exist
print("\n8. setdefault():")
student.setdefault("gender", "Male")
print(student)

# 9. copy() - Copy the dictionary
print("\n9. copy():")
student_copy = student.copy()
print(student_copy)

# 10. fromkeys() - Create a dictionary from keys
print("\n10. fromkeys():")
keys = ["name", "age", "course"]
new_student = dict.fromkeys(keys, "Not Available")
print(new_student)

# 11. clear() - Remove all items
print("\n11. clear():")
student_copy.clear()
print(student_copy)