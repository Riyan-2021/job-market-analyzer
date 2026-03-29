
import pandas as pd
import matplotlib.pyplot as plt

def analyze_jobs():
    df = pd.read_csv("data/sample_jobs.csv")

    # Count skills frequency
    skills_series = df['skills'].str.split(", ").explode()
    skill_counts = skills_series.value_counts()

    # Plot
    skill_counts.plot(kind='bar')
    plt.title("Top Skills Demand")
    plt.xlabel("Skills")
    plt.ylabel("Frequency")

    plt.savefig("outputs/skills_chart.png")
    print("Analysis completed!")

if __name__ == "__main__":
    analyze_jobs()
