
import os
#creating the file
file = open("employees.txt", "w")
#storing or wrirting the data to the file
file.write("1,John,50000\n")
file.write("2,Alice,60000\n")
file.write("3,Bob,55000\n")

file.close()

print("File Created Successfully")


#reading all the lines
file = open("employees.txt", "r")

content = file.read()

print(content)

file.close()

#readline reads only one line at a time 

file = open("employees.txt", "r")

line1 = file.readline()


print(line1)


file.close()

#readlines() Reads all lines and stores them in a list.

file = open("employees.txt", "r")

lines = file.readlines()

print(lines)

file.close()

#appending the value 
file = open("employees.txt", "a")

file.write("4,Mom,55009\n")

file.close()

# to check file exits

if os.path.exists("employees.txt"):
    print("File Exists")
else:
    print("File Not Found")


