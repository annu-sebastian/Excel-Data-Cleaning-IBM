import pandas as pd

# 1. Load the Excel file
file_name = "DATASET.xlsx"
df = pd.read_excel(file_name, sheet_name="Sheet1")

# 2. Remove duplicate records
df_cleaned = df.drop_duplicates()

# 3. Data Validation: Remove rows where CustomerID is missing
df_cleaned = df_cleaned.dropna(subset=['CustomerID'])

# 4. Handle Missing Values: Fill missing PurchaseAmount with the mean (average) value
mean_purchase = df_cleaned['PurchaseAmount'].mean()
df_cleaned['PurchaseAmount'] = df_cleaned['PurchaseAmount'].fillna(mean_purchase)

# 5. Export the cleaned data to a new Excel file
output_file = "Cleaned_Dataset.xlsx"
df_cleaned.to_excel(output_file, index=False)

print("Data cleaning successfully completed!")
