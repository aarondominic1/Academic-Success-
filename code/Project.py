
#Hypothesis: The academic success of students is influenced by a combination of demographic, socio-economic, and educational factors.

# Importing Libraries 
import pandas as pd 
import matplotlib.pyplot as plt 

#Reading the data file into project 
student_data = pd.read_csv("students.csv", sep = ";")

#Hypothesis: The academic success of students is influenced by a combination of demographic, socio-economic, and educational factors.

# 1) Parental Background - Analyzing the Influence of Father's Education on Student Outcomes
plt.figure(figsize=(20, 12))
parental_education_counts = student_data.groupby(['Father\'s qualification', 'Target']).size().unstack()
parental_education_counts.plot(kind='bar', stacked=True)
plt.title('Distribution of Academic Success based on Father\'s Education')
plt.xlabel('Father\'s Qualification')
plt.ylabel('Count')
plt.show()


# 2) Gender Differences 
plt.figure(figsize=(8, 6))
gender_counts = student_data.groupby(['Gender', 'Target']).size().unstack()
gender_counts.plot(kind='bar')
plt.title('Comparison of Academic Success between Genders')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.show()

# Unemployment Rate after enrollment, dropout or graduation
plt.figure(figsize=(10, 6))
student_data.boxplot(column='Unemployment rate', by='Target')
plt.title('Distribution of Academic Success based on Unemployment Rate')
plt.xlabel('Academic Success')
plt.ylabel('Unemployment Rate')
plt.show()