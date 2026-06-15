# class Employee:
#     # attribute
#     empno=35
#     empname="Harsh"
# # object of employee class
# emp=Employee()
# print(f"employee number : {emp.empno}")
# print(f"employee name : {emp.empname}")

#------------------------------------------------------------------------------------

# class Laptop:
#     type="electronics"  #class attribute

# l1=Laptop()
# l1.model="Dell"   #instance attribute
# l2=Laptop()
# l2.model="Hp"     #instance attribute

# print("Laptop 1 details :")
# print(f"Type of laptop : {l1.type} , Model of laptop : {l1.model}")
# print("Laptop 2 details :")
# print(f"Type of laptop : {l2.type} , Model of laptop : {l2.model}")


#------------------------------------------------------------------------------------

class Contact:
    fullname=""
    city=""
    phone=0
    
c=Contact()
c.fullname=input("enter full name : ")
c.city=input("enter city : ")
c.phone=int(input("enter phone number : "))
print("contact details")
print(f"full name : {c.fullname}")
print(f"city name : {c.city}")
print(f"phone number : {c.phone}")
