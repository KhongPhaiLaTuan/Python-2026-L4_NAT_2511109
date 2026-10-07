import curses
from helper import curses_message, sort_by_gpa
from input import curses_input
from domains import Course, Student
def list_courses(stdscr, courses):
    if not courses:
        curses_message(stdscr, "There are no courses.")
        return

    stdscr.clear()
    stdscr.addstr(0, 0, "========== COURSES ==========", curses.A_BOLD)

    for i, course in enumerate(courses, start=1):
        stdscr.addstr(i + 1, 0, f"{i}. ID: {course.id} | Name: {course.name}")

    stdscr.addstr(len(courses) + 3, 0, "Press any key to return...")
    stdscr.refresh()
    stdscr.getch()
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
        stdscr.addstr(row + 1, 0, f"ID:   {student.id}")
        stdscr.addstr(row + 2, 0, f"Name: {student.name}")
        stdscr.addstr(row + 3, 0, f"DOB:  {student.dob}")

        stdscr.addstr(row + 4, 0, f"GPA:  {student.gpa:.2f}")

        row += 6

    stdscr.addstr(min(row, curses.LINES - 1), 0, "Press any key to return...")
    stdscr.refresh()
    stdscr.getch()
def show_course_marks(stdscr, students, courses):
    if not courses:
        curses_message(stdscr, "There are no courses.")
        return

    while True:
        ask_course = curses_input(stdscr, "Enter the course's name or ID: ")
        course = next((candidate for candidate in courses if ask_course == candidate.name or ask_course == candidate.id), None)
        if course is not None:
            break
        curses_message(stdscr, "Course not found! Please try again.")

    course_name = course.name

    stdscr.clear()
    stdscr.addstr(0, 0,f"========== {course_name.upper()} MARKS ==========", curses.A_BOLD)
    row = 2
    found_student = False

    for student in students:
        if course_name in student.marks:
            found_student = True
            stdscr.addstr(row, 0,f"ID: {student.id} | " f"Name: {student.name} | " f"Mark: {student.marks[course_name]}")
            row += 1

    if not found_student:
        stdscr.addstr(row, 0, "No student attends this course.")

    row = min(row + 2, curses.LINES - 2)
    stdscr.addstr(row, 0, "Press any key to return...")
    stdscr.refresh()
    stdscr.getch()

def sort_students_by_gpa(stdscr, students):
    if not students:
        curses_message(stdscr, "There are no students.")
        return
    sort_by_gpa(students, 0, len(students) - 1)
    curses_message(stdscr, "Students sorted by GPA (highest to lowest).")