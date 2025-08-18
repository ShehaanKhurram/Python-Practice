# ________ Math built-in  ________
# Always returns answer in float
"""
import math
# ________ Commonly Used Functions ________

# 1. math.ceil(x) -> return increasing round figure value.
print(math.ceil(4.5)) #5

# 2. math.floor(x) -> returns decreasing round figure value.
print(math.floor(4.5)) #4

# 3. math.pow(x, y) -> returns x^y in float.
print(math.pow(2,3)) #8.0

# 4. math.sqrt(x) -> returns square root of x in float.
print(math.sqrt(16)) #4.0

# 5. math.isqrt(x) -> returns square root of x in int.
print(math.isqrt(16)) #4

# 6. math.factorial(x) -> returns factorial of x
print(math.factorial(5)) #120

# 7. math.trunc(x) -> truncate/remove decimal part of x.
print(math.trunc(2.5)) #2

# ________ Trignometric Functions ________  

# 1. math.sin(x)
print(math.sin(90))
print(math.sin(math.pi / 2))  #pi = 180 -> 180 / 2 = 90 -> output = 1.0 

# 2. math.cos(x) 
print(math.cos(0)) #1.0
print(int(math.cos(0))) #1.0

# 3. math.tan()
print(math.tan(math.pi / 4)) # 1.0

# 4. math.degrees(x) -> convert radian into degree
print(math.degrees(1)) #57

# 5. math.radians(x) -> convert dergees into radians
print(math.radians(57)) #1.0
"""
#_______________________________________________________________

# ________ Random built-in ________
"""
import random
#1. random.random()
print(random.random()) # returns random float number between 0 and 1

#2. random.randint(a, b)
print(random.randint(1,10)) # random int number between 1 and 10

#3. random.randrange(a, b, c)
print(random.randrange(0,20,2)) #return random number from a range.

#4. random.uniform(a, b)
print(random.uniform(1, 10)) # random float number between 1 and 10

#5. random.choice(list)
list = ["apple", "banana", "Mango"]
print(random.choice(list)) #choose random from a sequence

#6. random.choices(list, k = ?)
list1 = [1,2,3,4,5]
print(random.choices(list1, k = 4)) #allow repeated values

#7. random.sample(list, k = ?)
print(random.sample(list1, k = 4)) #no repitition of values

#8. random.shuffle(list)
deck = [1,2,3,4,5,6,7,8,9,10]
random.shuffle(deck) # Shuffle a sequence
print(deck)
print("Hi")

"""
