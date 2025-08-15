'''
str1 = "hello"
str2 = 'world'

print(len(str1))
print(len(str2))
print(str1+str2)
'''

'''
#________________Slicing________________
# Accessing parts of a string
# str[starting index : ending endex] where ending index is not included.

string = "Shehaan"
print(string[1:3]) # he

print(string[3:len(string)])


# Negative slicing -> backward indexingw
string1 = "apple"
print(string1[-5:-2])


#________________String Functions________________
#1. endswith function -> return boolean
print(string1.endswith("le")) #return True

#2. Capitalize Function
print(string1.capitalize()) #capitalize First character i.e: A

#3. replace Function
print(string1.replace("a", "o")) #replace a with o in string1

#4. find Function
print(string1.find("l")) #return index number of "l"

#5. count Function
print(string1.count("p")) #return number of existance in a string
'''


#________________________ Questions ________________________
#1. WAP to input user's name and print it's length
#2. WAP to find the occurance of a in 

'''name = str(input("Enter your First name: "))

print(len(name)) #1
print(name.count("a")) #2'''




# _________________ Conditional Statements _________________
'''
marks = int(input("Enter Marks: "))

if(marks >= 90):
    print("A")
elif(marks >= 80):
    print("B")
elif(marks >= 70):
    print("C")
elif(marks < 70):
    print("D")
'''

# Nested conditions
'''
age = int(input("Enter your age: "));

if(age >= 18):
    if(age >= 80):
        print("You cannot drive")
    else:
        print("You can drive")
else:
    print("You are under age cannot drive")
'''


#________________________ Questions ________________________
#1. check if entered number is even or odd.
num1 = int (input("Enter any number: "))

if(num1 % 2 == 0):
    print("Even Number")
else:
    print("Odd Number")


#2. find the greatest of 3 numbers entered by the user.
n1 = int(input("Enter 1st Number: "))
n2 = int(input("Enter 2nd Number: "))
n3 = int(input("Enter 3rd Number: "))

if(n1 > n2 and n1 > n3):
    print("1st number is the greatest.")
if(n2 > n1 and n2 > n3):
    print("2nd number is the greatest.")
if(n3 > n1 and n3 > n2):
    print("3rd number is the greatest.")


#3. check if a number is a multiple of 7 or not.

num2 = int (input("Enter any number: "))
flag = False

if(num2 % 7 == 0):
    flag = True
else:
    flag = False

if(flag):
    print(flag,": ",num2,"is the multiple of 7")
else:
    print(flag,": ",num2,"is not the multiple of 7")
