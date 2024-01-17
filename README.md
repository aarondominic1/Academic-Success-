
Academic Success Analysis
This repository contains Python code for analyzing factors influencing academic success among students. The dataset used is sourced from a CSV file named students.csv.

Hypothesis
The academic success of students is influenced by a combination of demographic, socio-economic, and educational factors.

Libraries Used
pandas
matplotlib
numpy
seaborn
Data Loading

The dataset is loaded into a pandas DataFrame using the pd.read_csv function.

Analysis Visualizations
Parental Background - Influence of Father's Education
A bar chart is created to visualize the distribution of academic success based on the father's education level.

Gender Differences
A bar chart is generated to compare academic success between genders.

Unemployment Rate after Enrollment
A boxplot is used to show the distribution of the unemployment rate based on academic success.

Marital Status
A stacked bar chart illustrates the distribution of academic success based on marital status.

Inflation Rate
A boxplot demonstrates the distribution of academic success based on the inflation rate.

Scatter Plot - Age at Enrollment vs Admission Grade
A scatter plot with a linear fit is created to analyze the relationship between age at enrollment and admission grade.

Scatter Plot - Previous Qualification Grade vs Admission Grade
A scatter plot with a linear fit is used to explore the relationship between the previous qualification grade and admission grade.

Scatter Plot - Inflation Rate vs Curricular Units 2nd Sem (Grade)
A scatter plot with a linear fit is employed to visualize the relationship between the inflation rate and grades in the 2nd semester.

Histograms
Histograms are created for age at enrollment, admission grade, GDP, and inflation rate to understand their distributions.

Count Plot - Scholarship Holder vs Gender
A count plot is generated to compare the number of scholarship holders based on gender.

Usage
Ensure you have the required libraries installed using:
bash
Copy code
pip install pandas matplotlib numpy seaborn
Run the Python script to execute the analyses:
bash
Copy code
python academic_success_analysis.py

