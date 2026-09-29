
def ordinal(i):
    n = i + 1
    if n % 100 in [11, 12, 13]:
        return str(n) + "th"
    elif n % 10 == 1:
        return str(n) + "st"
    elif n % 10 == 2:
        return str(n) + "nd"
    elif n % 10 == 3:
        return str(n) + "rd"
    else:
        return str(n) + "th"

def scores_input(students, courses, course_num):
    for i in students:
        while True:
            try:
                ask = int(input(f"Enter the number of courses that student {i['Name']} attend: "))
                if ask <= 0 or ask > course_num :
                    print("Enter a valid number!")
                    continue
                else:
                    break
            except ValueError:
                print("Enter a valid number!")
                continue
        for x in range(ask):
            i["Mark"]["Name"] = input("Enter the course's name: ")

student_list = []
course_list = []

option = input(f"Choose an option:\n 1. Enter new courses \n 2. Enter new students \n 3. Show current class \n 4. Show current score")
match option:
    case 1:
        while True:
            try:
                option_num = int(input("Enter the number of courses that you want to enter:"))
                break
            except ValueError or option_num <= 0:
                print("Enter a valid number of options!")
        for i in range(option_num):
            courses = {}
            while True:
                courses["ID"] = input(f"Enter the {ordinal(i)} course's ID: ")
                courses["Name"] = input(f"Enter the {ordinal(i)} course's name: ")
                if not courses["ID"] or not courses["Name"]:
                    print("Please fill in all information")
                    continue
                else:
                    break
            course_list.append(courses)
    case 2:
        while True:
            try:
                option_num = int(input("Enter the number of courses that you want to enter:"))
                break
            except ValueError or option_num <= 0:
                print("Enter a valid number of options!")
        for i in range(student_num):
            students = {}
            while True:
                students["ID"] = input(f"Enter the {ordinal(i)} student's ID: ")
                students["Name"] = input(f"Enter the {ordinal(i)} student's name: ")
                students["DOB"] = input(f"Enter the {ordinal(i)} student's date of birth: ")
                students["Marks"] = {}
                if not students["ID"] or not students["Name"] or not students["DOB"]:
                    print("Please fill in all information")
                    continue
                else:
                    break
            student_list.append(students)
            print(student_list)

