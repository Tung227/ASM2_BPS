import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Read the cleaned CSV file
file_path = '/SE06206/sale_table.csv'
df = pd.read_csv(file_path)

# Display column names to identify the sales column
print("Column names in the dataset:")
print(df.columns)

# Assuming 'TotalAmount' is the sales column
if 'TotalAmount' not in df.columns:
    raise ValueError("The dataset does not have a 'TotalAmount' column for prediction.")

# Convert 'SaleDate' to datetime format if present
if 'SaleDate' in df.columns:
    df['SaleDate'] = pd.to_datetime(df['SaleDate'])

# Convert categorical columns to numeric type
categorical_columns = ['PaymentMethod', 'OrderStatus']
for col in categorical_columns:
    if col in df.columns:
        df[col] = df[col].astype('category').cat.codes

# Select features and target variable
X = df[['Quantity', 'DiscountApplied'] + categorical_columns]
y = df['TotalAmount']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Linear Regression model
model = LinearRegression()

# Train the model with the training set
model.fit(X_train, y_train)

# Predict with the test set
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Squared Error:", mse)
print("R-squared:", r2)

# Plot the comparison between actual and predicted values
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, color='blue', alpha=0.5)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color='red', lw=2)
plt.xlabel('Actual Values')
plt.ylabel('Predicted Values')
plt.title('Comparison between Actual and Predicted Values')
plt.show()

# Predict future sales (e.g., with new feature values)
new_data = np.array([[10, 0, 1, 2]])  # Change values to fit your actual data
future_sales_pred = model.predict(new_data)
print("Future sales prediction:", future_sales_pred)

