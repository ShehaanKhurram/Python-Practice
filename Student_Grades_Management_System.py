import csv

def avg():
    try:
        with open("student_record.csv", "r") as f:
            content = csv.reader(f)
            header = next(content)

            data = list(content)
            
            total = 0
            for i in data:
                total += float(i[1])
            avg = total / len(data)
            return avg
    except:
        print("File not found!")



def add_Record():
    header = ["Name", "Marks"]
    details = [header]

    num = int(input("Enter Number of Students: "))
    for i in range(1, num+1):
        name = (input(f"Enter name of student {i}: "))
        marks = float(input(f"Enter marks of student {i}: "))
        details.append([name, marks])

    with open("student_record.csv", "w", newline = "") as f:
        writer = csv.writer(f)
        writer.writerows(details)
        print("\nRecord saved in 'student_record' successfully!")

print ("\n  ________ Grade Calculator ________\n")
while True:
    print ("\t_____ Main Menu _____\n")
    print("1. Enter Record")
    print("2. View Results")
    print("0. Exit")
    choice = (input("Enter your choice: "))

    if choice == '1':
        add_Record()
    elif choice == '2':
        print("Average of Students:",avg())
    elif choice == '0':
        print("Good Bye!")
        break
    else:
        print("Invalid choice...")



