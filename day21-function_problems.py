# Define a function is_even(n) that takes an integer n and returns True if even, False otherwise. Read t test cases, then for each, read n and print "Yes" or "No".
# Input: First line: t (1 ≤ t ≤ 10) Next t lines: integer n (|n| ≤ 10^4)
# Output: "Yes" or "No" for each test case


# def is_even(n):
#     if n%2==0:
#         return True
#     else:
#         return False
    
# for i in range(1,11):
#     if is_even(i):
#         print(f"{i} = {"Yes"}")
#     else:
#         print(f"{i} = {"No"}")


#-----------------------------------------------------------

# Define a function factorial(n=0) that returns n! (0! = 1). Use default parameter. Read a single integer n (0 ≤ n ≤ 12) and print the factorial.
# Input: Single integer n Output: n!


# def fact(n=0):
#     f=1
#     for i in range(1,n+1):
#         f=f*i
#     print(f"factorial of {n} is {f}")

# fact(5)

#-----------------------------------------------------------

# Define a function print_full_name(first, last) that prints "Hello [first] [last]! You just delved into python." Read first_name and last_name (strings, 1-10 chars each).
# Input: First line: first_name Second line: last_name
# Output: The formatted greeting

# def print_full_name(first,last):
#     print(f"Hello {first} {last}, How are you?")

# print_full_name("Harsh","Dhakate")

#-----------------------------------------------------------

# Problem: Define a function count_substring(string, sub_string) that returns the number of times sub_string appears in string. Read string and sub_string, print the count.
# Example: count_substring("abababa", "aba") → 3
# Input: First line: string (|string| ≤ 100) Second line: sub_string (|sub_string| ≤ 100)
# Output: Integer count

# def count_substring(string, sub_string):
#     count = 0
#     start = 0
#     while start <= len(string) - len(sub_string):
#         pos = string.find(sub_string, start)
#         if pos == -1:
#             break
#         count += 1
#         start = pos + 1
#     return count

