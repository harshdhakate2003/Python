# List methods 
co=[]

# append
c=input("Enter the cousre name : ")
co.append(c)
print(co)

# extend
cl=["python","html","java","go","c"]
co.extend(cl)
print("After extending")
print(co)

# insert
co.insert(1,"javascript")
print("after inserting at position")
print(co)

# remove
co.remove("javascript")
print("after removing")
print(co)

# pop
p=co.pop(1)
print("after pop")
print(f"pop item {p}")
print(co)

# index
i=co.index("html")
print(f"index of html is {i}")

# count
c=co.count("java")
print(f"count of java : {c}")

# sort
co.sort()
print("after sorting")
print(co)

# reverse
co.reverse()
print("after reversing")
print(co)

# concatination in list
num1=[1,2,3]
num2=[4,5,6]
n = num1 + num2
print(n)


# Python List Operations

# Create a list
numbers = [10, 20, 30, 40, 50]
print("Original List:", numbers)

# Access elements
print("First Element:", numbers[0])
print("Last Element:", numbers[-1])

# append() - Add one element
numbers.append(60)
print("After append:", numbers)

# extend() - Add multiple elements
numbers.extend([70, 80, 90])
print("After extend:", numbers)

# insert() - Add element at a specific position
numbers.insert(1, 15)
print("After insert:", numbers)

# remove() - Remove a specific element
numbers.remove(30)
print("After remove:", numbers)

# pop() - Remove the last element
numbers.pop()
print("After pop:", numbers)

# pop(index) - Remove element using index
numbers.pop(0)
print("After pop(index):", numbers)

# len() - Find length
print("Length:", len(numbers))

# sort() - Sort the list
numbers.sort()
print("Sorted List:", numbers)

# reverse() - Reverse the list
numbers.reverse()
print("Reversed List:", numbers)

# max() and min()
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))

# sum() - Calculate sum
print("Sum:", sum(numbers))

# Check if element exists
if 20 in numbers:
    print("20 is present in the list")

# count() - Count an element
numbers.append(20)
print("Count of 20:", numbers.count(20))

# index() - Find the index of an element
print("Index of 20:", numbers.index(20))

# Slicing
print("First 3 Elements:", numbers[:3])
print("Elements from Index 1 to 3:", numbers[1:4])

# copy() - Copy a list
new_list = numbers.copy()
print("Copied List:", new_list)

# clear() - Remove all elements
numbers.clear()
print("After clear:", numbers)

# Python List Operations

numbers = [10, 20, 30, 40, 50]

print("Original list:", numbers)

# 1. Add element at the end
numbers.append(60)
print("After append:", numbers)

# 2. Add element at a specific position
numbers.insert(2, 25)
print("After insert:", numbers)

# 3. Add multiple elements
numbers.extend([70, 80])
print("After extend:", numbers)

# 4. Access an element
print("First element:", numbers[0])
print("Last element:", numbers[-1])

# 5. Update an element
numbers[1] = 200
print("After update:", numbers)

# 6. Remove an element by value
numbers.remove(25)
print("After remove:", numbers)

# 7. Remove an element by index
numbers.pop(2)
print("After pop:", numbers)

# 8. Find length
print("Length:", len(numbers))

# 9. Check if element exists
print("30 exists:", 30 in numbers)

# 10. Count an element
print("Count of 30:", numbers.count(30))

# 11. Find index
print("Index of 40:", numbers.index(40))

# 12. Sort ascending
numbers.sort()
print("Ascending:", numbers)

# 13. Sort descending
numbers.sort(reverse=True)
print("Descending:", numbers)

# 14. Reverse the list
numbers.reverse()
print("After reverse:", numbers)

# 15. Copy the list
new_list = numbers.copy()
print("Copied list:", new_list)

# 16. Slicing
print("First 3 elements:", numbers[:3])
print("Last 3 elements:", numbers[-3:])

# 17. Delete all elements
numbers.clear()
print("After clear:", numbers)

