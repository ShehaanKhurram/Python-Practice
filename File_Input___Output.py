# ____________________ Read ____________________
"""file = open("demo.txt", "r")

print(file.read()) #read entire file as a string
print(file.readline()) #read one line
print(file.readlines()) #read all lines into a list

file.close()"""

# ____________________ Write ____________________
"""file = open("demo.txt", "w")

file.write("Google chrome, ")
file.write("Hello google")

file.close()"""

# ____________________ Append ____________________
"""file = open("demo.txt", "a")
file.write("Adding another line using append mode!")
file.close()"""

# ____________________ With (keyword) ____________________
"""with open("demo.txt", "r") as file:
    content = file.read()
    print(content) """#automatically close file

# ____________________ Check if exists ____________________
"""import os
with open("demo.txt","r") as file:
    if os.path.exists("demo.txt"):
        print("File exists!")
    else:
        print("File not Found!")"""

# ____________________ delete file ____________________
"""import os

if os.path.exits("demo.txt"):
    os.remove("demo.txt")
else:
    print("File not found!")"""


# ____________________ Questions ____________________
# ____________________ Question 01 ____________________
# Write a Python program to count how many vowels (a, e, i, o, u) are in a text file.

"""file = open("vowels_count.txt", "r")
if file.closed:
    print("File not found!")
else:
    content = file.read()
    words = content.lower().split()
    is_vowel = "aeiou"
    count = 0

    for ch in content:
        if ch in is_vowel:
            count += 1
    print("Total vowals in file:",count)

file.close()
#_____ or _____ >> Different ways to open file
import os
if not os.path.exists("vowels_count.txt"):
    print("File not found!")
else:
    file = open("vowels_count.txt", "r")
    content = file.read()
    words = content.lower().split()
    is_vowel = "aeiou"
    count = 0

    for ch in content:
        if ch in is_vowel:
            count += 1
    print("Total vowals in file:",count)

    file.close()"""


# ____________________ Question 02 ____________________
# Read a file and copy its entire content into another file(copt.txt).

"""import os

if not os.path.exists("demo.txt"):
    print("File not found!")
else:
    with open("demo.txt","r") as fin:
        content = fin.read()
        
        fout = open("demo_copy.txt", "x")
        fout.write(content)
        print("Content copied into another file...\nsuccessful")
        fout.close()"""

# ____________________ Question 03 ____________________
# Write a program to count how many lines and words are in a text file.

"""import os
if not os.path.exists("demo_copy.txt"):
    print("File not found!")
else:
    with open("demo.txt","r") as file:
        content = file.read()
        words = content.split()
        words_count = len(words)

        lines = content.splitlines()
        lines_count = len(lines)

        print("Total Words:",words_count)
        print("Total Lines:",lines_count)
"""


# ____________________ Question 04 ____________________
#Ask the user to enter a filename, then display its content (if it exists).
file = input("Enter a file name: ")
import os
if os.path.exists(file+".txt"):
    print("File Exists!")
    with open(file+".txt", "r") as fin:
        content = fin.read()
        print("Content in a file:",content)
else:
    print("File does not exists!")

# ____________________ Question 05 ____________________
"""
Ask the user for 5 students and their marks.
Save them in a file in this format: Name: Marks
Read the file and find the student with the highest marks.
"""

"""students = {}

for i in range(5):
    name = input(f"Enter the name of student {i+1}:")
    marks = int(input(f"Enter the marks of {name}: "))
    students[name] = marks
   
max_marks = 0

with open("students.txt", "w") as fout:
    for name, marks in students.items():
        fout.write(f"{name} : {marks}\n")

    for name in students.keys():
        if students[name] > max_marks:
            max_marks = students[name]
            topper = name

    print("Max Marks:",max_marks)
    print("Topper:",topper)"""