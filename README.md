# Data Cleaning and Preparation Project

## About the Project

This project is about cleaning and preparing a student performance dataset using Python and Pandas.

The dataset contains information about students such as their age, gender, family background, study habits, absences, and grades.

## Dataset

I used the UCI Student Performance dataset.

The dataset used in this project is `student-mat.csv`.

- Rows: 395
- Columns: 33

## Tools Used

- Python
- Pandas
- CSV
- GitHub

## Data Cleaning Performed

The following steps were performed during the cleaning process:

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

## Output

The cleaned dataset is saved as:

`cleaned_students.csv`

## Project Files

```text
Data_Cleaning_Project/
├── data_cleaning.py
├── student-mat.csv
├── cleaned_students.csv
├── requirements.txt
└── README.md
```
First install the required package
" pip install pandas " or "pip install -r requirements.txt"

Then run the python files
"python data_cleaning.py"


### Why I prefer this version for you

It sounds like **a student documenting what they actually did**, rather than a corporate technical document.

Also, it doesn't claim that you fixed problems that weren't actually present.
For example, we know your results showed **0 missing values and 0 duplicate rows**, so the README says exactly that.
And most importantly, **you should understand everything written in it**. If your interviewer asks,
*"What did you do in this project?"*, you can explain every bullet from your actual work.





