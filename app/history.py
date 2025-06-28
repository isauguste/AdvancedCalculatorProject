import pandas as pd

class HistoryManager:
    def __init__(self):
        self.history = pd.DataFrame(columns=["num1", "num2", "operation", "result"])

    def add(self, num1, num2, operation, result):
        new_entry = {
            "num1": num1,
            "num2": num2,
            "operation": operation,
            "result": result
        }
        new_df = pd.DataFrame([new_entry])
        if self.history.empty:
            self.history = new_df
        else:
            self.history = pd.concat([self.history, new_df], ignore_index=True)

    def show(self):
        if self.history.empty:
            print("No history available.")
        else:
            print(self.history)

    def clear(self):
        self.history = pd.DataFrame(columns=["num1", "num2", "operation", "result"])

    def save(self, filename="history.csv"):
        self.history.to_csv(filename, index=False)

    def load(self, filename="history.csv"):
        try:
            self.history = pd.read_csv(filename)

        except FileNotFoundError:
            print(f"File {filename} not found.")

    def empty(self):
        return self.history.empty
