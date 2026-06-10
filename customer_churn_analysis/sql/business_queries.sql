# Fix the Churn Column Issue and remove the carriage return character
SET SQL_SAFE_UPDATES = 0;
UPDATE customer_churn
SET Churn = REPLACE(Churn, CHAR(13), '');
SET SQL_SAFE_UPDATES = 1;

SELECT
Churn,
HEX(Churn),
LENGTH(Churn)
FROM customer_churn
GROUP BY Churn;

# Query 1: Overall Churn Rate
SELECT
ROUND(
    SUM(CASE WHEN Churn = "Yes" THEN 1 ELSE 0 END) / COUNT(*) * 100,
    2
) AS churn_rate
FROM customer_churn;

# Query 2: Churn by Contract
SELECT
Contract,
COUNT(*) AS customers,
SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END) AS churned_customers,
ROUND(
SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END)
*100.0/COUNT(*),2
) AS churn_rate
FROM customer_churn
GROUP BY Contract
ORDER BY churn_rate DESC;
-- Interpretation: Customer commitment strongly reduces churn.

# Query 3: Churn by Internet Service
SELECT
InternetService,
ROUND(
SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END)
*100.0/COUNT(*),2
) AS churn_rate
FROM customer_churn
GROUP BY InternetService
ORDER BY churn_rate DESC;
-- Interpretation: Premium service customers may have higher expectations or price sensitivity.

# Query 4: Churn by Payment Method
SELECT
PaymentMethod,
ROUND(
SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END)
*100.0/COUNT(*),2
) AS churn_rate
FROM customer_churn
GROUP BY PaymentMethod
ORDER BY churn_rate DESC;
-- Interpretation: Payment method is a strong churn indicator.

# Query 5: Revenue at Risk
SELECT
ROUND(
SUM(MonthlyCharges),2
) AS revenue_at_risk
FROM customer_churn
WHERE Churn='Yes';

# Query 6: Average Monthly Charges
SELECT
Churn,
ROUND(
AVG(MonthlyCharges),2
) AS avg_monthly_charges
FROM customer_churn
GROUP BY Churn;
-- Intrepretation: The company is losing higher-value customers, it means Large Revenue Impact.

# Query 7: Tenure Group Analysis
SELECT
CASE
WHEN tenure <=12 THEN '0-12'
WHEN tenure <=24 THEN '13-24'
WHEN tenure <=36 THEN '25-36'
WHEN tenure <=48 THEN '37-48'
WHEN tenure <=60 THEN '49-60'
ELSE '60+'
END AS tenure_group,

COUNT(*) AS customers,

ROUND(
SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END)
*100.0/COUNT(*),2
) AS churn_rate

FROM customer_churn

GROUP BY tenure_group

ORDER BY churn_rate DESC;
-- Intrepretation: New Customer Churns Heavily.














