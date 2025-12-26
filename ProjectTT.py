# Aman-Raj-6605766
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
number_of_students = 60 
class_subjects = ["Digital Marketing", "Financial Accounting", "Human Resources", "Microeconomics", "Business Ethics"]
maximum_score_per_subject = 100
maximum_score_for_CT = 30 

def determine_letter_grade(score):
    if score >= 90: return 'A+'
    elif score >= 80: return 'A'
    elif score >= 70: return 'B+'
    elif score >= 60: return 'B'
    elif score >= 50: return 'C'
    else: return 'F'
np.random.seed(42)

class_roster = {
    'Student Name': [f"Candidate_{i+101}" for i in range(number_of_students)],
    'Academic Term': ["MBA Semester 1"] * number_of_students,
    'Field of Study': ["Business Management"] * number_of_students,
}

subject_score_sheets = {}
for subject in class_subjects:
    low_bound = np.random.randint(35, 50) 
    subject_score_sheets[f'Score in {subject}'] = np.random.randint(low_bound, 101, size=number_of_students)

class_roster['CT Score (Received)'] = np.random.randint(15, 31, size=number_of_students)
class_roster['CT Score (Maximum)'] = [maximum_score_for_CT] * number_of_students

df = pd.DataFrame({**class_roster, **subject_score_sheets})

main_score_cols = [f'Score in {s}' for s in class_subjects]
df['Grand Total'] = df[main_score_cols].sum(axis=1) + df['CT Score (Received)']
total_possible = (len(class_subjects) * maximum_score_per_subject) + maximum_score_for_CT
df['Percentage'] = (df['Grand Total'] / total_possible) * 100

def calculate_spi(p):
    if p >= 90: return 10.0
    if p >= 80: return 9.0
    if p >= 70: return 8.0
    if p >= 60: return 7.0
    if p >= 50: return 6.0
    return 0.0

df['SPI'] = df['Percentage'].apply(calculate_spi)
plt.figure(figsize=(10, 6))
avg_scores = df[main_score_cols].mean().sort_values()
avg_scores.index = [i.replace('Score in ', '') for i in avg_scores.index]
avg_scores.plot(kind='barh', color=sns.color_palette('viridis', len(avg_scores)))
plt.title('Average Class Performance by Subject')
plt.xlabel('Average Score (out of 100)')
plt.savefig('average_subject_scores.png')
plt.figure(figsize=(8, 6))
sns.histplot(df['SPI'], bins=10, kde=True, color='teal')
plt.title('Distribution of Semester Performance Index (SPI)')
plt.savefig('spi_distribution.png')
df['Grade_DM'] = df['Score in Digital Marketing'].apply(determine_letter_grade)
grade_counts = df['Grade_DM'].value_counts().reindex(['A+', 'A', 'B+', 'B', 'C', 'F'], fill_value=0)
plt.figure(figsize=(8, 8))
plt.pie(grade_counts, labels=grade_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Grade Distribution: Digital Marketing')
plt.savefig('grade_distribution_marketing.png')

df.to_csv('student_performance_data.csv', index=False)
It is a performance  analyzer using numpy, pandas, matlplotlib .
