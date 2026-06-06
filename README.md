# Excel Data Validation & Cleaning (IBM Project)

This project focuses on automating the process of data validation and data cleaning in a customer dataset using Python and Pandas.

## Project Overview
Raw datasets often contain missing fields, duplicates, and incorrect formats. This project takes an uncleaned Excel sheet (DATASET.xlsx), processes it through a Python script, and outputs a refined, analysis-ready file.

## Data Cleaning Steps Performed
1. *Load Data:* Read the Excel dataset into a Python environment using Pandas.
2. *Remove Duplicates:* Identifies and eliminates repetitive customer rows.
3. *Data Validation:* Dropped records that lack critical identifying fields like CustomerID.
4. *Handle Missing Values:* Replaced missing entries in PurchaseAmount with the statistical mean (average) value of the column.
5. *Export Output:* Saved the clean dataset into a new file named Cleaned_Dataset.xlsx.

## Tech Stack Used
* *Tools:* Microsoft Excel
* *Language:* Python
* *Libraries:* Pandas, Openpyxl
