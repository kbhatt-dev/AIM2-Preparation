import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def analyze_canadian_housing(filename):
    try:
        df = pd.read_csv(filename)
        print(df)

        print()
        print("Displays the first 10 rows.")
        print(df.head(10))

        print()
        print("Prints the dataset shape.")
        print(df.shape)
        print(f"Rows: {df.shape[0]} And Columns: {df.shape[1]}")

        print()
        print("Prints the column names.")
        print(df.columns.tolist())

        print()
        print("Prints the data types.")
        print(df.dtypes)

        print()
        print("Runs info().")
        df.info()

        print()
        print("Runs describe().")
        print(df.describe())

        print()
        print("Counts missing values for every column.")
        print(df.isna().sum())

        print()
        print("Counts duplicate rows.")
        print(df.duplicated().sum())
        print(df[df.duplicated()])

        # Stage2— Data Cleaning

        print()
        print("Task 1 — Clean categorical columns")
        df["City"] = df["City"].str.strip().str.title()
        df["Province"] = df["Province"].str.strip().str.title()
        df["Property_Type"] = df["Property_Type"].str.strip().str.title()
        # print(df)
        print(f"City: {df["City"].unique().tolist()}")
        print(f"Province: {df["Province"].unique().tolist()}")
        print(f"Property Type: {df["Property_Type"].unique().tolist()}")

        print()
        print("Task 2 — Remove duplicates")
        print(f"Duplicate count before: {df.duplicated().sum()}")
        df = df.drop_duplicates()
        df = df.reset_index(drop=True)
        print(f"Duplicate count after: {df.duplicated().sum()}")
        # Pay attention to something else after you remove it: what happens to the DataFrame index?
        # the last row is a duplicate for that reason indexing are same just 24 number of row was deleted.

        print()
        print("Task 3 — Handle missing Price")
        price_mean = df["Price"].mean() 
        print(f"Price mean: {price_mean:.2f}")
        price_median = df["Price"].median()
        print(f"Price median: {price_median:.2f}")
        df["Price"] = df["Price"].fillna(price_median)

        # Price mean: 793695.65
        # Price median: 690000.00
       
        print()
        print("Task 4 — Handle missing Year_Built")
        year_built_mean = df["Year_Built"].mean()
        print(f"year build mean: {year_built_mean:.0f}")
        year_built_median = df["Year_Built"].median()
        print(f"year build median: {year_built_median:.0f}")
        df["Year_Built"] = df["Year_Built"].fillna(year_built_median)
        

        df["Year_Built"] = df["Year_Built"].astype(int)
        print(df)

        print()
        print("Task 5 — Final validation")
        df.info()
        print(df.isna().sum())
        print(df.duplicated().sum())

        print()
        print("STAGE 3 — EXPLORATORY DATA ANALYSIS")
        print("=" * 45)

        print()
        print("1. Overall Housing Statistics")
        print(f"Total number of properties: \n{len(df)}")
        print(f"Average property price: {df['Price'].mean():,.2f}")
        print(f"Median property price: {df["Price"].median():,.2f}")
        print(f"Minimum property price: {df["Price"].min():,.2f}")
        print(f"Maximum property price: {df["Price"].max():,.2f}")
        print(f"Average property area_sqft: {df['Area_sqft'].mean():,.2f}")
        print(f"Average number of bedrooms: {df['Bedrooms'].mean():,.2f}")
        print(f"Average number of bathrooms: {df['Bathrooms'].mean():,.2f}")

        print()
        print("2. Highest & Lowest Priced Properties")
        print(f"Most expensive properties: \n{df.loc[df["Price"].idxmax()]}")
        print(f"Least expensive properties: \n{df.loc[df['Price'].idxmin()]}")

        print()
        print("3. City Analysis")
        print(f"Number of properties per city: \n{df["City"].value_counts()}")
        print(f"Average price by city: \n{df.groupby("City")["Price"].mean()}")
        print(f"Median price by city: \n {df.groupby("City")["Price"].median()}")
        print(f"Average area by city: \n {df.groupby("City")["Area_sqft"].mean()}")

        print()
        print("4. Province Analysis")
        print("1. Number of properties per Province")
        print(df["Province"].value_counts())
        print("2. Average Price per Province")
        print(df.groupby("Province")["Price"].mean())
        print("3. Median Price per Province")
        print(df.groupby("Province")["Price"].median())
        print("4. Average Area_sqft per Province")
        print(df.groupby("Province")["Area_sqft"].mean())
        print(df.groupby("Province")["Price"].agg(["mean", "min", "max", "median"]))

        print()
        print("5. Property Type Analysis")
        print("1. Number of properties of each type")
        print(df["Property_Type"].value_counts())
        # also
        print(df.groupby("Property_Type")["Price"].count())
        print("2. Average price of each property type")
        print(df.groupby("Property_Type")["Price"].mean())
        print("3. Median price of each property type")
        print(df.groupby("Property_Type")["Price"].median())
        print("4. Average area of each property type")
        print(df.groupby("Property_Type")["Area_sqft"].mean())
        print(df.groupby("Property_Type")["Price"].agg(["mean", "min", "max", "median"]))

        print()
        print("6. Correlation Analysis")
        print(df[["Bedrooms", "Bathrooms", "Area_sqft", "Price", "Year_Built"]].corr())

        print()
        print("7. Independent Analysis")
        # my question:
        # 1. sorting high t olow price based data
        ds = df.sort_values("Price", ascending= False)
        print(ds)
        # 2. propery type base describe min and max value based on "Bedrooms", "Bathrooms", "Area_sqft", "Price", "Year_Built"
        print(df.groupby("Property_Type")[["Bedrooms", "Bathrooms", "Area_sqft", "Price", "Year_Built"]].min())
        print(df.groupby("Property_Type")[["Bedrooms", "Bathrooms", "Area_sqft", "Price", "Year_Built"]].max())
        # 3. most important- which year built how many house and how much sqft
        print(df["Year_Built"].value_counts())
        print(df.groupby("Year_Built")["Area_sqft"].agg(["mean", "min", "max", "median"]))

        print()
        print("STAGE 4 — DATA VISUALIZATION")
        print("=" * 45)

        print()
        print("1. Property Price Distribution")

        plt.figure(figsize=(10, 5))

        sns.histplot(
            data=df,
            x="Price",
            bins=8,
            kde=True
        )

        plt.title("Distribution of Property Prices")
        plt.xlabel("Price ($)")
        plt.ylabel("Number of Properties")

        plt.show()

        print()
        print("Average Price by City")
        plt.figure(figsize=(10,5))


        sns.barplot(
            data=df,
            x="City",
            y="Price",
        )
        plt.title("Average Property Price by City")
        plt.xticks(rotation=45)
        plt.xlabel("City")
        plt.ylabel("Average Price")

        plt.show()

        plt.figure(figsize=(10, 5))

        sns.scatterplot(
            data=df,
            x="Area_sqft",
            y="Price",
            hue="Property_Type"
        )

        plt.title("Property Area vs Price")
        plt.xlabel("Area (sqft)")
        plt.ylabel("Price ($)")
        plt.show()

        plt.figure(figsize=(10, 5))
        correlation = df[["Bedrooms", "Bathrooms", "Area_sqft", "Price", "Year_Built"]].corr()
        sns.heatmap(
            correlation,
            annot=True
        )
        plt.title("Housing Correlations")
        plt.show()

        sns.boxplot(
            data=df,
            x="Property_Type",
            y="Price"
        )
        plt.title("Property Prices by Property Type")
        plt.xlabel("Property_Type")
        plt.ylabel("Price")

        plt.show()
# how much area sell in which Province and  Price
        plt.figure(figsize=(10, 5))
        sns.barplot(
            data=df,
            x="Province",
            y="Price",
            hue="Area_sqft"
        )
        plt.title("Province vs Price (Area grouping)")
        plt.xlabel("Province")
        plt.ylabel("Price ($)")
        plt.show()

    except Exception as error:
        print(f"Error reading housing data: {error}")

if __name__ == "__main__":
    analyze_canadian_housing("housing.csv")

# Stage 1 :
""" 
Q1. How many rows and columns are in the dataset?
A1. 25 rows and 8 columns are there is dataset.

Q2. What does one row represent?
A2. it reprensents selling house details like which city, prrovince, how many bedrooms and bathrooms are their, squerfoot area, price, year when it build and proprty type.

Q3. Which columns are numerical?
A3. as per datatype there are total 5 columns are numerical such as bedrooms, bathrooms, area_sqft, price and year build.

Q4. Which columns are categorical/string?
A4. City, Province and property type categorized as a String datatype.

Q5. Which columns contain missing values?
A2. price and year build has missing values

Q6. Are there duplicate rows?
A6. yes there are 1 duplicate row.

Q7. Do you notice any suspicious or incorrect data types?
A7. maybe year build it is no need to float intiger will be good for it. i am not sure but area want to use float reathor than int.

Q8. Based only on this first inspection, what cleaning do you think might be required?
A8. First, I would remove duplicate rows and clean inconsistent string values such as City and Property_Type using strip() and title(). 
    For missing values, I would not automatically fill every numerical column with its overall mean. For a missing Price, I could identify 
    the property's Province, City, and Property_Type, then calculate the typical price of similar properties and use that value if there is 
    enough comparable data. For Year_Built, I would investigate an appropriate mean/median strategy and convert it to an integer if appropriate. 
    Finally, I would validate the cleaned dataset again.
"""
# Stage 2
""" 
Q1. Why did you choose mean or median for Price?
A1. I chose the median because housing prices can contain expensive properties that pull the mean upward. 
    The mean was about $793,696 while the median was $690,000. Since the median represents the middle of the ordered prices 
    and is less sensitive to extreme values, I considered it a more reasonable estimate for this small dataset.
    With a larger dataset, I could use group-based imputation using City, Province and Property_Type.

Q2. Why did you choose mean or median for Year_Built?
A2. I again choose median cause this is much practical then mean,
    how it works: 1st shortlist which year actual house build and then find center node of it.


Q3. Why did Price originally become float64 even though
    the visible prices were whole numbers?
A3. Price originally became float64 because the column contained
    a missing value (NaN). Even though the existing prices were whole
    numbers, Pandas represented the column as floating point so it could
    represent the missing NaN value.


Q4. Why is " london " different from "London" to Pandas
    before string cleaning?
A4. Strings are compared by their characters. Leading/trailing spaces and different capitalization make them different string values.

Q5. Why should we validate the dataset again after cleaning?
A5. to check after cleaning my dataset now look clean? or any other operation required.

Q6. After drop_duplicates(), what happened to the index?
    Why might reset_index(drop=True) sometimes be useful?
A6. after drop_duplicated() that pertiqular index delete but after that index - indexing are as is like before 0, 1, 2, 3, 4, 5 and after 3 which are duplicate row we deleted it now it shows like 0, 1, 2, 4, 5
    it look not proper thats why we use reset_index(drop=True) it sows data as 0, 1, 2, 3, 4
 """

# Stage 3
""" 
Q1. In which City and Province is the most expensive property?
A1. City = Vancouver and Province = British Columbia

Q2. What are its Price, Area_sqft and Property_Type?
A2. Area_sqft                    2400
    Price                   1650000.0
    Property_Type            Detached

Q3. Which city has the highest average property price?
A3. Vancouver    1.406667e+06

Q4. Which city has the largest average property area?
A4. Calgary      1883.333333

Q5. Which province has the highest average property price?
A5. British Columbia  1.406667e+06  1150000.0  1650000.0  1420000.0

Q6. Which Property_Type has the highest average price?
A6. Detached       886000.0  

Q7. Which Property_Type has the largest average area?
A7. Detached     1990.0

Q8. Which variable appears to have the strongest positive correlation with Price?
A8. Year_Built = 0.660508

Q9. If Area_sqft has a strong positive correlation with Price, what does that mean?
A9. it means strong positive linear relation between that two.

Q10. Does that prove that increasing Area_sqft directly causes the property's price to increase? Why or why not?
A10. NO, cause it suggetested strongest possitive "linear relationship".
 """

""" 
Q1. Where are most property prices concentrated?
A1.Most property prices are concentrated approximately between $500,000 and $800,000. There are only a few properties above $1 million.

Q2. Do you notice a long tail toward the higher prices?
A2. Yes. Most properties are concentrated at lower prices, while a few expensive properties extend the distribution toward the right, creating a long right tail.

Q3. Based on the chart, why might the median have been a reasonable choice for filling the missing Price in Stage 2?
A3. The distribution is right-skewed because a few expensive properties create a long upper-price tail. These high values pull the mean upward, 
    while the median is less affected by them. Therefore, the median was a reasonable simple choice for filling the missing Price.

Q4. Which city clearly has the highest average property price?
A4. Vancouver

Q5. Which Property_Type has the highest median Price?
A5. Detached

Q6. Which Property_Type has the widest Price spread?
A6. Detached

Q7. Does the scatter plot generally move upward as Area_sqft increases?
A7. Yes, there is a moderate general upward relationship. 
    As Area_sqft increases, Price tends to increase, although the points do not follow a perfect straight line.

Q8. Are all large properties necessarily expensive?
A8. Larger properties are not necessarily more expensive because price can also depend on factors such as city, province, property type, age, location, etc.

Q9. What extra information does hue="Property_Type" give you compared with Task 4?
A9. hue="Property_Type" groups the points by property type, allowing us to see whether each Area–Price
     observation represents a Detached, Condo, or Townhouse property.

Q10. Which variable has the strongest positive correlation with Price, excluding Price itself?
A10. dont ask same questions i already gave this que ans erlyer

Q11. Which two different variables have the strongest positive correlation in the entire matrix?
A11. badroom ~= area_sqft


 """

# STAGE 5 — FINAL INSIGHTS & CONCLUSION

"""
Q1. What are the most important findings from the housing data?

A1. Property price appears to be influenced by multiple factors,
including location, property area, property type, and year built.
Location is especially important because prices vary significantly
between cities.


Q2. Which city/province appears most expensive?

A2. Vancouver, British Columbia.
Vancouver had the highest average property price in this dataset,
and the most expensive individual property was also located there.


Q3. What did you learn about property type and price?

A3. Detached properties generally have larger areas and had the
highest average and median prices in this dataset.
They also showed a wider price spread than the other property types.


Q4. What relationships did you discover between area,
year built, and price?

A4.
Area_sqft ↔ Price  = 0.51
Year_Built ↔ Price = 0.66

Both show positive correlations with Price.

Year_Built had the stronger positive linear relationship with Price
in this dataset.

However, correlation does not prove causation.


Q5. What limitations does this small dataset have?

A5. The dataset contains only 24 cleaned properties, with only a few
properties representing each city and property type.

Because the sample is very small, the results should not be treated
as an accurate representation of the entire Canadian housing market.

A larger real-world dataset would provide more reliable conclusions.


Q6. What was your overall conclusion?

A6. The analysis suggests that Canadian housing prices in this dataset
vary considerably depending on location and property characteristics.

Vancouver was the most expensive city, while detached properties
generally had larger areas and higher prices.

Price also showed positive relationships with property area and
year built.

Overall, this project demonstrated the complete data-analysis workflow:

Load Data
    ↓
Inspect Data
    ↓
Clean Data
    ↓
Analyze Data
    ↓
Visualize Data
    ↓
Interpret Results
"""