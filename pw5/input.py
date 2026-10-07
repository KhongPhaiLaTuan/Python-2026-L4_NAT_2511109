import math
import curses
import datetime 
from helper import ordinal, curses_message, average_gpa
from domains import Student, Course

def curses_input(stdscr, prompt):
    curses.echo()
    stdscr.addstr(prompt)
    stdscr.refresh()
    value = stdscr.getstr().decode("utf-8").strip()
    curses.noecho()
    return value

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

def new_course(stdscr, courses):
    option_num = get_int(stdscr, "\n Enter the number of courses that you want to enter: ", minimum=0)
    f = open("courses.txt", "a+")
    for i in range(option_num):
        while True:
            course_id = curses_input(stdscr, f"Enter the {ordinal(i)} course's ID: ").upper()
            course_name = curses_input(stdscr, f"Enter the {ordinal(i)} course's name: ").lower().title()

            if course_id and course_name:
                break

            curses_message(stdscr, "Please fill in all information!")
        f.write(f"\n#{i+1} \nCourse name: {course_name} \nID: {course_id}\n ")
        courses.append(Course(course_id, course_name))
    f.close()
    curses_message(stdscr, f"Successfully added {option_num} course(s).")

def new_student(stdscr, students):
    option_num = get_int(stdscr, "\n Enter the number of students that you want to enter: ", minimum=0)
    f = open("students.txt", "a+")
    for i in range(option_num):
        while True:
            student_id = curses_input(stdscr, f"Enter the {ordinal(i)} student's ID: ").upper()
            name = curses_input(stdscr, f"Enter the {ordinal(i)} student's name: ").lower().title()
            dob = get_date(stdscr, f"Enter the {ordinal(i)} student's date of birth: ")

            if student_id and name and dob:
                break

            curses_message(stdscr, "Please fill in all information!")
        f.write(f"\n#{i+1} \nName: {name} \nDate of birth: {dob} \nID: {student_id}\n")
        students.append(Student(student_id, name, dob))
    f.close()
    curses_message(stdscr, f"Successfully added {option_num} student(s).")

def scores_input(stdscr, students, courses):
    if not students:
        curses_message(stdscr, "There are no students.")
        return

    if not courses:
        curses_message(stdscr, "There are no courses.")
        return

    course_num = len(courses)
    f = open("marks", "a+")
    for student in students:
        f.write(f"\n#{students.index(student) + 1} \nName: {student.name} \nID: {student.id}")
        ask = get_int(stdscr, f"\n Enter the number of courses that student {student.name} attends: ", minimum=1, maximum=course_num)
        for i in range(ask):
            while True:
                course_name = curses_input(stdscr, "Enter the course's name: ").lower().title()

                found_course = next((course for course in courses if course_name == course.name or course_name == course.id),None)

                if not found_course:
                    curses_message(stdscr, "Course not found! Please try again.")
                    continue

                if course_name in student.marks:
                    curses_message(stdscr, "Course already exists! " "Cannot change existing marks during creation.")
                    continue
                course_name = found_course.name
                student.marks[course_name] = get_score(stdscr, f"Enter the {course_name}'s score: ")
                f.write(f"\n{course_name}: {student.marks[course_name]}")
                average_gpa(student)
                break
        f.write(f"\n")
    f.close()
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
        student = next((candidate for candidate in students if ask_name.lower().title() == candidate.name or ask_name.upper() == candidate.id), None)
        if student is not None:
            break

        curses_message(stdscr, "Invalid student.")

    while True:
        ask_course = curses_input(stdscr, "Enter the course's name or ID that needs to be changed: ")

        course = next((candidate for candidate in courses if ask_course.lower().title() == candidate.name or ask_course.upper() == candidate.id), None)

        if course is None:
            curses_message(stdscr, "Course not found! Try again.")
            continue

        course_name = course.name

        if course_name not in student.marks:
            curses_message(stdscr, f"Student {student.name} does not attend " f"{course_name}.")
            continue
        break

    student.marks[course_name] = get_score(stdscr, f"Enter new {course_name} score for " f"student {student.name}: ")

    curses_message(stdscr, "Score modified successfully.")


