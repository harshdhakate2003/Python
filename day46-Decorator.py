'''Decorator'''
# A decorator in python is a function that takes another function as input. adds some functionality to it.
# and returns it. It allows you to "wrap" or  modify the behavior of a function or method without changing its acutal code.

# def my_decorator(io):
#     def wrapper():
#         print("Before function is called.")
#         io()
#         print("After function is called.") 
#     return wrapper

# @my_decorator
# def say_hello():
#     print("Hello!, Harsh")

# say_hello()


#---------------------------------------------------------------------------------
# Write a decorator that converts the string of a

# def to_uppercase(func):
#     def wrapper(*args):
#         result=func(*args)
#         return result.upper()
#     return wrapper

# @to_uppercase
# def func():
#     return "Hello Python"

# print(func())


#---------------------------------------------------------------------------------
# Write a decorator that prints "Function is being called" before calling any function

# def my_decorator(io):
#     def wrapper():
#         print("Function is being called")
#         io()
#     return wrapper

# @my_decorator
# def my_func():
#     print("we are learning decorator")
# my_func()


#---------------------------------------------------------------------------------
# Write a decorator that doubles the return value of the function it decorates

# def double_value(io):
#     def wrapper(*args):
#         result=io(*args)
#         return result*2
#     return wrapper

# @double_value
# def func():
#     return 10

# print(func())


#---------------------------------------------------------------------------------
# Write a decorator that cube the return value of the function it decorates

# def cube_value(io):
#     def wrapper(*args):
#         result=io(*args)
#         return result**3
#     return wrapper

# @cube_value
# def func():
#     return 3

# print(func())


