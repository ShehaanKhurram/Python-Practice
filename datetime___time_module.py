# ____________________ datetime module ____________________
"""
import datetime
from datetime import datetime

#1. Gettig current date and time
now = datetime.now()
print(now)

#2. Getting current date
date_today = datetime.today().date()
print(date_today)

#3. Getting current time
current_time = datetime.now().time()
print(current_time)

# __________ Accessing Components __________

print(now.year) #year
print(now.month) #month
print(now.day) #day
print(now.hour) #hour
print(now.minute) #minutes
print(now.second) #seconds

# __________ Formatting dates (strftime) __________

# %Y or %y = year
# %m = month
# %d = day
# %H = hour (24-hour format)
# %I = hour (12-hour format)
# %M = month
# %S = second
# %p = AM/PM

formatted = now.strftime("%Y-%m-%d %H:%M:%S %p")
print(formatted)


# __________ Parsing strings into dates(strptime) __________
date = "2025-07-09 12:10"
dt = datetime.strptime(date, "%Y-%m-%d %H:%M")
print(dt)


# __________ Date Arithmetic__________
from datetime import timedelta

future = now + timedelta(days = 5)
past = now - timedelta(hours = 2)

print(future)
print(past)
"""

# ____________________ time module ____________________
"""
import time

#1. Epoch time: Current time in seconds
epoch_time = time.time() 
print(epoch_time)

#2. Convert Epoch time into readable time.
readable_time = time.ctime(epoch_time)
print(readable_time)

#3. Delay execution -> time.sleep(seconds)
print("start")
time.sleep(1) #delay of 2 seconds before printing next statement i.e stop.
print("stop")

#4. structured time
t = time.localtime()
print(t)

#5. formatted time like datetime
formatted = time.strftime("%Y-%m-%d %H:%M:%S", t)
print(formatted)
"""

# ____________________ Question 01 ____________________
# Find the execution time of a program. Next 2 seconds after execution
"""
import time
from datetime import datetime

start = time.time()  # Start timers
print("Start:",start)

print("Current date:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
time.sleep(2)  # Wait 2 seconds

end = time.time()  # End timer
print("End:",end)
print(f"Execution time: {end - start} seconds")
"""

# ____________________ Question 02 ____________________
#Asks the user to enter their date of birth in the format YYYY-MM-DD.
#Calculates and prints their current age in years.
#Waits for 3 seconds (using time.sleep).
#Displays the exact date & time they will turn 100 years old.

import time
from datetime import datetime

userInput = str(input("Enter your Date of Birth(YYYY-MM-DD): "))

dob = datetime.strptime(userInput, "%Y-%m-%d").date()


current_date = datetime.today().date()
print("Today's Date:",current_date)

age_year = current_date.year - dob.year

if(current_date.month,current_date.day) < (dob.month,dob.day):
    age_year -= 1

print("Your current age:",age_year)

time.sleep(3)

hundered_years_date = dob.replace(year = dob.year + 100)
print("You will turn 100 years old on:",hundered_years_date)



