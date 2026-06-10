# Load Dataset
from xml.parsers.expat import model

import pandas as pd

df = pd.read_csv(
    "E:/arpit_works/customer_churn_prediction_bi_dashboard/customer_churn_analysis/data/cleaned/clean_telco_customer_churn.csv"
)

# 1. Remove Customer ID (customerID is not useful for prediction)
df = df.drop(
    columns=["customerID"]
)

# 2. Encode Target
df["Churn"] = df["Churn"].map({
    "No":0,
    "Yes":1
})

# print(df["Churn"].value_counts())

# 3. Create Features & Target
X = df.drop("Churn", axis=1)

y = df["Churn"]

# 4. One-Hot Encoding
X = pd.get_dummies(
    X,
    drop_first=True
)
X = X.astype(float)

# print(X.shape)
# print(X.columns[:10])

# 5. Train-Test Split
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# 6. Train Logistic Regression
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

lr_model = LogisticRegression(max_iter=2000)
lr_model.fit(
    X_train_scaled,
    y_train
)

# 7. Predictions
y_pred = lr_model.predict(X_test_scaled)

y_prob = lr_model.predict_proba(X_test_scaled)[:,1]


# 8. Evaluation
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    confusion_matrix
)

print("Accuracy:",
      accuracy_score(y_test,y_pred))

print("Precision:",
      precision_score(y_test,y_pred))

print("Recall:",
      recall_score(y_test,y_pred))

print("F1:",
      f1_score(y_test,y_pred))

print("ROC-AUC:",
      roc_auc_score(y_test,y_prob))

print(confusion_matrix(y_test,y_pred))

# 9.Feature Importance
importance = pd.DataFrame({
    "Feature":X.columns,
    "Coefficient":lr_model.coef_[0]
})

importance["Abs"] = (
    importance["Coefficient"].abs()
)

importance = (
    importance
    .sort_values(
        "Abs",
        ascending=False
    )
)

print(
    importance.head(15)
)

# 10. Generate Customer Risk Scores
full_prob = lr_model.predict_proba(X)[:,1]

results = df.copy()

results["Churn_Probability"] = full_prob

# 11. Risk Segmentation
def risk_level(prob):

    if prob >= 0.70:
        return "High Risk"

    elif prob >= 0.40:
        return "Medium Risk"

    else:
        return "Low Risk"

results["Risk_Level"] = (
    results["Churn_Probability"]
    .apply(risk_level)
)

# 12. Save Final Output
results.to_csv(
    "E:/arpit_works/customer_churn_prediction_bi_dashboard/customer_churn_analysis/reports/outputs/customer_churn_predictions.csv",
    index=False
)