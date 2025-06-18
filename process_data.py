import pandas as pd
import numpy as np
import random

random.seed(42)
np.random.seed(42)

genders = ['male', 'female']
educations = [
    "high school", "some high school", "associate's degree",
    "bachelor's degree", "master's degree", "some college"
]
ethnic_groups = ['group A', 'group B', 'group C', 'group D', 'group E']
lunch_types = ['standard', 'free/reduced']
test_preparation = ['completed', 'none']

def generate_data(n=200):
    data = []
    for _ in range(n):
        gender = random.choice(genders)
        education = random.choice(educations)
        ethnic = random.choice(ethnic_groups)
        lunch = random.choice(lunch_types)
        prep = random.choice(test_preparation)

        base = 70 if prep == 'completed' else 60
        math = np.clip(int(np.random.normal(base + 5, 10)), 40, 100)
        reading = np.clip(int(np.random.normal(base, 10)), 40, 100)
        writing = np.clip(int(np.random.normal(base - 2, 10)), 40, 100)

        data.append([gender, ethnic, education, lunch, prep, math, reading, writing])
    return pd.DataFrame(data, columns=[
        "gender", "race_ethnicity", "parental_education",
        "lunch_type", "test_preparation",
        "math_score", "reading_score", "writing_score"
    ])

# Save data
df = generate_data()
df["average_score"] = df[["math_score", "reading_score", "writing_score"]].mean(axis=1)
df.to_csv("students_cleaned_rich.csv", index=False)
print("✅ Dataset saved to students_cleaned_rich.csv")
