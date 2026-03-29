def clean_skills(skill_text):
    if not isinstance(skill_text, str):
        return []

    skill_text = skill_text.lower()
    skills = skill_text.split(",")
    skills = [s.strip() for s in skills]

    return skills
