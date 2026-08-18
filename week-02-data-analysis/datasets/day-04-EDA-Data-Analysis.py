import pandas as pd

data = {
    "Name": ["Krishna", "Rahul", "Priya", "Amit", "Neha",
             "Ravi", "Sara", "John"],

    "City": ["London", "Toronto", "London", "Ottawa",
             "Toronto", "London", "Ottawa", "Toronto"],

    "Math": [85, 72, 95, 65, 88, 78, 92, 70],

    "Python": [92, 75, 98, 70, 90, 82, 95, 73],

    "AI": [88, 70, 96, 68, 91, 80, 94, 72]
}

df = pd.DataFrame(data)
print(df)
# Print the dataset shape, columns and data types.
print(f"dataset Shape: {df.shape}")
print(f"dataset Column: {df.columns}")
print(f"dataset Column: {df.columns.tolist()}")
print(f"Datatype: \n{df.dtypes}")
# Run describe() and identify the mean, median and standard deviation of Math.
# print(df.describe())
print("Math mean: 80.62500")
print("Math median: 81.50000")
print("Math standard deviation: 11.00568")
# you can also see dynamically value using loc and iloc()
ds = df.describe()
print(ds)
# using iloc
print(f"Math mean: {ds.iloc[1, 0]:.2f}")
print(f"Math median: {ds.iloc[5, 0]:.2f}")
print(f"Math std: {ds.iloc[2,0]:.2f}")
# using loc
print(ds.loc["mean", "Math"])
print(ds.loc["50%", "Math"])
print(ds.loc["std", "Math"])
# Even simpler, when you specifically want these statistics:
print(df["Math"].mean())
print(df["Math"].median())
print(df["Math"].std())

# Find all unique cities and the number of unique cities.
print(f"Unique City: {df["City"].unique()}")
print(f"number fof unique cities: {df["City"].nunique()}")

# Count students belonging to each city.
print(f"Count students belonging to each city: \n{df.groupby("City")["Name"].count()}")
print(f"Count students belonging to each city: \n{df["City"].value_counts()}")

# Calculate the percentage of students from each city using value_counts(normalize=True).
print(
    f"Calculate the percentage of students from each city: \n{df["City"].value_counts(normalize=True)*100} "
)

# Create an Average column from Math, Python and AI.
df["Average"] = df[["Math", "Python", "AI"]].mean(axis=1)
print(df)

# Sort students from highest Average to lowest.
print(f"highrst -> lowest: \n{df.sort_values("Average",ascending= False)}")

# Find the student with the highest Average using idxmax().
print(f"Highest Average:\n{df.loc[df["Average"].idxmax()]}")

# Find the student with the lowest Average using idxmin().
print(f"Lowest Student:\n{df.loc[df["Average"].idxmin()]}")

# Calculate the average Math score for each City.
print(f"Average Math score: \n {df.groupby("City")["Math"].mean()}")

# Calculate average Math, Python and AI scores for each City.
print(f"Average Math, Python and AI scores for each City: \n{df.groupby("City")[["Math", "Python", "AI"]].mean()}")

# For each City, calculate the mean, minimum and maximum Math score using agg().
print(f"calculate the mean, minimum and maximum Math score: \n{df.groupby("City")["Math"].agg(["mean", "max", "min"])}")

# Calculate the correlation matrix for Math, Python and AI.
print(f"Calculate the correlation matrix for Math, Python and AI: \n{df[["Math", "Python", "AI"]].corr()}")

# Q1. What is the difference between mean() and median()?
# A1. mean() = Add all values and divide by the number of values. and median() = Sort the data and find the middle value. -- Median is the middle value of an ordered dataset.

# Q2. What does a high standard deviation tell us about the values?
# A2. High standard deviation - Values are MORE spread out from the mean. AND Low standard deviation- Values are MORE clustered/close to the mean.
# LOW std  → 🫂 close together
# HIGH std → ↔️ spread apart
# The values are more spread out around the mean "High standard deviation"

# Q3. What's the difference between:df["City"].unique() and df["City"].nunique()
# A3. .unique()-> give what are the unique values are there? and nunique()-> gives how many unique values are there?

# Q4. Explain this in your own words: df.groupby("City")["Math"].mean()
# A4. output are -> each city's students, average of math score

# Q5. If Python and AI have a correlation of 0.95, does that prove that high Python scores cause high AI scores? Why or why not?
# A5. first of all if Python and AI corr() = 0.95 that does not mean python score cause of AI score. it reflect correlation between Python and AI score has a strong corelation it does not prove causing.

# 🏆 Day 4 Mini-Project — Student Performance EDA
print()
print("STUDENT PERFORMANCE EDA")
print()
print("Dataset Overview".center(30, "="))
print(df)
print(f"Number of students: {df["Name"].count()}")
print(f"Number of columns: {len(df.columns)}")
# using shape-
print("Using shape")
print(f"Number of students: {df.shape[0]}")
print(f"Number of columns: {df.shape[1]}")
print(f"Unique cities: \n{df["City"].unique()}")

print()
print("Overall Performance".center(30, "="))
print(f"Overall Math average: {df["Math"].mean():.2f}")
print(f"Overall Python average: {df["Python"].mean():.2f}")
print(f"Overall AI average: {df["AI"].mean():.2f}")
print(f"Overall student Average: {df["Average"].mean():.2f} ")

print()
print("Top/Bottom Performance".center(30,"="))
print(f"Highest-performing student: \n{df.loc[df['Average'].idxmax()]}") #it will give full array of that student
# but want only name of that student
top_index = df["Average"].idxmax()
print(f"name:::: {df.loc[top_index, "Name"]}")
# or you can do in another way
print(
    f"name::: \n{df.loc[top_index, ["Name", "Average"]]}"
)

print()
print(f"Lowest-performing student: \n{df.loc[df['Average'].idxmin()]}")
low_index = df["Average"].idxmin()
print(f"name::: \n{df.loc[low_index, ["Name", "Average"]]}")
print()
print(f"Top 3 students by Average: \n{df.sort_values('Average', ascending=False).head(3)}")

print()
print("City Analysis".center(30,"="))
print(f"Number of students per city: \n{df["City"].value_counts()}")
print(f"Average Math/Python/AI scores per city: \n{df.groupby("City")[["Math", "Python", "AI"]].mean()}")
print(f"Mean/min/max Math score per city: \n{df.groupby("City")["Math"].agg(["mean", "min", "max"])}")

print()
print("Relationships".center(30,"="))
print(f"Correlation between Math, Python and AI: \n{df[["Math", "Python", "AI"]].corr()}")