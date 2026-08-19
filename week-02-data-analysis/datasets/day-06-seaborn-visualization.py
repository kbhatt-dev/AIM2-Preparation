""" STUDENT PERFORMANCE
ADVANCED VISUALIZATION

1. Student Average Scores
   → Seaborn bar plot

2. Math Score Distribution
   → Histogram + KDE

3. Math Scores by City
   → Box plot

4. Python vs AI by City
   → Scatter plot + hue

5. Python vs AI Trend
   → Regression plot

6. Subject Correlations
   → Heatmap

7. Subject Relationships
   → Pair plot """

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


print("STUDENT PERFORMANCE ADVANCED VISUALIZATION")
print("==========================================")

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

print("1. Student Average Scores")
sns.barplot(
    data=df,
    x="Name",
    y="Average",
)
plt.title("Student Average Scores")
plt.xticks(rotation=45)
plt.show()

print("2. Math Score Distribution")
sns.histplot(
    data=df,
    x="Math",
    kde=True
)
plt.title("Math Score Distribution")
plt.show()

print("3. Math Scores by City")
plt.figure(figsize=(10,5))
sns.boxplot(
    data=df,
    x="City",
    y="Math"
)
plt.title("Math Scores by City")
plt.show()

print("4. Python vs AI by City")
sns.scatterplot(
    data=df,
    x="Python",
    y="AI",
    hue="City"
)
plt.title("Python vs AI by City")
plt.show()

print("5. Python vs AI Trend")
sns.regplot(
    data=df,
    x="Python",
    y="AI"
)
plt.title("Python vs AI Trend")
plt.show()

print("6. Subject Correlations")
Corrilation = df[["Math", "Python", "AI"]].corr()
sns.heatmap(
    Corrilation,
    annot=True
)
plt.title("Subject Correlations")
plt.show()


print("7. Subject Relationships")
g = sns.pairplot(
    df[["Math", "Python", "AI"]]
)

g.fig.suptitle("Subject Relationships", y=1.02)

plt.show()
# also add city grouping
g = sns.pairplot(
    df,
    vars=["Math", "Python", "AI"],
    hue="City"
)
g.fig.suptitle("Subject Relationships", y=1.02)
plt.show()

# 🧠 Day 6 Assessment Questions

# Put your answers as comments at the bottom of your code:

# Q1. Why might Seaborn be easier than Matplotlib when working with Pandas DataFrames?
# A1. Because it is conveniant and statistical visualization library

# Q2. What does hue do?
# A2. hue maps another variable to different colors, allowing us to see groups while still examining the relationship between X and Y.

# Q3. What does the middle line in a box plot represent?
# A3. it represent midiun of that box same as 50% in plt.discribe()

# Q4. What does kde=True add to a histogram?
# A4. it adds a smooth curve representing the approximate shape of the distributions. It is calculated from the individual observations to estimate where the data is concentrated.

# Q5. What's the difference between a scatter plot and a regression plot?
# A5. scatter plot -> relation between that 2 vareables or axies between eachother , regression plot -> gives individual plot + trand line which helps proper vizualization 

# Q6. What does annot=True do in a heatmap?
# A6. to display the numerical connection value inside the heatmap cells.

# Q7. Why are the diagonal values of a correlation heatmap 1.0?
# A7. because it correlation with it self and that is obeausly 1.0 / stron possitve relationship like Math vs Math and so on.

# Q8. Why is pairplot() useful for EDA?
# A8. it is automatically creates multiple chars comparing numarical columns without manually makking several scattle plot code.

# Q9. If a regression plot shows a strong upward trend, can we conclude that X causes Y? Explain.
# A9. defiinetly NO-> it shows just relationship between x and y. it doesnot prove causesing.