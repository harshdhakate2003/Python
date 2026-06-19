# This is a program of hackerrank

class Person:
    def __init__(self,firstName,lastName,idNumber):
        self.firstName=firstName
        self.lastName=lastName
        self.idNumber=idNumber
    def printPerson(self):
        print(f"first name : {self.firstName}")
        print(f"last name : {self.lastName}")
        print(f"Id Number : {self.idNumber}")
class Student(Person):
    def __init__(self,firstName,lastName,idNumber,scores):
        super().__init__(firstName,lastName,idNumber)
        self.scores=scores
    def calculate(self):
        a=sum(self.scores)/len(self.scores)
        print(f"average of scores : {a}")
        if 90 <= a <= 100:
            print(f"grade : O ")
        elif 80 <= a <90 :
            print(f"grade : E ")
        elif 70 <= a <80 :
            print(f"grade : A ")
        elif 55 <= a <70 :
            print(f"grade : P ")
        elif 40 <= a <55 :
            print(f"grade : D ")
        elif a <40:
            print(f"grade : T ")
s=Student("ravi","kumar",222,[60,60,65])
s.printPerson()
s.calculate()