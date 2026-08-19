import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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

# 🧪 Day 6 Exercises
# Exercise 1 — Seaborn Bar Plot
sns.barplot(
    data=df,
    x="Name",
    y="Average"
)
plt.title("Student Average Scores")
plt.xticks(rotation=45)
plt.show()

# Exercise 2 — Distribution
sns.histplot(
    data=df,
    x="Math",
    bins=5,
    kde=True
)

plt.title("Math Score Distribution")
plt.show()
# What information does KDE add compared with only showing histogram bars?
# KDE add smooth curve visual trand shape of the distribution.

# Exercise 3 — Box Plot
sns.boxplot(
    data=df,
    x="City",
    y="Math"
)
plt.title("Math Score Distribution by City")
plt.show()
# What does the line inside each box represent?
# line represent each box median value.

# Exercise 4 — Scatter + Hue
sns.scatterplot(
    data=df,
    x="Python",
    y="AI",
    hue="City"
)
plt.title("Python vs AI Scores by City")
plt.show()
# What additional information does hue="City" provide?
# city grouping

# Exercise 5 — Regression
sns.regplot(
    data=df,
    x="Python",
    y="AI"
)
plt.title("Python vs AI regression plot")
plt.show()
# What does the direction of the regression line suggest?
# correlation between python and ai and currently it is upword side so it is said possitve relationship. that does not mean python causeing to AI.
# Does it prove Python performance causes AI performance? -> No

# Exercise 6 — Correlation Heatmap
correlation = df[["Math", "Python", "AI"]].corr()
sns.heatmap(
    correlation,
    annot= True
)
plt.title("Correlation Heatmap")
plt.show()
# Why is the diagonal of the heatmap always 1.0?
# Because it shows correlation between Math vs Math, Pthond vs Python and AI vs AI it self. and that are always +1 means strong possitive relationship

# Exercise 7 — Pair Plot
sns.pairplot(
    df,
    vars=["Math", "Python", "AI"],
    hue="City"
)
plt.title("Math, Python and AI Pairplot")
plt.show()
# Why might pairplot() be useful during EDA?
# Because it provides a quick overview for multiple plot using sible pairplot() use, reathorthen manually making multiple scattler plot.
