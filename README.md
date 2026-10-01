# Student Performance Analysis and Dashboard

## About the Project

This project focuses on analyzing a student performance dataset using Python, Pandas, Matplotlib, and Power BI.

The project includes data cleaning and preparation, exploratory data analysis, data visualization, and an 
interactive dashboard to understand student performance and identify useful patterns in the dataset.

## Problem Statement

The objective of this project is to analyze student performance data and identify useful patterns related to 
students grades, study time, absences, gender, and other available factors.

The project aims to clean and prepare the dataset, perform exploratory analysis, create visualizations, and 
develop an interactive dashboard to present the findings clearly.

## Dataset

I used the UCI Student Performance dataset.

The dataset used in this project is `student-mat.csv`.

- Rows: 395
- Columns: 33
- Main information included: student gender, study time, absences, and grades.
- The final grade column used for analysis is `G3`.

## Tools Used

- Python
- Pandas
- Matplotlib
- Power BI
- CSV
- GitHub

## Data Cleaning Performed

The student performance dataset was cleaned and performed using python and pandas.

The following steps were performed:

- Loaded the CSV file using Pandas.
- Fixed the quotation formatting in the source CSV file.
- Removed unnecessary spaces from text values.
- Checked the number of rows and columns.
- Checked the column names.
- Checked the data types.
- Converted `G1`, `G2`, and `G3` into numeric values.
- Checked for missing values.
- Checked for duplicate rows.
- Checked unique values in categorical columns.
- Checked the minimum and maximum values of numeric columns.
- Saved the cleaned data into a new CSV file.

## Data Quality Results

- Missing values found: 0
- Duplicate rows found: 0
- No obvious inconsistent categorical values were found.
- Numeric values were checked for possible invalid ranges.
- The `G1`, `G2`, and `G3` columns were converted to numeric data types.

The cleaned dataset was saved as 'Cleaned_student.csv'

## Exploratory Data Analysis

Exploratory data analysis was performed using Python, Pandas, and Matplotlib to understand the
dataset and identify useful patterns.

The following analysis was performed:

- Calculated basic statistics for the dataset.
- Analyzed the average, minimum, maximum, and median of `G3`.
- Analyzed the average, minimum, maximum, and median number of absences.
- Checked the correlation between absences and `G3`.
- Analyzed the number of students by gender.
- Analyzed the number of students in each study time category.
- Created charts to visualize the results.

 ### Analysis Results

- Average G3 score: 10.42
- Minimum G3 score: 0
- Maximum G3 score: 20
- Median G3 score: 11
- Average absences: 5.71
- Minimum absences: 0
- Maximum absences: 75
- Median absences: 4
- Number of female students: 208
- Number of male students: 187

## Visualizations

Four visualizations were created to understand the student performance data.

### 1. Absences vs G3

A scatter plot was used to compare the number of absences with the final G3 grade.

The correlation between absences and G3 was approximately `0.034`, which indicates a very weak linear relationship in this dataset.

### 2. G3 Grade Distribution

A histogram was created to show the distribution of students' final G3 grades.

### 3. Students by Gender

A bar chart was created to show the number of students by gender.

- Female students: 208
- Male students: 187

### 4. Students by Study Time

A bar chart was created to show the number of students in each study time category.

## Interactive Dashboard

An interactive dashboard was created using Power BI to present the main 
findings from the student performance dataset.

The dashboard includes the following KPIs:

- Total Students: 395
- Average G3: 10.42
- Average Absences: 5.71
- Highest G3: 20

### Dashboard Visuals

The dashboard includes:

- G3 Grade Distribution
- Students by Gender
- Students by Study Time
- Absences vs G3

### Interactive Filters

The dashboard includes filters for:

- Study Time
- School
- Gender

These filters allow the user to interact with the dashboard and view the 
data based on different categories.

## Key Insights

The analysis of the student performance dataset provided the following insights:

1. The average final G3 grade was 10.42, while the median G3 grade was 11.

2. The number of absences varied from 0 to 75, with an average of 5.71 absences per student.

3. The correlation between absences and G3 was approximately 0.034, showing a very weak linear relationship between the two variables in this dataset.

4. The dataset contains 208 female students and 187 male students.

5. Most students belonged to study time category 2, which represents 2–5 hours of study per week.

6. Students in the higher study-time categories had somewhat higher average G3 scores
7. in this dataset.

## Conclusion

This project helped me understand the complete data analytics process, from cleaning and 
preparing raw data to performing exploratory analysis and creating an interactive dashboard.

Using Python, Pandas, Matplotlib, and Power BI, I analyzed student performance data and 
presented the findings through visualizations and an interactive dashboard.

## Project Files

'''text
Data_Cleaning_Project/
├── data_cleaning.py
├── analysis_data.py
├── student-mat.csv
├── cleaned_students.csv
├── requirements.txt
├── absences_vs_g3.png
├── g3_grade_distribution.png
├── no_of_students_by_gender.png
├── students_by_studytime.png
├── Student_Performance_Dashboard.pbix
└── README.md '''

## How to Run the Python Files

First, install the required packages:

"pip install -r requirements.txt"

To run the data cleaning file

"python data_cleaning.py"

To run the exploratory data analysis

"python analysis_data.py"

The interactive dashboard can be opened using:

"Student_Performance_Dashboard.pbix"







