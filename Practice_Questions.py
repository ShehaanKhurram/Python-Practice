# _______________ Variables & DataTypes _______________
# _______________ Question 01 _______________
# Swap two numbers without using a third variable.
"""a = 10
b = 20
print(a,b)

a, b = b, a
print(a,b)
"""

# _______________ Question 02 _______________
# Take a string input and print its first and last character.
"""name = str(input("Enter your name: "))
print(name[0])
print(name[len(name) - 1])"""



# _______________ Question 03 _______________
# Take 3 numbers as input and print their average.
"""a = float(input("Enter First Number: "))
b = float(input("Enter Second Number: "))
c = float(input("Enter Third Number: "))
avg = (a + b + c) / 3
print("Average is:",avg)
"""

# _______________ Strings _______________
# _______________ Question 01 _______________
# Check if a string is palindrome (same forwards and backwards).

# _______________ Question 02 _______________
# Count how many vowels are in a string.
"""def is_vowel(char):
    if(char == "A" or char == "E" or char == "I" or char == "O" or char == "U"):
        return True
    elif(char == "a" or char == "e" or char == "i" or char == "o" or char == "u"):
        return True
    else:
         return False

string = "Shehaan"
count = 0;
for i in string:
    if(is_vowel(i)):
        count += 1

print("Number of vowels in a string =",count)"""

# or
"""string = "Shehaan"
vowels = "aieouAEIOU"
count = 0;
for i in string:
    if i in vowels:
        count += 1

print("Number of vowels in a string =",count)"""

# _______________ Question 03 _______________
# Convert a string into Title Case without using .title().



# _______________ Lists, Tuples, Dictionaries, Sets _______________
# _______________ Question 01 _______________
# Take 5 integers in a list and find the maximum and minimum.
"""list = []
list.append(int(input("Enter first number: ")))
list.append(int(input("Enter second number: ")))
list.append(int(input("Enter third number: ")))
list.append(int(input("Enter forth number: ")))
list.append(int(input("Enter fifth number: ")))
print("list:",list)

print("Max:",max(list))
print("Min:",min(list))"""

# _______________ Question 02 _______________
# Remove duplicates from a list using a set.
"""set1 = set()
for i in range(len(list)): #(0 default, len(list) condition, i+=1 default increment) 
    set1.add(list[i])

print("Set:",set1)"""


# _______________ Question 03 _______________
# Store students and their marks in a dictionary and print the highest scorer.
"""students = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 90
}

highest_scorer = max(students, key=students.get)
highest_score = students[highest_scorer]

print("Highest scorer:", highest_scorer)
print("Marks:", highest_score)"""

# _______________ Question 04 _______________
# Count the frequency of each word in a string using a dictionary.

"""text = input("Enter a sentence: ")
words = text.lower().split()
print(text)
print(words)
print(words[1])
print(type(words))

freq = {}

for i in words:
    freq[i] = words.count(i)

print("Frequency:",freq)"""

# _______________ Conditional Statements _______________
# _______________ Question 01 _______________
# Check if a number is prime.

# _______________ Question 02 _______________
# Take a year as input and check if it is a leap year.

# _______________ Question 03 _______________
# Take marks as input and print Grade A/B/C/F according to ranges.


# _______________ Loops _______________
# _______________ Question 01 _______________
#Print the Fibonacci series up to n terms.

# _______________ Question 02 _______________
# Print the multiplication table of a given number.

# _______________ Question 03 _______________
# Find the factorial of a number using a loop.



# _______________ Functions _______________
# _______________ Question 01 _______________
# Write a function that checks if a number is even or odd.

# _______________ Question 02 _______________
# Write a function that returns the sum of digits of a number.

# _______________ Question 03 _______________
# Write a function that takes a list of numbers and returns the second largest number.

# _______________ Question 04 _______________
# Write a function that counts the vowels in a string.
