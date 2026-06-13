# WAP print the factorial of number using recursive function

# def fact(n):
#     if n==0 or n==1:
#         return 1
#     return n * fact(n-1)

# print(fact(5))


#--------------------------------------------------------------------------------------
# WAP print the fibonacci series of number using recursive function

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(5))

