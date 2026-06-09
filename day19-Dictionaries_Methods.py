#-----------Dictionaries Methods-----------------------

# my_dict = {"name" : "Alice", "age" : 25, "city" : "New York" }

# print(f"keys : {my_dict.keys()}")
# print(f"keys : {my_dict.values()}")
# print(f"keys : {my_dict.items()}")

# age=my_dict.pop("age")
# print(age)

# pi=my_dict.popitem()
# print(pi)

# print("Dictionaries")
# print(my_dict)

# my_dict.update({"city" : "Boston", "job" : "Engineer"})
# print(my_dict)

# my_dict.clear()
# print(f"dict : {my_dict}")

# new_dict= {"a" : 1, "b" : 2}

# dict_copy = new_dict.copy()
# print(f"dict copy : {dict_copy}")


#----------------------------------------------------------------------
# **kvargs (Variable length arguments in function)

# def display(**kvargs):
#     for k, v in kvargs.items():
#         print(f"Key : {k}")
#         print(f"Value : {v}")
#         print("---------------")

# display(name="alice", age=20, city="nagpur")


#---------------------------------------------------

# def display(**kv):
#     print("contact details : ")
#     print("--------------------")
#     for k, v in kv.items():
#         print(f"{k} : {v}")

# fn=input("Enter your full name : ")
# city=input("Enter the name of city : ")
# ph=int(input("Enter phone number : "))
# c=input("Enter the course name : ")

# display(name=fn, city=city, Phone=ph, course=c)