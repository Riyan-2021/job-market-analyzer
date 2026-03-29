import pandas as pd
from collections import Counter
from utils.skill_cleaner import clean_skills

def analyze_skills():
    df = pd.read_csv("data/jobs.csv")

    all_skills = []

    for skill_text in df["Skills"]:
        skills = clean_skills(skill_text)
        all_skills.extend(skills)

    counter = Counter(all_skills)

    skill_df = pd.DataFrame(
        counter.items(),
        columns=["Skill", "Frequency"]
    )

    skill_df = skill_df.sort_values(
        by="Frequency",
        ascending=False
    )

    return skill_df
