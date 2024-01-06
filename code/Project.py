
#Hypothesis: The academic success of students is influenced by a combination of demographic, socio-economic, and educational factors.

# Importing Libraries 
import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 
import seaborn as sns 

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

# Marital Status
plt.figure(figsize=(8, 6))
marital_status_counts = student_data.groupby(['Marital status', 'Target']).size().unstack()
marital_status_counts.plot(kind='bar', stacked=True)
plt.title('Distribution of Academic Success based on Marital Status')
plt.xlabel('Marital Status')
plt.ylabel('Count')
plt.show()


# Inflation Rate
plt.figure(figsize=(10, 6))
student_data.boxplot(column='Inflation rate', by='Target')
plt.title('Distribution of Academic Success based on Inflation Rate')
plt.xlabel('Academic Success')
plt.ylabel('Inflation Rate')
plt.show()

#Scatter Plot - Age at enrollment vs Admission Grade 
sample_size = 100
sampled_data = student_data.sample(sample_size)

# Extract data from the sampled dataset
x_data = sampled_data['Age at enrollment']
y_data = sampled_data['Admission grade']

# Scatter plot
plt.scatter(x_data, y_data, label='Sampled Data Points')

# Linear Fit
linear_fit = np.polyfit(x_data, y_data, 1)
linear_fit_fn = np.poly1d(linear_fit)
plt.plot(x_data, linear_fit_fn(x_data), color='red', label='Linear Fit')

plt.title('Scatter Plot with Linear Fit (Sampled Data)')
plt.xlabel('Age at Enrollment')
plt.ylabel('Admission Grade')
plt.legend()
plt.show()

#Scatter Plot: Previous Qualification Grade vs Admission Grade'

sample_size = 100
sampled_data = student_data.sample(sample_size)

# Extract data from the sampled dataset
x_data = sampled_data['Previous qualification (grade)']
y_data = sampled_data['Admission grade']

# Scatter plot
plt.scatter(x_data, y_data, label='Data Points')

# Linear Fit
linear_fit = np.polyfit(x_data, y_data, 1)
linear_fit_fn = np.poly1d(linear_fit)
plt.plot(x_data, linear_fit_fn(x_data), color='red', label='Linear Fit')

plt.title('Scatter Plot: Previous Qualification Grade vs Admission Grade')
plt.xlabel('Previous Qualification Grade')
plt.ylabel('Admission Grade')
plt.legend()
plt.show()

# Extract data from the dataset
x_data = student_data['Inflation rate']
y_data = student_data['Curricular units 2nd sem (grade)']

# Sample a subset of your data (adjust the sample size as needed)
sample_size = 100
sampled_data = student_data.sample(sample_size)

# Extract data from the sampled dataset
sampled_x_data = sampled_data['Inflation rate']
sampled_y_data = sampled_data['Curricular units 2nd sem (grade)']

# Scatter plot
plt.scatter(sampled_x_data, sampled_y_data, label='Sampled Data Points')

# Linear Fit
linear_fit = np.polyfit(x_data, y_data, 1)
linear_fit_fn = np.poly1d(linear_fit)
plt.plot(x_data, linear_fit_fn(x_data), color='cyan', label='Linear Fit')

plt.title('Scatter Plot: Inflation Rate vs Curricular Units 2nd Sem (Grade) (Sampled Data)')
plt.xlabel('Inflation Rate')
plt.ylabel('Curricular Units 2nd Sem (Grade)')
plt.legend()
plt.show()


# Mode of age Enrollment 

selected_variable = 'Age at enrollment'

# Create histogram
plt.hist(student_data[selected_variable], bins=20, color='skyblue', edgecolor='black')
plt.title(f'Histogram of {selected_variable}')
plt.xlabel(selected_variable)
plt.ylabel('Frequency')
plt.show()

#  histogram for 'Admission grade'
plt.hist(student_data['Admission grade'], bins=20, color='lightgreen', edgecolor='black')
plt.title('Histogram for Admission Grade')
plt.xlabel('Admission Grade')
plt.ylabel('Frequency')
plt.show()

#  histogram for 'GDP'
plt.hist(student_data['GDP'], bins=20, color='lightblue', edgecolor='black')
plt.title('Histogram for GDP')
plt.xlabel('GDP')
plt.ylabel('Frequency')
plt.show()

# histogram for 'Inflation rate'
plt.hist(student_data['Inflation rate'], bins=20, color='gold', edgecolor='black')
plt.title('Histogram for Inflation Rate')
plt.xlabel('Inflation Rate')
plt.ylabel('Frequency')
plt.show()

# Count plot for Scholarship Holder vs Gender
plt.figure(figsize=(8, 6))
sns.countplot(x='Scholarship holder', hue='Gender', data=student_data, palette='Set2')
plt.title('Count Plot: Scholarship Holder vs Gender')
plt.xlabel('Scholarship Holder')
plt.ylabel('Count')
plt.show()

















