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
# line chart
plt.plot(
    df["Name"], 
    df["Average"],
    marker='o'
    )
plt.xlabel("Students")
plt.ylabel("Average Score")
plt.title("Student Average Score")
plt.show()
# Bar chart
plt.bar(
    df["Name"],
    df["Average"]
)
plt.xticks(rotation=45)
plt.xlabel("Students")
plt.ylabel("Average")
plt.title("Student Average Score")
plt.show()
# Horizontal bar chart
plt.barh(
    df["Name"],
    df["Average"]
)
plt.xlabel("Students")
plt.ylabel("Average")
plt.title("Student Average Score")
plt.show()

# Histogram
plt.hist(df["Math"])
plt.xlabel("Math Score")
plt.ylabel("Frequency")
plt.title("Distribution of Math Scores")
plt.show()

# Scatter plot
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

# Multiple lines on one graph
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

city_average = df.groupby("City")["Math"].mean()
plt.bar(city_average.index, city_average.values)
plt.xlabel("City")
plt.ylabel("Math Average Marks")
plt.title("Average Math Score By Cities")

plt.show()