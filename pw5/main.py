from input import new_student, new_course, score_modify, scores_input
from output import list_students, list_courses, show_course_marks, sort_students_by_gpa
import curses

def main(stdscr):
    students = []
    courses = []
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

if __name__ == "__main__":
    curses.wrapper(main)