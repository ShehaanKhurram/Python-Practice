
import os

# __________________ Make new folder __________________
"""
if not os.path.exists("data"):
    os.mkdir("data")
"""

#os.makedirs("data/test/day1")

# __________________ Remove Directories __________________
#os.rmdir("data/test/day1")


# __________________ Make 100 folders in data folder __________________
"""
for i in range(100):
    os.mkdir(f"data/day{i+1}") #make 100 folders in data folders
 """

 # __________________ Rename folder __________________
""" 
# Rename folder
for i in range(100):
    os.rename(f"data/day {i+1}", f"data/part {i+1}") #rename day1 to part 1
"""

# __________________ List Files and folders __________________
# check how many folders are in data folder
# first store all folders in a list using os.listdir("data")
# check length
"""
folders = os.listdir("data")    # pack all folders in a list    

print(type(folders))
print(len(folders))
print(folders)
"""

#current = os.listdir()
#print(current)


# __________________ Get Current Directory __________________
#print(os.getcwd())

# __________________ Change Directory __________________

#os.chdir("E:/Shehaan/BSCS")
#print(os.getcwd())

# __________________ Delete Files __________________

#if os.path.exists("students.txt"):
    #os.remove("students.txt")

# __________________ Check directory or file __________________
#print(os.path.isdir("data/test"))
#print(os.path.isfile("students.txt"))


#extras
#os.system("echo Hello World Hi")
#print(os.name)

#print(os.path.abspath("filee.txt"))
