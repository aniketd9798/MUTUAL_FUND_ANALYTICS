-- Query 1: Top 5 Funds by AUM

SELECT scheme_name,
fund_house,
aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;


-- Query 2: Average NAV Per Month

SELECT strftime('%Y-%m', date) AS month,
ROUND(AVG(nav),2) AS avg_nav
FROM fact_nav
GROUP BY month
ORDER BY month;


-- Query 3: SIP YoY Growth

SELECT month,
sip_inflow_crore,
yoy_growth_pct
FROM monthly_sip_inflows
ORDER BY month;


-- Query 4: Transactions by State

SELECT state,
COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY state
ORDER BY total_transactions DESC;


-- Query 5: Funds with Expense Ratio Less Than 1%

SELECT scheme_name,
expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1
ORDER BY expense_ratio_pct;


-- Query 6: Top 5 Funds by 5-Year Return

SELECT scheme_name,
return_5yr_pct
FROM fact_performance
ORDER BY return_5yr_pct DESC
LIMIT 5;


-- Query 7: Average Return by Category

SELECT category,
ROUND(AVG(return_3yr_pct),2) AS avg_return
FROM fact_performance
GROUP BY category
ORDER BY avg_return DESC;


-- Query 8: Funds by Risk Grade

SELECT risk_grade,
COUNT(*) AS total_funds
FROM fact_performance
GROUP BY risk_grade;


-- Query 9: Transaction Amount by Type

SELECT transaction_type,
ROUND(SUM(amount_inr),2) AS total_amount
FROM fact_transactions
GROUP BY transaction_type;


-- Query 10: Average Transaction Amount by State

SELECT state,
ROUND(AVG(amount_inr),2) AS avg_transaction
FROM fact_transactions
GROUP BY state
ORDER BY avg_transaction DESC;