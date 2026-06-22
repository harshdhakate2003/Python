# MultiTalent Athlete
# Problem
# In a sports academy, some athletes have multiple talents. You need to create classes for different kinds of athletes using multiple inheritance.
# Create these classes:
# 1.	Runner → has method run() that returns "running fast"
# 2.	Swimmer → has method swim() that returns "swimming smoothly"
# 3.	Triathlete → inherits from bothRunner and Swimmer → has additional method compete() that returns "triathlon: running + swimming"
# Input Format
# First line contains integer T (1 ≤ T ≤ 8) — number of athletes
# Next T lines each contain one word:
# •	runner
# •	swimmer
# •	triathlete
# Output Format
# For each athlete, print what they can do (one line per athlete)
# Sample Input
# text
# 5
# runner
# swimmer
# triathlete
# runner
# triathlete
# Sample Output
# text
# running fast
# swimming smoothly
# triathlon: running + swimming
# running fast
# triathlon: running + swimming
# Constraints
# •	1 ≤ T ≤ 8
# •	Input will contain only valid types
# Your Task
# Write the classes Runner, Swimmer and Triathlete using multiple inheritance.


class Runner:
    def run(self):
        print("running fast")
class Swimmer:
    def swim(self):
        print("Swimming Smoothly")
class Triathlete(Runner,Swimmer):
    def __init__(self,n):
        self.n=n
        lst=[]
        print("Enter which category you wants to add \n1 : runner \n2 : swimmer \n3 : triathlete")
        for i in range(1,self.n+1):
            c=input()
            lst.append(c)

        for x in lst:
            if x=="runner":
                self.run()
            elif x=="swimmer":
                self.swim()
            elif x=="triathlete":
                self.complete()

    def complete(self):
        print("triathlon: running + swimming")

t=Triathlete(3)

