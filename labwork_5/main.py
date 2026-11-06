import pandas as pd
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def ex1():
    students_file = os.path.join(BASE_DIR, "students.csv")
    df = pd.read_csv(students_file)
    print(f"First 5 rows of the dataset: \n{df.head()} \n")
    rows, columns = df.shape
    print(f"The dataset students.csv has {rows} rows and {columns} columns\n")
    print(f"Name and GPA of students: \n{df[["name", "GPA"]]}\n")
    print(f"Students with GPA higher than 3.5: \n {df[df["GPA"] > 3.5]}\n")
    print(f"Students who study ICT and has GPA higher than 3.5: \n{df[(df["GPA"] > 3.5) & (df["major"] == "ICT")]}\n")

def ex2():
    students_file = os.path.join(BASE_DIR, "students.csv")
    scores_file = os.path.join(BASE_DIR, "scores.csv")
    df1 = pd.read_csv(students_file)
    df2 = pd.read_csv(scores_file)
    print(f"Missing values in dataset students.csv: \n{df1.isna().sum()}\n")
    print(f"Missing values in dataset scores.csv: \n {df2.isna().sum()} \n")
    print(f"Deteleting missing values in dataset students.csv...")
    print(f"New dataset student.csv: \n{df1.dropna()}\n")
    print(f"Replacing missing values in dataset scores.csv with 0...\n")
    print(f"New dataset scores.csv: \n{df1.fillna(0)}\n")
    print(f"Merging two datasets together...\n")
    df = pd.merge(df1, df2, on="student_id")
    print(f"Done! New dataset:\n {df}\n")
    print(f"Top 5 students: \n{df.sort_values("GPA", ascending= False).head()}\n")
    print(f"Average score by major: \n{df.groupby("major")["GPA"].mean()}\n")
if __name__ == "__main__":
    ex2()