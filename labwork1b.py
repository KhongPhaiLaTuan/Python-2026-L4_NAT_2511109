
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

def option_check(n):
    while True:
        try:
            n = int(n)
            if n >= 0:
                return n
            print("Enter a valid number of options!")
        except ValueError:
            print("Enter a valid number of options!")

def new_course(list):
        option_num = int(input("Enter the number of courses that you want to enter:"))
        option_check(option_num)
        for i in range(option_num):
            courses = {}
            while True:
                courses["ID"] = input(f"Enter the {ordinal(i)} course's ID: ")
                courses["Name"] = input(f"Enter the {ordinal(i)} course's name: ")
                if courses["ID"] and courses["Name"]:
                    break
                print("Please fill in all information")
            list.append(courses)

def new_student(list):
        option_num = int(input("Enter the number of students that you want to enter:"))
        option_check(option_num)
        for i in range(option_num):
            students = {}
            while True:
                students["ID"] = input(f"Enter the {ordinal(i)} student's ID: ")
                students["Name"] = input(f"Enter the {ordinal(i)} student's name: ")
                students["DOB"] = input(f"Enter the {ordinal(i)} student's date of birth: ")
                students["Marks"] = {}
                if students["ID"] and students["Name"] and students["DOB"]:
                    break
                print("Please fill in all information")
            list.append(students)

def scores_input(students, courses):
    course_num = len(courses)
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
            while True:
                course_name = input("Enter the course's name: ")
                check = False
                for a in courses:
                    if course_name == a["Name"]:
                        check = True
                if course_name in i["Marks"]:
                    print("Course already exists! Can not change existed marks during creation!")
                    check = False
                if check == True:
                    while True:
                        try:
                            score = float(input(f"Enter the {course_name}'s score of this student"))
                            if score >= 0 and score <= 20:
                                break
                            print("Enter a valid number!")
                        except ValueError:
                            print("Enter a valid number!")
                    i["Marks"][course_name] = score
                    break
                continue

def score_modify(students, courses):
    while True:
        ask_name = input("Enter the student's name or id: ")
        student_check = False
        for i in students:
            if ask_name == i["Name"] or ask_name == i["ID"]:
                student_check = True
                break
            else:
                continue
        if student_check:
            break
        print("Invalid student")
    while True:
        ask_course = input("Enter the course's name or id that scores need to be changed: ")
        check_course = False
        for x in courses:
            if ask_course == x['Name'] or ask_course == x["ID"]:
                check_course = True
                break
            else:
                continue
        if not check_course:
            print("Course not found! Try again!")
            continue
        if x["Name"] not in i["Marks"]:
            print(f"Student {i["Name"]} does not attend in {x["Name"]} course")
            continue
        break
    while True:
        try:
            new_score = float(input(f"Enter new {x["Name"]} for student {i["Name"]}"))
            if 0 <= new_score <= 20:
                break
            print("Invalid score!")
        except ValueError:
            print("Invalid score!")
        i["Marks"][x["Name"]] = new_score
        
student_list = []
course_list = []

option = int(input(f"Choose an option:\n 1. Enter new courses \n 2. Enter new students \n 3. Enter scores for students \n 4. Chage a student's scores \n 5. Show courses \n 6. Show students and scores \nInput: "))
match option:
    case 1:
        new_course(course_list)
    case 2:
        new_student(student_list)
    case 3:
        scores_input(student_list, course_list)
    case 4:
        score_modify(student_list, course_list)
    case 5:
        print(course_list)
    case 6:
        print(student_list)
