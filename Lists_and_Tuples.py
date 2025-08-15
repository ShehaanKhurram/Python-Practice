# ___________________________ Lists ___________________________
'''
Strings are immutable(can't change or modify)
but lists are arrays and mutable(can be changed)
'''
print("\n\t ______ Lists ______\n\n")
marks = [1,2,3,4,5]
print(marks)
print(type(marks))

#we can store data with different datatypes

student = ["shehaan", 20, "phase 8", 92];
print(student)

#_______ List Slicing (sub list)_______
# same syntax as string

print(marks[1:4])
print(marks[-3:-1])

#________ List Methods ________

list = [3,1,2]
list.append(4) #add 4 at last
list.sort() # sort in ascending order
list.sort(reverse = True) # sort in descending order
print(list)

list.reverse()
print(list)

list.insert(3, 6) #list.insert(index, element)
print(list)

list.remove(6) # remove element 6
print(list)

list.pop(3) #remove element on 3rd index
print(list)


# ___________________________ Tuples ___________________________
# use round brackets ()

print("\n\t ______ Tuples ______\n\n")
tup = (9,8,7, 7)
print(tup)

#______SLicing______
# Tuple slicing same as string and lists


#______Tuples methods______

print(tup.index(8)) #find index of specific element e.g: 8

print(tup.count(7)) #number of occurances



# _______________ Questions_______________

print("\n\t ______ Questions ______\n\n")
print("\n\t ______ Question 1 ______\n\n")

movies = []
name1 = str(input("Enter first name: "))
name2 = str(input("Enter second name: "))
name3 = str(input("Enter third name: "))

movies.append(name1)
movies.append(name2)
movies.append(name3)

print("Your Favorite Movies:", movies)

print("\n\t ______ Question 2 ______\n\n")
print("Check palindrome:\n")

list1 = [1,2,1]

copy_list1= list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("Palindrome list!")
else:
    print("Not a Palindrome list!")



print("\n\t ______ Question 3 ______\n\n")

tuple = ("C", "D", "A", "A", "B", "B", "A")
print(tuple)

print("Number of students with A grade:",tuple.count("A"))


grades = []
grades.append(tuple[0])
grades.append(tuple[2])
grades.append(tuple[3])
grades.append(tuple[4])
grades.append(tuple[5])
grades.append(tuple[6])
grades.sort()
print("Grades List:",grades)