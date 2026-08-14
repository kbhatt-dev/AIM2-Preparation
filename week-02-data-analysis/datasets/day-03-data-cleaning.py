import pandas as pd
import numpy as np

data = {
    "Name": ["Krishna", "Rahul", "Priya", "Krishna", "Amit", "Neha"],
    "Age": [28, np.nan, 27, 28, 32, 29],
    "City": ["London", "Toronto", "Ottawa", "London", "london", " Toronto "],
    "Score": [85, 75, np.nan, 85, 70, 92]
}

df = pd.DataFrame(data)
print(df)
print(df.isnull())
print(df.isnull().sum())
print(df[df["Score"].isna()])
print(df.isna())
print(df[df["Score"].notnull()])
print(df.notnull())

clean_df = df.dropna()
print(clean_df)

# imputation
average_age = round(df["Age"].mean())
df["Age"] = df["Age"].fillna(average_age)
print(df)
# It shows rahul value = 28.8 but that is also not valid so what if convert float to int?

score_avg = df["Score"].mean()
df["Score"] = df["Score"].fillna(score_avg)
print(df)

# duplicate data
print(df.duplicated())
# See actual duplicate rows
print(df[df.duplicated()])

df = df.drop_duplicates()
print(df)
print(f"Duplicate values : {df.duplicated().sum()}")

df["City"] = df["City"].str.strip()
print(df)

# mic strip + title
df["City"] = df["City"].str.strip().str.title()

# 🧪 Exercise 1 — Missing Values
data = {
    "Name": ["Krishna", "Rahul", "Priya", "Amit", "Neha"],
    "Age": [28, None, 27, 32, 29],
    "Score": [85, 75, None, 70, 92]
}
df1 = pd.DataFrame(data)
average_age = int(df1["Age"].mean())
average_score = df1["Score"].mean()
print()
print("Exercise 1===================")
print(f"Print the DataFrame: \n{df1}")
print(f"Count missing values for every column: \n{df1.isna().sum()}")
print(f"Print rows where Score is not missing: \n{df1[df1["Score"].notnull()]}")
print(f"Calculate the mean Age: {average_age}")
df1["Age"] = df1["Age"].fillna(average_age)
print(f"Fill the missing Age using the mean Age: \n{df1}")
print(f"Calculate the mean Score: {average_score}")
df1["Score"] = df1["Score"].fillna(average_score)
print(f"Fill the missing Score using the mean Score: \n{df1}")
print(f"Print the cleaned DataFrame")
# Add validations
print(df1)
print(df1.info())
# produces: <class 'pandas.DataFrame'> ... None - Because info() "already prints its information itself and returns" None.
print(df1.isnull().sum())
print(df1.duplicated().sum())

# 🧪 Exercise 2 — Duplicates
print()
print("=======================Exercise 2")
data1 = {
    "Name": ["Krishna", "Rahul", "Priya", "Krishna", "Amit"],
    "Score": [85, 75, 91, 85, 70]
}
df2 = pd.DataFrame(data1)
print(df2)
print(f"Check duplicated(): \n{df2.duplicated()}")
print(f"Count duplicate rows: {df2.duplicated().sum()}")
print(f"Display the duplicate rows: \n{df2[df2.duplicated()]}")
df2 = df2.drop_duplicates()
# If you ever specifically want: specific index like - 0 1 2 3 ... 
# df2 = df2.drop_duplicates().reset_index(drop=True)
print(f"Remove duplicates: \n{df2}")
print(f"Verify the duplicate count is now 0")
# Validate
print(df2.info())
print(df2.duplicated().sum())
print(df2)

# 🧪 Exercise 3 — String Cleaning
print()
print("===========================Exercise 3")
data3 = {
    "Name": [" krishna", "RAHUL ", "priya", " Amit "],
    "City": [" london ", "TORONTO", "ottawa ", " LONDON"]
}
df3 = pd.DataFrame(data3)
print(df3)
df3["Name"] = df3["Name"].str.strip().str.title()
df3["City"] = df3["City"].str.strip().str.title()

print(f"Clean datset: \n{df3}")

# 🧪 Exercise 4 — Incorrect Data Types
print()
print("===================================Exercise 4")
data4 = {
    "Name": ["Krishna", "Rahul", "Priya", "Amit"],
    "Age": ["28", "30", "27", "32"]
}
df4 = pd.DataFrame(data4)
print(df4)
print(f"Print dtypes: \n{df4.dtypes}")
print(f"Convert Age to integer:")
df4["Age"] = df4["Age"].astype(int)
print(df4)
print(f"Print dtypes: \n{df4.dtypes}")
print(df4.info())

# Q. Why was Age not numeric originally even though it contained numbers?
# A. Because, Age array data stored in between " ", so computer think it is String data type wherealse actule age is in intiger datatype.

# 🧪 Exercise 5 — Invalid Numeric Data
print()
print("=================================Exeecise 5")
data5 = {
    "Name": ["Krishna", "Rahul", "Priya", "Amit"],
    "Score": ["85", "unknown", "91", "70"]
}
df5 =pd.DataFrame(data5)
print(df5)
# df5["Score"] = df5["Score"].astype(int)
df5["Score"] = pd.to_numeric(df5["Score"], errors="coerce")
print(df5)
print(f"Count missing values: {df5.isna().sum()}")
print(f"Calculate the mean of valid scores: ")
average_Score = df5["Score"].mean()
print(average_Score)
# column-specific cleaning is safer.
df5["Score"] = df5["Score"].fillna(average_Score)
print(f"Fill the missing score with the mean: \n{df5}")
print(f"Print the cleaned DataFrame")
# Validate
print(df5.info())

# 🏆 Day 3 Mini-Project
print()
print("====================================")
print("Messy Student Dataset Cleaner".center(35, "="))
print("====================================")
print()
data = {
    "Name": [
        " krishna",
        "RAHUL ",
        "priya",
        " krishna",
        "Amit",
        "NEHA "
    ],

    "Age": [
        "28",
        "30",
        "unknown",
        "28",
        "32",
        "29"
    ],

    "City": [
        " london ",
        "TORONTO",
        "ottawa",
        " london ",
        "LONDON",
        " Toronto "
    ],

    "Math": [
        "85",
        "75",
        "91",
        "85",
        "65",
        "88"
    ],

    "Python": [
        92,
        80,
        95,
        92,
        None,
        85
    ],

    "AI": [
        88,
        75,
        94,
        88,
        68,
        None
    ]
}

df = pd.DataFrame(data)
# Display the original dataset
print(df)

# Run info()
# print(df.info())

# Display the original data types
print(df.dtypes)
# Count missing values
print(df.isna().sum())
# Count duplicate rows
print(df.duplicated().sum())
# Clean Name
df["Name"] = df["Name"].str.strip().str.title()
# Clean City
df["City"] = df["City"].str.strip().str.title()
# Convert Age to numeric
df["Age"] = pd.to_numeric(df["Age"], errors="coerce")
# Convert Math to numeric
df["Math"] = pd.to_numeric(df["Math"], errors="coerce")
# Fill missing Age using its mean
average_age = df["Age"].mean()
df["Age"] = df["Age"].fillna(average_age)
# Fill missing Python using its mean
average_pthyon = df["Python"].mean()
df["Python"] = df["Python"].fillna(average_pthyon)
# Fill missing AI using its mean
average_ai = df["AI"].mean()
df["AI"] = df["AI"].fillna(average_ai)
# Remove duplicate rows
df = df.drop_duplicates().reset_index(drop=True)
print(df)
df.info()
# Create an Average column from Math, Python and AI
df["Average"] = df[["Math", "Python", "AI"]].mean(axis=1)
# Display the final cleaned DataFrame
print(df)
# Display final data types
print(df.dtypes)
# Verify missing-value counts
print(df.isna().sum())
# Verify duplicate count
print(df.duplicated().sum())


# Q1. diffrence between df.isna() and df.isna().sum()
# A1. df.isna() gives output of all cell value as True-> missing or False-> not null/ not missing AND df.isna().sum() = count every coloum of missing value name = 0, age = 0 like wise

# Q2. Why shouldn't we automatically replace every missing numerical value with 0?
# A2. 0 is the number and sumetimes it is valid value for some data and for other it is not sensible value like for age 0 is not sensible and math, ai, pyhton or any score that value= 0 means they got nothing in their marks.

# Q3. Why can this fail? df["Age"].astype(int) while this can successfully process messy data? pd.to_numeric(df["Age"], errors="coerce")
# A3. coz not every time age shows in "25" / "68" but in some time that value is missing or someone stored as(using) "unknown" keyboard at that time .astype(int) get number formation error.

