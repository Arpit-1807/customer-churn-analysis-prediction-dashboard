# Load Dataset

import pandas as pd
from scipy.stats import chi2_contingency

df = pd.read_csv(
    "E:/arpit_works/customer_churn_prediction_bi_dashboard/customer_churn_analysis/data/cleaned/clean_telco_customer_churn.csv"
)

# Test 1: Contract vs Churn

## Question: Does Contract Type significantly affect Churn?
table = pd.crosstab(
    df["Contract"],
    df["Churn"]
)

chi2,p,dof,expected = chi2_contingency(table)

print("P-value:", p)

## Intrepretation:if p < 0.05, then contract type significantly impacts churn. If p >= 0.05, then contract type does not significantly impact churn.

# Test 2: Internet Service vs Churn

## Question: Does Internet Service Type significantly affect Churn?
table = pd.crosstab(
    df["InternetService"],
    df["Churn"]
)

chi2,p,dof,expected = chi2_contingency(table)

print("P-value:", p)

# Test 3: Payment Method vs Churn

## Question: Does Payment Method significantly affect Churn?
table = pd.crosstab(
    df["PaymentMethod"],
    df["Churn"]
)

chi2,p,dof,expected = chi2_contingency(table)

print("P-value:", p)

# Intrepretation: Contract Type, Internet Service, and Payment Method have statistically significant relationships with customer churn.

## Since all p-values are far below: 0.05, we reject the null hypothesis for all three tests, indicating that these factors are significantly associated with customer churn.