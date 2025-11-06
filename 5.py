 import numpy as np
 import pandas as pd
 from sklearn.model_selection import train_test_split
 from sklearn.linear_model import LinearRegression
 from sklearn.metrics import mean_squared_error, r2_score
 data = {
 "Size (sq ft)": [1500, 1700, 1800, 2400, 3000, 3500, 4000, 4500, 5000,
 5500],
 "Number of Bedrooms": [3, 3, 4, 4, 5, 5, 5, 6, 6, 7],
 "Age of House (years)": [10, 15, 20, 5, 8, 12, 18, 5, 10, 3],
 "Price ($)": [300000, 350000, 370000, 450000, 600000, 700000,
 720000, 850000, 950000, 1100000], }
 df = pd.DataFrame(data)
 X = df[["Size (sq ft)", "Number of Bedrooms", "Age of House (years)"]]
 y = df["Price ($)"]
 X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,
 random_state=42)
 model = LinearRegression()
 model.fit(X_train, y_train)
 y_pred = model.predict(X_test)
 mse = mean_squared_error(y_test, y_pred)
 r2 = r2_score(y_test, y_pred)
 print(f"\nMean Squared Error (MSE): {mse:.2f}")
 print(f"R^2 Score: {r2:.2f}")
 print("\nPredicted vs Actual Prices:")
 me({"Actual": y_test, "Predicted": y_pred})
 print(comparison) 



       program:
# Importing modules and packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error
# Importing the dataset
df = pd.read_csv('Real-estate1.csv')
print(df.head()) # Display the first few rows of the dataset
print(df.columns) # Display column names
# Plotting a scatterplot
sns.scatterplot(
 x='X4 number of convenience stores',
 y='Y house price of unit area',
 data=df

)
plt.title('Convenience Stores vs House Price')
plt.xlabel('Number of Convenience Stores')
plt.ylabel('House Price per Unit Area')
plt.show()
# Creating feature and target variables
X = df.drop('Y house price of unit area', axis=1) # Feature variables
y = df['Y house price of unit area'] # Target variable
print(X.head()) # Display the first few rows of features
print(y.head()) # Display the first few rows of the target variable
# Splitting the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
 X, y, test_size=0.3, random_state=101)
# Creating and fitting the regression model
model = LinearRegression()
model.fit(X_train, y_train)
# Making predictions
predictions = model.predict(X_test)
# Model evaluation
print('Mean Squared Error:', mean_squared_error(y_test, predictions))
print('Mean Absolute Error:', mean_absolute_error(y_test, predictions))
