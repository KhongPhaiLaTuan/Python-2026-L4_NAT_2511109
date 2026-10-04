import math
import numpy as np
import random as rn
import curses
import datetime 

#Helpers

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
    return str(n) + "th"

def curses_input(stdscr, prompt):
    curses.echo()
    stdscr.addstr(prompt)
    stdscr.refresh()
    value = stdscr.getstr().decode("utf-8").strip()
    curses.noecho()
    return value

def curses_message(stdscr, message):
    stdscr.clear()
    stdscr.addstr(0, 0, message)
    stdscr.addstr(2, 0, "Press any key to continue...")
    stdscr.refresh()
    stdscr.getch()

def get_date(stdscr, prompt):
    while True:
        value = curses_input(stdscr, prompt)
        try:
            datetime.datetime.strptime(value, "%d/%m")
            return value
        except ValueError:
            curses_message(stdscr, "Invalid date! Please enter in DD/MM format.")

def get_int(stdscr, prompt, minimum=None, maximum=None):
    while True:
        value = curses_input(stdscr, prompt)

        try:
            value = int(value)
        except ValueError:
            curses_message(stdscr, "Please enter a valid integer!")
            continue

        if minimum is not None and value < minimum:
            curses_message(stdscr, "The number is too small!")
            continue

        if maximum is not None and value > maximum:
            curses_message(stdscr, "The number is too large!")
            continue

        return value

def get_score(stdscr, prompt):
    while True:
        value = curses_input(stdscr, prompt)

        try:
            score = float(value)
        except ValueError:
            curses_message(stdscr, "Please enter a valid number!")
            continue

        if 0 <= score <= 20:
            return math.floor(score * 10) / 10

        curses_message(stdscr, "Score must be between 0 and 20!")

#Main

def new_course(stdscr, courses):
    option_num = get_int(stdscr, "\n Enter the number of courses that you want to enter: ", minimum=0)

    for i in range(option_num):
        while True:
            course_id = curses_input(stdscr, f"Enter the {ordinal(i)} course's ID: ")
            course_name = curses_input(stdscr, f"Enter the {ordinal(i)} course's name: ")

            if course_id and course_name:
                break

            curses_message(stdscr, "Please fill in all information!")

        courses.append({
            "ID": course_id,
            "Name": course_name
        })

    curses_message(stdscr, f"Successfully added {option_num} course(s).")

def list_courses(stdscr, courses):
    if not courses:
        curses_message(stdscr, "There are no courses.")
        return

    stdscr.clear()
    stdscr.addstr(0, 0, "========== COURSES ==========", curses.A_BOLD)

    for i, course in enumerate(courses, start=1):
        stdscr.addstr(i + 1, 0, f"{i}. ID: {course['ID']} | Name: {course['Name']}")

    stdscr.addstr(len(courses) + 3, 0, "Press any key to return...")
    stdscr.refresh()
    stdscr.getch()

def new_student(stdscr, students):
    option_num = get_int(stdscr, "\n Enter the number of students that you want to enter: ", minimum=0)

    for i in range(option_num):
        while True:
            student_id = curses_input(stdscr, f"Enter the {ordinal(i)} student's ID: ")
            name = curses_input(stdscr, f"Enter the {ordinal(i)} student's name: ")
            dob = get_date(stdscr, f"Enter the {ordinal(i)} student's date of birth: ")

            if student_id and name and dob:
                break

            curses_message(stdscr, "Please fill in all information!")

        students.append({
            "ID": student_id,
            "Name": name,
            "DOB": dob,
            "Marks": {}
        })

    curses_message(stdscr, f"Successfully added {option_num} student(s).")

def list_students(stdscr, students):
    if not students:
        curses_message(stdscr, "There are no students.")
        return

    stdscr.clear()
    stdscr.addstr(0, 0, "========== STUDENTS ==========", curses.A_BOLD)

    row = 2

    for index, student in enumerate(students, start=1):
        if row + 4 >= curses.LINES - 1:
            stdscr.addstr(curses.LINES - 1, 0, "Screen full. Press any key to continue...")
            stdscr.refresh()
            stdscr.getch()
            stdscr.clear()
            row = 0

        stdscr.addstr(row, 0, f"{index}.")
        stdscr.addstr(row + 1, 0, f"ID:   {student['ID']}")
        stdscr.addstr(row + 2, 0, f"Name: {student['Name']}")
        stdscr.addstr(row + 3, 0, f"DOB:  {student['DOB']}")

        if "GPA" in student:
            stdscr.addstr(row + 4, 0, f"GPA:  {student['GPA']:.2f}")
        else:
            stdscr.addstr(row + 4, 0, "GPA:  Not calculated")

        row += 6

    stdscr.addstr(min(row, curses.LINES - 1), 0, "Press any key to return...")
    stdscr.refresh()
    stdscr.getch()

def scores_input(stdscr, students, courses):
    if not students:
        curses_message(stdscr, "There are no students.")
        return

    if not courses:
        curses_message(stdscr, "There are no courses.")
        return

    course_num = len(courses)

    for student in students:
        ask = get_int(stdscr, f"\n Enter the number of courses that student {student['Name']} attends: ", minimum=1, maximum=course_num)
        for _ in range(ask):
            while True:
                course_name = curses_input(stdscr, "Enter the course's name: ")

                found_course = any(course_name == course["Name"] for course in courses)

                if not found_course:
                    curses_message(stdscr, "Course not found! Please try again.")
                    continue

                if course_name in student["Marks"]:
                    curses_message(stdscr, "Course already exists! " "Cannot change existing marks during creation.")
                    continue

                student["Marks"][course_name] = get_score(stdscr, f"Enter the {course_name}'s score: ")
                break

    curses_message(stdscr, "Scores entered successfully.")

def score_modify(stdscr, students, courses):
    if not students:
        curses_message(stdscr, "There are no students.")
        return

    if not courses:
        curses_message(stdscr, "There are no courses.")
        return

    while True:
        ask_name = curses_input(stdscr, "\n Enter the student's name or ID: ")
        student = next((candidate for candidate in students if ask_name == candidate["Name"] or ask_name == candidate["ID"]), None)
        if student is not None:
            break

        curses_message(stdscr, "Invalid student.")

    while True:
        ask_course = curses_input(stdscr, "Enter the course's name or ID that needs to be changed: ")

        course = next((candidate for candidate in courses if ask_course == candidate["Name"] or ask_course == candidate["ID"]), None)

        if course is None:
            curses_message(stdscr, "Course not found! Try again.")
            continue

        course_name = course["Name"]

        if course_name not in student["Marks"]:
            curses_message(stdscr, f"Student {student['Name']} does not attend " f"{course_name}.")
            continue
        break

    student["Marks"][course_name] = get_score(stdscr, f"Enter new {course_name} score for " f"student {student['Name']}: ")

    curses_message(stdscr, "Score modified successfully.")

def show_course_marks(stdscr, students, courses):
    if not courses:
        curses_message(stdscr, "There are no courses.")
        return

    while True:
        ask_course = curses_input(stdscr, "Enter the course's name or ID: ")
        course = next((candidate for candidate in courses if ask_course == candidate["Name"] or ask_course == candidate["ID"]), None)
        if course is not None:
            break
        curses_message(stdscr, "Course not found! Please try again.")

    course_name = course["Name"]

    stdscr.clear()
    stdscr.addstr(0, 0,f"========== {course_name.upper()} MARKS ==========", curses.A_BOLD)
    row = 2
    found_student = False

    for student in students:
        if course_name in student["Marks"]:
            found_student = True
            stdscr.addstr(row, 0,f"ID: {student['ID']} | " f"Name: {student['Name']} | " f"Mark: {student['Marks'][course_name]}")
            row += 1

    if not found_student:
        stdscr.addstr(row, 0, "No student attends this course.")

    stdscr.addstr(min(row + 2, curses.LINES - 1), 0, "Press any key to return...")
    stdscr.refresh()
    stdscr.getch()

def average_gpa(students):
    for student in students:
        scores = np.array(list(student["Marks"].values()))
        if len(scores) == 0:
            student["GPA"] = 0
        else:
            student["GPA"] = np.mean(scores)

def partition(students, low, high):
    # pivot
    x = rn.randint(low, high)
    students[x], students[high] = (students[high], students[x])
    pivot = students[high]["GPA"]
    i = low - 1

    for j in range(low, high):
        if students[j]["GPA"] > pivot:
            i += 1
            students[i], students[j] = students[j], students[i]

    students[i + 1], students[high] = (students[high], students[i + 1])

    return i + 1

def sort_by_gpa(students, low, high):
    if low < high:
        x = partition(students, low, high)
        sort_by_gpa(students, low, x - 1)
        sort_by_gpa(students, x + 1, high)

def sort_students_by_gpa(stdscr, students):
    if not students:
        curses_message(stdscr, "There are no students.")
        return

    average_gpa(students)
    sort_by_gpa(students, 0, len(students) - 1)
    curses_message(stdscr, "Students sorted by GPA (highest to lowest).")

# UI

def main_menu(stdscr, students, courses):
    curses.curs_set(0)

    options = [
        "Enter new courses",
        "Enter new students",
        "Enter scores for students",
        "Change a student's scores",
        "Show courses",
        "Show students",
        "Show student marks for a course",
        "Sort students by GPA",
        "Exit"
    ]

    selected = 0

    while True:
        stdscr.clear()

        stdscr.addstr(
            1, 5,
            "STUDENT MANAGEMENT SYSTEM",
            curses.A_BOLD
        )

        for index, option in enumerate(options):
            if index == selected:
                stdscr.addstr(
                    index + 3,
                    5,
                    "> " + option,
                    curses.A_REVERSE
                )
            else:
                stdscr.addstr(
                    index + 3,
                    5,
                    "  " + option
                )

        stdscr.addstr(
            len(options) + 5,
            5,
            "UP/DOWN: Navigate | ENTER: Select | Q: Quit"
        )

        stdscr.refresh()
        key = stdscr.getch()

        if key == curses.KEY_UP:
            selected -= 1

        elif key == curses.KEY_DOWN:
            selected += 1

        elif key in (curses.KEY_ENTER, 10, 13):
            if selected == 0:
                new_course(stdscr, courses)
            elif selected == 1:
                new_student(stdscr, students)
            elif selected == 2:
                scores_input(stdscr, students, courses)
            elif selected == 3:
                score_modify(stdscr, students, courses)
            elif selected == 4:
                list_courses(stdscr, courses)
            elif selected == 5:
                list_students(stdscr, students)
            elif selected == 6:
                show_course_marks(stdscr, students, courses)
            elif selected == 7:
                sort_students_by_gpa(stdscr, students)
            elif selected == 8:
                break

        elif key in (ord("q"), ord("Q")):
            break

        if selected < 0:
            selected = len(options) - 1
        elif selected >= len(options):
            selected = 0


# Program

student_list = []
course_list = []

curses.wrapper(main_menu, student_list, course_list)
