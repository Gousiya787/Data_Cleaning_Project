import pandas as pd

#To Load hte dataset
df = pd.read_csv("student-mat.csv",sep=";",
                 quotechar='"',
                 quoting=3)

#Structural information about the dataset
#print(df.info())

# remove extra quotation marks from values
df = df.map(lambda x: x.replace('"','')
            if isinstance(x, str) else x)

# Convert grade columns from text to integers
df["G1"] = pd.to_numeric(df["G1"])
df["G2"] = pd.to_numeric(df["G2"])
df["G3"] = pd.to_numeric(df["G3"])

# check unique values
print("\nUNIQUE values:")
categorical_columns = ["school","sex","address","famsize","Pstatus","Mjob",
                       "Fjob","reason","guardian","schoolsup","famsup","paid",
                       "activities","nursery","higher","romantic"]
for column in categorical_columns:
    print(f"\n{column}:")
    print(df[column].unique())
#Display the first few rows 
print("\nFirst DATA Rows:")
print(df[["school","sex","age","address","Pstatus"]].head(5).to_string(index=True))

#Display no.of ROWs & COLUMNs
print("\nDataset shape:")
print(df.shape)

#Display columns names in a list
print("\nColumn names:")
print(df.columns.tolist())

#Check the DATA TYPE
print("\nDATA TYPE:")
print(df.dtypes)

#Check the missing values 
print("\nMISSING VALUES:")
print(df.isnull().sum())

#Check DUPLICATE values 
print("\nDUPLICATE ROWS:")
print(df.duplicated().sum())

# Check numeric value ranges
print("\nNUMERIC VALUE RANGES:")

numeric_columns = [
    "age", "Medu", "Fedu", "traveltime", "studytime",
    "failures", "famrel", "freetime", "goout",
    "Dalc", "Walc", "health", "absences",
    "G1", "G2", "G3"
]

for column in numeric_columns:
    print(f"{column}: Min = {df[column].min()}, Max = {df[column].max()}")

# Remove leading and trailing spaces from text columns
for column in df.select_dtypes(include="str").columns:
    df[column] = df[column].str.strip()


# Save cleaned dataset
df.to_csv("cleaned_students.csv", index=False)

print("\nCleaned dataset saved as cleaned_students.csv")
