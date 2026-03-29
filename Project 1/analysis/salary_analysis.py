import pandas as pd

def analyze_salary():
    df = pd.read_csv("data/jobs.csv")

    df["Salary"] = pd.to_numeric(
        df["Salary"],
        errors="coerce"
    )

    avg_salary = df["Salary"].mean()

    salary_by_location = df.groupby(
        "Location"
    )["Salary"].mean()

    return avg_salary, salary_by_location
