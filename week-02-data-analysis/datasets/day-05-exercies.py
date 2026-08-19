import matplotlib.pyplot as plt
import pandas as pd

data = {
    "Name": [
        "Krishna", "Rahul", "Priya", "Amit",
        "Neha", "Ravi", "Sara", "John"
    ],

    "City": [
        "London", "Toronto", "London", "Ottawa",
        "Toronto", "London", "Ottawa", "Toronto"
    ],

    "Math": [85, 72, 95, 65, 88, 78, 92, 70],
    "Python": [92, 75, 98, 70, 90, 82, 95, 73],
    "AI": [88, 70, 96, 68, 91, 80, 94, 72]
}

df = pd.DataFrame(data)
df["Average"] = df[["Math", "Python", "AI"]].mean(axis=1)

print(df)

# Exercise 1 — Student Average Bar Chart
plt.figure(figsize=(10,5))
plt.bar(
    df["Name"],
    df["Average"]
)
plt.title("Students Average Chart")
plt.xlabel("Students")
plt.ylabel("Average Scores")
plt.show()
# we do not need rotate labels righ now, because students name size are not that big.

# Exercise 2 — Math Distribution
plt.hist(df["Math"], bins=5)
plt.title("Students Math Score Distribution")
plt.xlabel("Math Score")
plt.ylabel("Students")
plt.show()

# it shows - around 65-70 math score range students are 2, 70-75, 75-80 each has 1 student, 85-90, 90-95 each has 2 students.  
# i understand the fraph and i also change bin value and see graph but i did not get that original use why we add 5 range like what shouth that redirect it shows range of matscores or any  other thing coz if i change bin graph hase changed but i did not get it why it has to change?

# Exercise 3 — Python vs AI
plt.figure(figsize=(10,5))
plt.scatter(
    df["Python"],
    df["AI"]
)
plt.xlabel("Python Score")
plt.ylabel("AI Score")
plt.title("Python vs AI Scores")
plt.grid()
plt.show()

# Does the visual pattern agree with yesterday's strong positive correlation? -> yes

# Exercise 4 — Subject Comparison
plt.figure(figsize=(10,5))
plt.plot(
    df["Name"],
    df["Math"],
    marker="o",
    label="Math"
)
plt.plot(
    df["Name"],
    df["Python"],
    marker="o",
    label="Python"
)
plt.plot(
    df["Name"],
    df["AI"],
    marker="o",
    label="AI"
)
plt.xticks(rotation=45)
plt.xlabel("Students")
plt.ylabel("Scores")
plt.title("Student Subject Score")
plt.legend()
plt.show()

# Exercise 5 — City Analysis
city_average = df.groupby("City")["Math"].mean()
plt.bar(city_average.index, city_average.values)
plt.xlabel("City")
plt.ylabel("Math Average Marks")
plt.title("Average Math Score By Cities")

plt.show()

# Q1. Why is a bar chart more appropriate than a line chart for comparing student averages?
# A2. because bar chart compare categoreis and we want comparing student average for that bar chart is more appropriate then line chart which mainly used for tred, orders or time.

# Q2. What's the difference between a bar chart and histogram?
# A2. as i told previous ans bar chart are mainly used for comparing categories and histogram is use for automatic grouping for given values using bins/ranges

# Q3. What does bins=5 mean in:
# A3. bins=5 tells Matplotlib to divide the range of Math scores into 5 intervals and count how many student scores fall into each interval.
# The histogram shows how the 8 Math scores are distributed across five score intervals, with some intervals containing more students than others.

# Q4. Why is a scatter plot useful for comparing Python and AI scores?
# A4. because, scatter use for comparing two numerical values, and python and ai scores both are numerical.

# Q5. What is the purpose of: plt.legend()
# A5. It shows which line suggested which subjects.

# Q6. Explain- city_average = df.groupby("City")["Math"].mean()
# plt.bar(city_average.index, city_average.values)
# A6. city_average= the first line of code is give group of city math score average, and secod line create bar chart for that value as (city name (x), avegare math score(y) for visualization )
""" corr()
→ numerical evidence

scatter()
→ visual evidence """

# 🏆 Day 5 Mini-Project — Student Performance Dashboard
print()
print("🏆 Day 5 Mini-Project — Student Performance Dashboard".center(56, "="))
""" STUDENT PERFORMANCE VISUALIZATION

1. Student Average Scores
   → Bar chart

2. Math Score Distribution
   → Histogram

3. Python vs AI
   → Scatter plot

4. Subject Performance
   → Math/Python/AI line comparison

5. Average Math by City
   → Bar chart """

# 1. Student Average Scores
print("1. Student Average Scores")
plt.figure(figsize=(10,5))
plt.bar(
    df["Name"],
    df["Average"]
)
plt.xticks(rotation=45)
plt.xlabel("Students")
plt.ylabel("Average")
plt.title("Student Average Score")
plt.show()
# 2. Math Score Distribution
print("2. Math Score Distribution")
plt.figure(figsize=(10,5))
plt.hist(df["Math"])
plt.xlabel("Math Score")
plt.ylabel("Frequency")
plt.title("Distribution of Math Scores")
plt.show()
# 3. Python vs AI
print("3. Python vs AI")
plt.figure(figsize=(10,5))
plt.scatter(
    df["Python"],
    df["AI"]
)
plt.xlabel("Python Score")
plt.ylabel("AI Score")
plt.title("Python vs AI Scores")
plt.grid()
plt.show()
# 4. Subject Performance
print("4. Subject Performance")
plt.figure(figsize=(10,5))
plt.plot(
    df["Name"],
    df["Math"],
    marker="o",
    label="Math"
)
plt.plot(
    df["Name"],
    df["Python"],
    marker="o",
    label="Python"
)
plt.plot(
    df["Name"],
    df["AI"],
    marker="o",
    label="AI"
)
plt.xlabel("Students")
plt.ylabel("Scores")
plt.title("Student Subject Score")
plt.legend()
plt.show()
# 5. Average Python by City
plt.figure(figsize=(10,5))
print("5. Average Python by City")
city_average = df.groupby("City")["Python"].mean()
plt.bar(city_average.index, city_average.values)
plt.xlabel("City")
plt.ylabel("Python Average Marks")
plt.title("Average Python Score By Cities")

plt.show()

