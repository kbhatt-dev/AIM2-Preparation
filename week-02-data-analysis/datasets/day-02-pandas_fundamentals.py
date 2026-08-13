import pandas as pd
data = {
    "Name": ["Krishna", "Rahul", "Priya", "Amit"],
    "Math": [85, 75, 91, 65],
    "Python": [92, 80, 95, 70],
    "AI": [88, 75, 94, 68],
}

df = pd.DataFrame(data)
print(df)

#sereis
# Sereis has value, index, and datatype
# One Labeled Column
print()
print("Sereis-------------")
scores = pd.Series([85, 75, 65, 55])
print(scores)

# Column index in series
# You can provide labels
print()
print("--------------------")
scores1 = pd.Series(
    [85, 75, 65, 55],
    index = ["Krishna", "Rahul", "Priya", "Amit"]
)
print(scores1)
# Remember Python is case sensitive you dont even type "priya" reathor than "Priya" it gives error. 
print(f"Priya's Score= {scores1["Priya"]}")

# type()
print()
print("------------------")
print(f"type(): {type(df["Math"])}")

# shape()
print()
print("----------------")
print(f"shape: {df.shape}")

# Colums- see columns name
print()
print("------------------")
print(f"coulmn: {df.columns}")
print(df.columns.tolist())

# Index
# Thats the pandas defaulr row index 
print()
print("------------------")
print("index:::" , df.index)

# head()
# To see first 5 row in dataset - you can also change default row
print()
print("-------------------")
print(f"default head():\n {df.head()}")
print(f"you can specify:\n {df.head(2)}")

# tail()
# Same as head but it shows bottom first rows
print()
print("-------------------------")
print(f"tail():::: \n {df.tail()}")
print(f"specific:: , \n {df.tail(2)}")

# info()
# gives info about- number of rows, columns, column name, non- null value, data type
print()
print("-------info-------")
print(f"info::: {df.info()}")

df.info()

# Datatype- inspects just the column datatypes.
print()
print("--------------")
print(f"datatype::: \n {df.dtypes}")

# Selecting one column- return a series
print()
print("-----------------")
print(df["Math"])

# Selecting Multiple column---- return multiple columns
print()
print("-----------------------")
print(df[["Name", "Math"]])

# Accessing Rows with loc
print()
print('---------------------')
print(df.loc[0])
print(df.loc[0,"Python"])

# Accesing rows with iloc
# iloc = users numeriic positions
print()
print('---------------------')
print(df.iloc[0]) # get the first row
print(df.iloc[0, 2]) # row = 0 and col = 2

# Filtering
print()
print('---------------------')
print(f"filtering same as Numpy::: \n{df["Math"] > 80}")

# Multiple Condition
# Use & not "and"
print()
print("-----------------------")
result = df[
    (df["Math"] > 80) &
    (df["AI"] > 80)
]
print(result)

# Adding a new column
print()
print("----------------------")
df["Average"] = (
    df["Math"] +
    df["Python"] +
    df["AI"]
) / 3

print(df)

# Better way to calculate the average
print()
print("---------------------------")
df["Average"] = df[["Math", "Python", "AI"]].mean(axis=1)
print(df)

# Basic Statistical Summary with describe()
print()
print("-------------------------")
print(df.describe())

# 🧪 Day 2 Practice
# Exercise 1 — Create a Series
print()
print("--------------Ex-1")
mathScore = pd.Series(
    [85, 75, 91, 65],
    index = ["Krishna", "Rahul", "Priya", "Amit"]
)
print(mathScore)
print(f"Krishna's Score: {mathScore["Krishna"]}")
print(f"Priya's Score: {mathScore["Priya"]}")
print(f"Series datatype: {mathScore.dtype}")
print(f"Series Size: {mathScore.size}")

# Exercise 2 — Create a DataFrame
print()
print("-------------------------Ex-2")
studentData = {
    "Name": ["Krishna", "Rahul", "Priya", "Amit"],
    "Age": [28, 30, 27, 32],
    "City": ["London", "Toronto", "Ottawa", "London"]
}
df = pd.DataFrame(studentData)
print(df)
print(f"Shape: {df.shape}")
print(f"Columns: {df.columns}")
print(f"Datatype: {df.dtypes}")
print(f"first 2 rows: \n{df.head(2)}")
print(f"last 2 rows: \n {df.tail(2)}")

# Exercise 3 — Column Selection
print()
print("-----------------Ex-3")
print(f"Only name: \n{df["Name"]}")
print(f"Only City: \n{df["City"]}")
print(f"Name and Age: \n {df[["Name", "Age"]]}")
print(f"Name and City: \n {df[["Name", "City"]]}")
# Q. Which ones return a Series?
# A. df["Name"] and df["City"] return a Series because each selects one column directly.
# Q. Which ones return a DataFrame?
# A. df - df[["Name", "Age"]] and df[["Name", "City"]] return a DataFrame

# Exercise 4 — loc and iloc
print()
print("-----------------------Ex-4")
print(f"Rahuls full row : \n{df.loc[1]}")
print(f"Priya's city using loc: {df.loc[2, "City"]}")
print(f"First row using iloc: \n{df.iloc[0]}")
print(f"Amit's age using iloc: {df.iloc[3, 1]}")

# Exercise 5 — Filtering
print()
print("----------------------Ex-5")
students = {
    "Name": ["Krishna", "Rahul", "Priya", "Amit"],
    "Math": [85, 75, 91, 65],
    "Python": [92, 80, 95, 70],
    "AI": [88, 75, 94, 68]
}

df = pd.DataFrame(students)
print(df)
print(f"1. Students with Math > 80: \n{df[df["Math"] > 80]}")
print(f"2. Students with Python >= 90: \n{df[df["Python"] >= 90]}")
print(f"3. Students with AI < 80: \n{df[df["AI"] < 80]}")
result = df[
    ((df["Math"] > 80) &
        (df["Python"] > 90))
]
print(f"4. Students with Math > 80 AND Python > 90: \n{result}")

# Exercise 6 — Add Average Column
print()
print("--------------------------------Ex-6")
df["Average"] = df[["Math", "Python", "AI"]].mean(axis=1)
print(df)
print(df[["Name", "Average"]])
print(f" Average >= 80: \n{df[df["Average"] >= 80]}")

# 🏆 Day 2 Mini-Project
# Student Performance DataFrame Analyzer
print()
print("===============================================================================")
print("Student Performance DataFrame Analyzer".center(70, " "))
print("===============================================================================")
print()

spd = {
    "Name": ["Krishna", "Rahul", "Priya", "Amit", "Neha"],
    "Math": [85, 75, 91, 65, 88],
    "Python": [92, 80, 95, 70, 85],
    "AI": [88, 75, 94, 68, 90]
}
df = pd.DataFrame(spd)
print(df)

print(f"Print its shape: {df.shape}")
print(f"Print column names: {df.columns}")
print(f"Print datatypes: \n{df.dtypes}")
print(f"Display the first 3 rows: \n{df.head(3)}")
print(f"Display the last 2 rows: \n{df.tail(2)}")
print(f"Add an Average column")
df["Average"] = df[["Math", "Python", "AI"]].mean(axis=1)
print(df)
print(f"Display only Name and Average: \n{df[["Name", "Average"]]}")
print(f"Find students with Average >= 80: \n{df[df["Average"] >= 80]}")
print(f"Find students with Math >= 85: \n{df[df["Math"] >= 85]}")
print(f"Find students with both Python >= 85 and AI >= 85")
result = df[
    ((df["Python"] >= 85) &
           (df["AI"] >= 85))
]
print(result)
print(f"Print a statistical summary using describe(): \n{df.describe()}")
print(f"Print the highest average: {df["Average"].max():.2f}")
print(f"Print the lowest average: {df["Average"].min():.2f}")

# Q. What is the difference between these two? print(df["Math"]) and print(df[["Math"]])
# A.  df["Math"] returns a Series because one column name is passed directly.
# df[["Math"]] returns a DataFrame because a list of column names is passed.
print()
print(df["Math"])
print(df[["Math"]])

