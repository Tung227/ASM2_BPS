import pandas as pd
import matplotlib.pyplot as plt

# Read the cleaned CSV file
file_path = '/SE06206/product_group_table_cleaned.csv'
df = pd.read_csv(file_path)

# Create a bar chart to display the number of products in each market segment
plt.figure(figsize=(10, 6))
df['MarketSegment'].value_counts().plot(kind='bar', color='skyblue')
plt.title('Number of Products in Each Market Segment')
plt.xlabel('Market Segment')
plt.ylabel('Number of Products')
plt.xticks(rotation=45)
plt.show()

# Significance: This bar chart helps us understand the distribution of products across different market segments. We can easily see which market segment has the most products.

# Create a pie chart to display the percentage of product types in the main categories
plt.figure(figsize=(8, 8))
df['Category'].value_counts().plot(kind='pie', autopct='%1.1f%%', colors=['lightcoral', 'yellowgreen', 'lightblue'])
plt.title('Percentage of Product Types in Main Categories')
plt.ylabel('')
plt.show()

# Significance: This pie chart provides an overview of the percentage of product types in the main categories. It helps identify which category has the largest proportion of products.

# Create a scatter plot to examine the relationship between creation date and product activation status
plt.figure(figsize=(10, 6))
plt.scatter(df['DateCreated'], df['IsActive'], c='green', alpha=0.5)
plt.title('Relationship Between Creation Date and Product Activation Status')
plt.xlabel('Creation Date')
plt.ylabel('Activation Status (IsActive)')
plt.xticks(rotation=45)
plt.show()

# Significance: This scatter plot helps us examine the relationship between the product's creation date and its activation status. We can see if products created on certain dates have higher activation rates.

# Create a bar chart to display the number of products by group
plt.figure(figsize=(10, 6))
df['GroupName'].value_counts().plot(kind='bar', color='orange')
plt.title('Number of Products by Group')
plt.xlabel('Product Group')
plt.ylabel('Number of Products')
plt.xticks(rotation=45)
plt.show()

# Significance: This bar chart helps us see the number of products in each product group. It allows us to easily identify which group has the most products and which has fewer.
