# _____________________ Functions _____________________
print("\n\t __________ Functions __________\n\n")
def cal_sum(a, b):
    return a + b


sum = cal_sum(5,10)
print(sum)
 
# _____________________ Questions _____________________
# ________ Question 1 __________
# WAF to print length of a list


food = ["apple", "potato", "grapes", "confslour"]

def get_Length(food):
    return len(food)

length = get_Length(food)

print("Length of a list is:",length)


# ________ Question 2 __________
# WAF to print print elements of list in single line

def display_list(list1):
    print(list1)

display_list(food)

# ________ Question 3 __________
# WAF to find the factorial of n

def get_factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    print(fact)

get_factorial(5)

    
# ________ Question 4 __________
# WAF to convert dollar to pkr (current rate 1 dlr = 283.25 pkr)

def converter(dlr):
    pkr = dlr * 283.25
    print(dlr,"dollar =",pkr,"pkr") 

print()
converter(6)


# ________ Question 5 __________
# WAF to check if the given number n is even or odd

def check_status(n):
    if(n % 2 == 0):
        print(n,"is Even Number")
    else:
        print(n,"is Odd Number")


check_status(4)


# _____________________ Recursion _____________________
print("\n\t __________ Recursion __________\n\n")

# ________ Question 1 __________
# WAF to calculate first n natural numbers

def naturalNumbers(n):
    if(n == 0):
        return 0
    print(n)
    return naturalNumbers(n-1) + n

naturalNumbers(5)


# ________ Question 2 __________
# WAF to calculate the sum of first n natural numbers

def cal_sum(n):
    if n == 0:
        return 0
    return cal_sum(n-1) + n

s = cal_sum(5)
print("sum:", s)


# ________ Question 3 __________
# WAF to print all elements in the list (hint: use list and index as paremeter)


heroes = ["spiderman", "batman", "ironman", "thor", "superman"]

def print_list(list, index):
    if(index == len(list)):
        return
    print(list[index], end = " ")

    print_list(list, index+1)

print_list(heroes, 0)
print()


a = [1, 2]
print(a)
a = [1, 2] * 2
print(a)
a[1] = 3 
print(a)