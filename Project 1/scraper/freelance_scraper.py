import pandas as pd

def scrape_freelance():
    jobs = [
        {
            "Title": "Freelance Python Developer",
            "Company": "Upwork Client",
            "Location": "Remote",
            "Skills": "Python, API, Flask",
            "Salary": "50000"
        },
        {
            "Title": "Web Developer",
            "Company": "Freelancer Client",
            "Location": "Remote",
            "Skills": "HTML, CSS, JavaScript",
            "Salary": "45000"
        }
    ]
    return pd.DataFrame(jobs)
