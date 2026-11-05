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

