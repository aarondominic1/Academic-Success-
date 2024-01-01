# Importing Libraries 

import pandas as pd 
import matplotlib as plt 

#Reading the data file into project 
student_data = pd.read_csv("students.csv")
print(student_data)

#Hypothesis: The academic success of students is influenced by a combination of demographic, socio-economic, and educational factors.

#1) Previous Qualifications - Hypothesis: Students with a higher grade in their previous qualifications are more likely to succeed academically.

plt.figure(figsize=(10, 6))
student_data.groupby('Previous qualification (grade)')['Academic success'].mean().plot(kind='bar')
plt.title('Relationship between Previous Qualifications and Academic Success')
plt.xlabel('Previous Qualification Grade')
plt.ylabel('Average Academic Success')
plt.show()

