import numpy as np
import random as rn 

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

def curses_message(stdscr, message):
    stdscr.clear()
    stdscr.addstr(0, 0, message)
    stdscr.addstr(2, 0, "Press any key to continue...")
    stdscr.refresh()
    stdscr.getch()

def average_gpa(student):
    scores = np.array(list(student.marks.values()))
    if len(scores) == 0:
        student.gpa = 0
    else:
        student.gpa = np.mean(scores)

def partition(students, low, high):
    # pivot
    x = rn.randint(low, high)
    students[x], students[high] = (students[high], students[x])
    pivot = students[high].gpa
    i = low - 1

    for j in range(low, high):
        if students[j].gpa > pivot:
            i += 1
            students[i], students[j] = students[j], students[i]

    students[i + 1], students[high] = (students[high], students[i + 1])

    return i + 1

def sort_by_gpa(students, low, high):
    if low < high:
        x = partition(students, low, high)
        sort_by_gpa(students, low, x - 1)
        sort_by_gpa(students, x + 1, high)