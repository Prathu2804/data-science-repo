print("Hello from Binder!")
import pandas as pd

# Load the dataset
df = pd.read_excel("./titanic.xls")

# Check for missing values
print("Missing values:")
print(df.isnull().sum())

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Convert data types
df['Age'] = df['Age'].astype(float)

# Rename columns
df.rename(columns={'Pclass': 'PassengerClass', 'Embarked': 'Port'}, inplace=True)

# Save the cleaned dataset
df.to_excel("titanic_data_cleaned.xlsx", index=False)
