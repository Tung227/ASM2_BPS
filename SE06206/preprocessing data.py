import pandas as pd

# Read the uploaded CSV file
file_path = '/SE06206/product_group_table.csv'
df = pd.read_csv(file_path)

# Display basic information
print("Overview of columns and data types:")
df_info = df.info()
print(df_info)

print("\nDisplay basic statistics:")
df_describe = df.describe(include='all')
print(df_describe)

print("\nNumber of missing values in each column:")
df_missing = df.isnull().sum()
print(df_missing)

# Remove rows with missing values
df_cleaned = df.dropna()

# Display data after removing rows with missing values
print("Data after removing rows with missing values:")
print(df_cleaned)

# Check and remove invalid data in the IsActive column
df_valid_is_active = df_cleaned[df_cleaned['IsActive'].isin([True, False])]

# Display data after removing invalid values in the IsActive column
print("Data after removing invalid values in the IsActive column:")
print(df_valid_is_active)

# Define the path and name of the new CSV file
output_file_path = '/SE06206/product_group_table_cleaned.csv'

# Use the to_csv method of Pandas to save the data to a new CSV file
df_valid_is_active.to_csv(output_file_path, index=False)

# Display completion message
print(f"Data has been successfully saved to the file: {output_file_path}")
