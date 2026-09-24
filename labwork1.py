#ex 1
print("Exercise 1")
while True:
    try:
        ex1 = float(input("Enter circle radius: "))
        break
    except ValueError:
        print("Enter a valid number!")
def circle_area(radius):
    area = 3.14 * radius**2
    print(f"Circle area: {area}\n")
circle_area(ex1)

#ex 2
print("Exercise 2")
while True:
    try:
        ex2 = float(input("Enter the temperature in Celsius: "))
        break
    except ValueError:
        print("Enter a valid number!")
def f_to_c(c):
    f = c*1.8 + 32
    print( f"{c} (C) = {f} F\n" )
f_to_c(ex2)


#ex 3
import math
print("Exercise 3")
while True:
    try:
        ex3 = int(input("Enter a number: "))
        break
    except ValueError:
        print("Enter a valid number!")
def prime_number_check(n):
    if n <= 1:
        print(f"{n} is NOT a prime number\n")
    else:
        for i in range(2, math.isqrt(n) +1):
            if n%i == 0:
                print(f"{n} is NOT a prime number\n")
            else:
                print(f"{n} is a prime number\n")
prime_number_check(ex3)

#ex4
print("Exercise 4")
while True:
    try:
        ex4 = int(input("Enter a number: "))
        break
    except ValueError:
        print("Enter a valid number!")
def perfect_number_check(n):
    if n <= 1:
        print(n, "is not a perfect number\n")
    else:
        s = 1
        for i in range(2, math.isqrt(n) +1):
            if n%i==0:
                s+=i
                if i != n//i:
                    s += n//i
        if s == n:
            print(n, "is a perfect number\n")
        else:
            print(n, "is not a perfect number\n")
perfect_number_check(ex4)

#ex5
print("Exercise 5")
ex5 = input("What is your favorite color: ").lower()
def color_check(color):
    check_list = ["white", "gray", "cyan", "blue"]
    for i in check_list:
        if color == i:
            print(f"Your color is at index {check_list.index(i) + 1} in my list\n")
            break
    else:
        print("Sorry, I could not find your color\n")
color_check(ex5)

#ex6
print("Exercise 6")
print("range1:", *range(7))
print("range2:", *range(1, 11, 3))
print("range3:", *range(5, 0, -1))
print("range4:", *range(6, -3, -2))

#ex7
print("\n Exercise 7")
while True:
    ex7 = str(input("Enter a text with the $ sign: "))
    a = False
    for i in ex7:
        if i == "$":
            a = True
    if a == True:
        break
    else:
        print("please enter a string with the $ sign")
def dollar_remover(s):
    new_s = s.replace("$", "")
    print(new_s, "\n")
dollar_remover(ex7)


#ex8
print("Exercise 8")
def even_sort(l):
    list_sort = l.split()
    new_list = []
    for i in list_sort:
        try:
            x = int(i)
            if x%2 == 0:
                new_list.append(x)
        except ValueError:
            continue
    print(new_list, "\n")
while True:
    ex8 = input("Enter the list of numbers seperated by a space: ")
    if not ex8:
        print("Please enter the list of numbers seperated by a space: ")
        continue

    else:
        break
even_sort(ex8)

#ex9
print("Exercise 9")
def factorial(n):
    a = 1
    for i in range(1, n+1):
        a = i*a
    print("The factorial of", n ,"is:", a, "\n")

while True:
    try:
        ex9 = int(input("Enter a non negative integer: "))
        if ex9 < 0:
            print("Please enter a non-negative integer!")
        else:
            break
    except ValueError:
        print("Please enter a valid integer!")
factorial(ex9)

# %%
#ex10
print("Exercise 10")
while True:
    try:
        ex10 = int(input("Enter an integer: "))
        break
    except ValueError:
        print("Please enter a valid integer!")

def all_divisors(n):
    divisor_list = []
    for i in range(1, math.isqrt(abs(n)) + 1):
        if n%i==0:
            divisor_list.append(i)
            if i != n//i:
                divisor_list.append(n//i)
    print(n, "Divisors list is: ", divisor_list, "\n")

all_divisors(ex10)

#ex11
import math
while True:
    ex11a = input("Enter 2 position of point A (seperate by a space): ")
    ex11b = input("Enter 2 position of point B (seperate by a space): ")
    if not ex11a or not ex11b:
        print("Please enter again!")
        continue
    else:
        ex11a_list = ex11a.split()
        ex11b_list = ex11b.split()
        if len(ex11a_list) != 2 or len(ex11b_list) != 2:
            print("Please enter again!")
            continue
        else:
            try:
                a_list = []
                b_list = []
                for i in range(2):
                    a_list.append(int(ex11a_list[i]))
                    b_list.append(int(ex11b_list[i]))
                break
            except ValueError:
                print("Please enter again!")
                continue
print(f"The distance between point A and B is {math.dist(a_list, b_list)} \n")

#ex12
print("Exercise 12")
def hollow_rectangle(m, n):
    for i in range(m):
        for j in range(n):
            if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

while True:
    try:
        ex12 = input("Enter the length of m and n seperate by a space").split()
        if not ex12:
            print("Enter again!")
            continue
        m = int(ex12[0])
        n = int(ex12[1])
        break
    except ValueError:
        print("Enter again!")
hollow_rectangle(m, n)


