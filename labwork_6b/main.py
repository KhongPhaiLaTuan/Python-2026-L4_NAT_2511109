import pandas as pd
import matplotlib.pyplot as plt
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
score_file = os.path.join(BASE_DIR, "scores.csv")
df = pd.read_csv(score_file)
def scatter():
    ax = df.plot.scatter(x="student_id", y="math", color="red", label="Math")
    df.plot.scatter(x="student_id", y="python", color="blue", label="Python", ax=ax)
    df.plot.scatter(x="student_id", y="python", color="green", label ="Db", ax=ax)
    plt.xlabel("Student_ID")
    plt.ylabel("Scores")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.savefig(os.path.join(BASE_DIR, "scattered.png"), dpi=300, bbox_inches="tight")
    plt.show()
def histogram():
    df[["python", "math", "database"]].plot.hist(subplots=True, layout=(1, 3), figsize=(12, 4), bins=10, edgecolor="black")
    plt.tight_layout()
    plt.savefig(os.path.join(BASE_DIR, "histo.png"), dpi=300)
    plt.show()
def box():
    df[["python", "math", "database"]].plot.box()
    plt.savefig(os.path.join(BASE_DIR, "box.png"), dpi=300)
    plt.show()

if __name__ == "__main__":
    scatter()
    histogram()
    box()
    

