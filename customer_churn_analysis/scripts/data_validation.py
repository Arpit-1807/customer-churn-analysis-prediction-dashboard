# Import Libraries
import pandas as pd
import numpy as np

# Load Dataset
file_path = r"E:\arpit_works\customer_churn_prediction_bi_dashboard\customer_churn_analysis\data\raw\telco_customer_churn.csv"

print("Checking file...")

df = pd.read_csv(file_path)

print("File loaded successfully!")
print(df.head())

# Check Dataset Shape
print(df.shape)

# Check Column Names
print("\nColumns:")
print(df.columns.tolist())

# Dataset Information
print("\nDataset Info:")
print(df.info())

# Data Quality Check 1: Missing Values
missing_values = df.isnull().sum()

print("\nMissing Values:")
print(missing_values)

# Data Quality Check 2: Blank Values
blank_values = (df == '').sum()

print("\nBlank Values:")
print(blank_values)

# Data Quality Check 3: Duplicate Records
duplicates = df.duplicated().sum()

print("\nDuplicate Rows:")
print(duplicates)

# Data Quality Check 4: Unique Values
unique_values = df.nunique()

print("\nUnique Values:")
print(unique_values)

# Convert TotalCharges from Object to Numeric
df["TotalCharges"] = pd.to_numeric(
    df["TotalCharges"],
    errors="coerce"
)
print(df["TotalCharges"].dtype)

# Check New Missing Values
print(df["TotalCharges"].isnull().sum())

# Handle Missing Values
df = df.dropna()
print(df.shape)


# Create Data Quality Report
quality_report = pd.DataFrame({
    "Column": df.columns,
    "DataType": df.dtypes.values,
    "Missing_Values": df.isnull().sum().values,
    "Unique_Values": df.nunique().values
})

quality_report.to_csv(
    "E:/arpit_works/customer_churn_prediction_bi_dashboard/customer_churn_analysis/reports/outputs/data_quality_report.csv",
    index=False
)

print("Data Quality Report Saved")


# Save Clean Dataset
df.to_csv(
    "E:/arpit_works/customer_churn_prediction_bi_dashboard/customer_churn_analysis/data/cleaned/clean_telco_customer_churn.csv",
    index=False
)

print("Clean Dataset Saved")


# Additional Analysis

## Customer Churn Distribution
print(df["Churn"].value_counts())
print(df["Churn"].value_counts(normalize=True)*100)

# Numerical Summary
print(df.describe())