# Create a abstract base class shape with an abstract method area 
# create a sub class rectnagle with contructor for
# length and breath make a function area that prints area of a rectangle.

# from abc import ABC, abstractmethod
# class Shape(ABC):
#     @abstractmethod
#     def area(self,r):
#         a=3.14*r*r
#         print(a)

# class Rectangle(Shape):
#     def __init__(self,l,b):
#         self.l=l
#         self.b=b
    
#     def area(self):
#         area=self.l*self.b
#         print(f"Area of rectangle is {area}")

# r=Rectangle(5,3)
# r.area()


#------------------------------------------------------------------------------
# Create abstract class bank with rate of interest method 
# create two classes SBI and HDFC 

# from abc import ABC, abstractmethod
# class Bank(ABC):
#     @abstractmethod
#     def Rateofinterest(self,p,r,t):
#         self.p=p
#         self.r=r
#         self.t=t
#         rate=(self.p*self.r*self.t)/100
#         print(f"The rate of interest of Bank {rate}")
    
# class Sbi(Bank):
#     def Rateofinterest(self,p,r,t):
#         self.p=p
#         self.r=r
#         self.t=t
#         rate=(self.p*self.r*self.t)/100
#         print(f"The rate of interest of SBI {rate}")

# class Hdfc(Bank):
#     def Rateofinterest(self,p,r,t):
#         self.p=p
#         self.r=r
#         self.t=t
#         rate=(self.p*self.r*self.t)/100
#         print(f"The rate of interest of HDFC {rate}")

# s=Sbi()
# s.Rateofinterest(5,8,3)

# h=Hdfc()
# h.Rateofinterest(1,5,9)


#------------------------------------------------------------------------------
# Write a program using abstraction for a printer that prints documnets in diffrent format.

# from abc import ABC,abstractmethod
# class Printer(ABC):
#     @abstractmethod
#     def printing(self):
#         print("This is printing a document")

# class Worddoc(Printer):
#     def printing(self):
#         print("Printing the word document")
    
# class Pdf(Printer):
#     def printing(self):
#         print("Printing the Pdf document")

# w=Worddoc()
# w.printing()

# p=Pdf()
# p.printing()


