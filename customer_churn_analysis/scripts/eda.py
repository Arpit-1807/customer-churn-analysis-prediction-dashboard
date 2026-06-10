# Load Clean Dataset

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(
    "E:/arpit_works/customer_churn_prediction_bi_dashboard/customer_churn_analysis/data/cleaned/clean_telco_customer_churn.csv"
)

print(df.head())

# 1. Overall Churn Rate
churn_rate = (
    (df["Churn"] == "Yes").mean()
) * 100

print(f"Churn Rate: {churn_rate:.2f}%")

# 2. Churn by Contract Type
contract_churn = pd.crosstab(
    df["Contract"],
    df["Churn"],
    normalize = "index"
) * 100

print(contract_churn)

## Visualization
contract_churn["Yes"].plot(
    kind="bar"
)

plt.title("Churn Rate by Contract")
plt.ylabel("Churn %")
plt.show()

# 3. Churn by Payment Method
payment_churn = pd.crosstab(
    df["PaymentMethod"],
    df["Churn"],
    normalize = "index"
) * 100

print(payment_churn)

## Visualization
payment_churn["Yes"].sort_values(ascending=False).plot(
    kind = "bar"
)

plt.title("Churn by Payment Method")
plt.ylabel("Churn %")
plt.show()

# 4. Churn by Internet Service
internet_churn = pd.crosstab(
    df["InternetService"],
    df["Churn"],
    normalize="index"
) * 100

print(internet_churn)

## Visualization
internet_churn["Yes"].sort_values(ascending=False).plot(
    kind="bar"
)

plt.title("Churn by Internet Service")
plt.ylabel("Churn %")
plt.show()

# 5. Churn by Senior Citizen
senior_churn = pd.crosstab(
    df["SeniorCitizen"],
    df["Churn"],
    normalize="index"
) * 100

print(senior_churn)

## Visualization
senior_churn["Yes"].sort_values(ascending=False).plot(
    kind="bar"
)

plt.title("Churn by Senior Citizen")
plt.ylabel("Churn %")
plt.show()


# Create Tenure Buckets
bins = [0,12,24,36,48,60,72]

labels = [
    "0-12",
    "13-24",
    "25-36",
    "37-48",
    "49-60",
    "60+"
]

df["Tenure_Group"] = pd.cut(
    df["tenure"],
    bins=bins,
    labels=labels
)

# 7. Churn by Tenure Groups
tenure_churn = pd.crosstab(
    df["Tenure_Group"],
    df["Churn"],
    normalize="index"
) * 100

print(tenure_churn)

## Visualization
tenure_churn["Yes"].sort_values(ascending=False).plot(
    kind="bar"
)
plt.title("Churn by Tenure Group")
plt.ylabel("Churn %")
plt.xlabel("Tenure Group ")
plt.show()

# 8. Revenue Analysis
revenue_at_risk = df.loc[
    df["Churn"] == "Yes",
    "MonthlyCharges"
].sum()

print(revenue_at_risk)

# 9. Correlation Analysis
numeric_df = df.select_dtypes(
    include=["int64","float64"]
)

## Visualization (Heatmap)
plt.figure(figsize=(8,5))

sns.heatmap(
    numeric_df.corr(),
    annot=True
)

plt.show()


# Save EDA Outputs
contract_churn.to_csv(
    "E:/arpit_works/customer_churn_prediction_bi_dashboard/customer_churn_analysis/reports/outputs/contract_churn.csv"
)

payment_churn.to_csv(
    "E:/arpit_works/customer_churn_prediction_bi_dashboard/customer_churn_analysis/reports/outputs/payment_churn.csv"
)

internet_churn.to_csv(
    "E:/arpit_works/customer_churn_prediction_bi_dashboard/customer_churn_analysis/reports/outputs/internet_churn.csv"
)

senior_churn.to_csv(
    "E:/arpit_works/customer_churn_prediction_bi_dashboard/customer_churn_analysis/reports/outputs/senior_churn.csv"
)

tenure_churn.to_csv(
    "E:/arpit_works/customer_churn_prediction_bi_dashboard/customer_churn_analysis/reports/outputs/tenure_churn.csv"
)