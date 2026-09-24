import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("cleaned_students.csv")
print(df.head())

print(df.shape)
#basic satistics
print(df.describe())

#g3 statistics
print(df["G3"].mean())
print(df["G3"].min())
print(df["G3"].max())
print(df["G3"].median())

#min,max,average,median for absences
print(df["absences"].mean())
print(df["absences"].min())
print(df["absences"].max())
print(df["absences"].median())

print(df[["absences","G3"]].corr())

# used to represent the 1st chart
plt.title("Absences VS G3")
plt.scatter(df["absences"],df["G3"])
plt.xlabel("No.of Abceances")
plt.ylabel("G3")

plt.savefig("absences_vs_g3.png") #saving the files
plt.show()

#the histogram() used for the distribuiton 2nd chart
plt.title("G3 Grade distribution")
plt.hist(df["G3"], bins=10)
plt.xlabel("G3")
plt.ylabel("Students")
plt.show()

#stores values in the sex_counts variable t use in chart
sex_counts = df["sex"].value_counts()
print(sex_counts)
print(sex_counts.index)
print(sex_counts.values)

#number of students by gender 3rd chart
plt.bar(sex_counts.index,sex_counts.values)
plt.title("No.of Students by Gender")
plt.xlabel("Gender")
plt.ylabel("No.of Students")
plt.show()

#study time 4th chart
studytime_counts = df["studytime"].value_counts()
plt.bar(studytime_counts.index,studytime_counts.values)
plt.title("No.of students by study time")
plt.xlabel("study time category")
plt.ylabel("No.of Students")
plt.show()
