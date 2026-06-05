# create a list to store product details

# prod=[123,"mouse",120.30]
# print(type(prod))
# print(prod)
# print("product details :")
# print(f"product id {prod[0]}")
# print(f"product name {prod[1]}")
# print(f"product price {prod[2]}")

# print("using loop :")
# l=len(prod)
# for i in range(l):
#     print(prod[i])

#-------------------------------------------------------
#---------------Methods in List-------------------------
#----------append method----------

# prod=[]
# for i in range(3):
#     p=input("Enter product name : ")
#     prod.append(p)

# print("Product details :")
# l=len(prod)
# for i in range(l):
#     print(f"product name : {prod[i]}")

#-------------------------------------------------------
# Write a Python program to take details of three contacts (name, phone number, and city), 
# store them as tuples in a list, and display the contact details in a formatted way.

contact=[]
for i in range(3):
    fn=input("Enter name : ")
    ph=int(input("Enter phone number : "))
    ct=input("Enter city : ")
    tuple=(fn,ph,ct)
    contact.append(tuple)

print("contact details : ")
print(contact)

print("contact details : ")
l=len(contact)
for i in range(l):
    print(f"Full name : {contact[i][0]} , Phone number : {contact[i][1]} , City : {contact[i][2]}")

