# ___________ While Loops ___________
# ___________ Question 01 ___________
# print 1 to 100
"""i = 0
while i <= 100:
    print(i)
    i += 1"""

# ___________ Question 02 ___________
# 100 to 1
"""i = 100
while i >= 1:
    print(i)
    i -= 1"""

# ___________ Question 03 ___________
# print given list
"""arr = [1,4,9,16,25,36,49,64,81,100] # list
i = 0
while i < len(arr):
    print(arr[i])
    i += 1"""

# ___________ Question 04 ___________
# Search a number from 
"""arr = (1,4,9,16,25,36,49,64,81,100) #tuple
i = 0
n = 36
while i < len(arr):
    if(n == arr[i]):
        print("Found at index:", i)
    i += 1"""


# break and continue statement



# ___________ For Loops ___________
#1
"""arr = [1,4,9,16,25,36,49,64,81,100] # list

for i in arr:
    print(i)"""

#2
"""arr = (1,4,9,16,25,36,49,64,81,100) #tuple
for i in arr:
    print(i)"""

#3
"""str = "shehaan"
for i in str:
    print(i)"""

# ___________ For Loops with else ___________
# else in for loop works as break

str = "shehaan"

for i in str:
    print(i)
else:   
    print("end")