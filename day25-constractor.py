# constractor 

# class book:
#     def __init__(self):
#         print("constractor called automatically")

# b=book()

#-----------------------------------------------------------
#constarctor with instance attribute

# class book:
#     def __init__(self,title,author,price):
#         self.title=title
#         self.author=author
#         self.price=price

# b=book("python","abc",1200)
# print("Book details : ")
# print(f"tittle = {b.title}")
# print(f"author = {b.author}")
# print(f"price = {b.price}")

#-----------------------------------------------------------

# class book:
#     def __init__(self,title,author,price):
#         self.title=title
#         self.author=author
#         self.price=price

#     def display(self):
#         print("Book details : ")
#         print(f"tittle = {self.title}")
#         print(f"author = {self.author}")
#         print(f"price = {self.price}")


# t=input("Enter title : ")
# a=input("Enter author : ")
# p=int(input("Enter price : "))
# b=book(t,a,p)
# b.display()


#-----------------------------------------------------------


class contact:
    def __init__(self,name,city,phone,education):
        self.name=name
        self.city=city
        self.phone=phone
        self.education=education

    def display(self):
        print("Contact Details : ")
        print(f"Full name : {self.name}")
        print(f"City : {self.city}")
        print(f"Phone number : {self.phone}")
        print(f"Education : {self.education}")

n=input("Enter full name : ")
c=input("Enter your city : ")
p=int(input("Enter phone number : "))
e=input("Enter your education : ")

a=contact(n,c,p,e)
a.display()



        