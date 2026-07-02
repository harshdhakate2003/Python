'''File Handling'''

#---------To write the data in txt file

# with open("day6.txt","r") as files:
#     lines=files.readlines()
# for i in lines:
#     print(i)

#---------To write the data in txt file. It will remove the previous data

# with open("day6.txt","w") as files:
#     files.write("My name is Harsh\n")
#     print("written successfull")

#---------To append the data in txt file. It will append the data in file

# with open("day6.txt","a") as files:
#     files.writelines("I am 22 years old\n")
#     print("Append successfull")

#------------------------------------------------------------------------
# Take the data from user and write it to txt files

user=input("Enter the data to add in file: ")
with open("day6.txt","w") as files:
    files.write(user)
    print("writtern successfull")

