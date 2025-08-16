import csv
# ________________________ List Methods ________________________
# ____________ Read CSV File ____________
# csv.reader(file)

"""
file = r"record.csv"
with open(file,"r") as csv_file:
    content = csv.reader(csv_file, delimiter = ',') #default delimeters are ","
    header = next(content) # header is seperately saved i.e [Name,Age,Email]
    print(content) #content is just an object.

    list1 = list(content) #converting content object into list.
    print(type(list1))

    for row in list1:
        print(row)
"""

# ____________ Write CSV File ____________
#csv.writer

"""with open("data.csv", "w", newline = "") as f:
    writer = csv.writer(f, delimiter = ',')
    writer.writerows(list1)
    print("\n'data.csv' file is successfully created!")
"""

# ________________________ Dictionary Methods ________________________
# ____________ Read CSV File ____________
#csv.DictReader

data = []
with open("record.csv") as f:
    content = csv.DictReader(f)
    
    for row in content:
        data.append(dict(row))

    print(data)

# ____________ Write CSV File ____________
#csv.DictWriter

with open("dict_record.csv", "w", newline = "") as f:
    header = ["Name", "Age", "Email"]
    writer = csv.DictWriter(f, fieldnames = header)
    writer.writeheader()
    writer.writerows(data)
    print("\n'dict_record.csv' file is successfully created!")
