# Read the CSV file
import pandas as pd
df = pd.read_csv('student.csv')

# Find the total number of students
total_students = len(df)

# Find the maximum and minimum marks
max_marks = df['mark'].max()
min_marks = df['mark'].min()

# Display the results
print(df)
print("Total number of students:", total_students)
print("Maximum marks:", max_marks)
print("Minimum marks:", min_marks)
