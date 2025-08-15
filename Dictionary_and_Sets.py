# Dictionaries are to store data values in "key:value pairs"
# They are unordered, mutable(changeable) and don't allow duplicate keys.
# We can you multiple datatypes in a dictionary

info = {
    "key" : "value",
    "name" : "Shehaan", #string
    "age" : 20, #int
    "is_adult" : True, #bool
    "marks" : [92.4, 80, 60], #list
    "subjects" : {"python", "javascript", "c++"} #tuple
}

print (info)
print (type(info))

# If we want to print individual values from dictionary

print("\n")
print("Name:",info["name"])
print("Age:",info["age"])
print("marks:",info["marks"])
print("subjects:",info["subjects"])


# If we want to change some info

info["name"] = "Shehaan Khurram"   #mutable

print("\n")
print("New Name:",info["name"])


# If we want to add new info in dictionary

info["Blood group"] = "O+"
print(info)


# We can create NUll dictionary

null_dict = {}
print(null_dict)


# __________________ Nested Dictionary __________________

print("\n\t _______ Nested Dictionary _______\n\n")

students = {
    "name" : "Shehaan Khurram",
    "subjects" : {
        "DSA" : 95,
        "Maths" : 97,
        "phy" : 92
    }
}

print(students)
print("Subjects:",students["subjects"])

print("Marks of DSA:", students["subjects"]["DSA"])
    

    

# __________________ Dictionary Methods __________________
print("\n\t _______ Dictionary Methods _______\n\n")

#1. dict.keys()
print(students.keys()) #returns all keys
print(len(students)) #total number of keys = 2


#if we want to convert into list form then use typecasting
print(list(students.keys()))
print(len(list(students.keys()))) # total number of keys = 2

#2. dict.values()
print(students.values()) #returns all Values
print(list(students.values())) #values of dictionary

#3. dict.items()
print(students.items()) # in the form of pairs
print("\n")

pair = list(students.items())
print(pair[1])


#4. dict.get("keys")
print(students.get("name"))

#5. dict.update()
students.update({"city" : "Lahore"})
print(students)




# ____________________________ Sets ____________________________
# Sets ar unordered and mutable
# we can store any immutabe type of data type in a set
# but not lists and dictionaries because they are mutable
print("\n\t _______ Sets _______\n\n")


set1 = {1, 2, 2, 4, "Hello", "World", "World"} #unordered set in display
print(set1)
print(type(set1))

# if we want to create an empty set then
# set2 = {} --> Wrong syntax because it is syntax of empty dictionary
# set2 = set() --> Right syntax of empty set

set2 = set()
print(set2)
print(type(set2))


# ______________ Set Methods ______________

collection = set()
print("Empty Set 'Collection':", collection)
#1. add
collection.add(1)
collection.add(2)
collection.add("Hello") # stringw
collection.add((9,8,7)) #tuple
collection.add(2) #repeated values are ignored
print(collection)

#2. remove
collection.remove(1)
print(collection)

#3. clear method is used to make a set empty
print(len(collection))
collection.clear()
print(len(collection))

#4. 'pop' pop random values

#5. Union
set_1 = {1,2,3}
set_2 = {3,4,5}

print("Set 1:",set_1)
print("Set 2:",set_2)
print("Union Set:",set_1.union(set_2))

#5. intersection

print("Intersection Set:",set_1.intersection(set_2))

 


# ______________ Questions ______________
# _____ Question 01 _____
print("\n\t _______ Question 01 _______\n\n")


dictionary = {
        "Cat" : "A small Animal",
        "table" : ["A peice of furniture", "List of facts and figures"]
}

print(dictionary)
print(dictionary["Cat"])
print(dictionary["table"])


# _____ Question 02 _____
print("\n\t _______ Question 02 _______\n\n")

subjects = {"python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C"}

print("Total Number of classrooms for each subject:",len(subjects))



# _____ Question 03 _____
print("\n\t _______ Question 03 _______\n\n")

subject = {}

sub1 = int(input("Enter marks of Maths: "))
sub2 = int(input("Enter marks of Physics: "))
sub3 = int(input("Enter marks of Computer: "))

subject.update({"Maths" : sub1})
subject.update({"Physics" : sub2})
subject.update({"Computer" : sub3})

print(subject)
print("Maths:",subject["Maths"])
print("Physics:",subject["Physics"])
print("Computer:",subject["Computer"])

