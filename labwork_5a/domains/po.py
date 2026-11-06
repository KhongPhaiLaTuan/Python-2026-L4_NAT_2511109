import pandas as pd 
import os

class Po:
    def __init__(self):
        self.students = None
    def load_csv(self, path):
        if os.path.exists(path):
            self.students = pd.read_csv(path)
    def query(self, condition):
        if self.students is None:
            return None
        try:
            result = self.students.query(condition)
            return result
        except Exception:
            return None
