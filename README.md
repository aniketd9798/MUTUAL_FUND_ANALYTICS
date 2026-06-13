# Bluestock Mutual Fund Analytics

## Project Overview

Bluestock Mutual Fund Analytics is an end-to-end data analytics project designed to analyze mutual fund performance, investor behavior, portfolio diversification, and industry trends. The project integrates ETL pipelines, financial analytics, advanced risk assessment, and interactive Power BI dashboards to generate actionable investment insights.

---

## Project Objectives

* Build a complete ETL pipeline for mutual fund datasets.
* Perform exploratory data analysis (EDA).
* Calculate performance and risk metrics.
* Analyze investor behavior and SIP trends.
* Develop a risk-based fund recommendation engine.
* Create an interactive Power BI dashboard for decision-making.

---

## Tech Stack

### Programming & Analytics

* Python
* Pandas
* NumPy
* Plotly

### Database

* SQLite

### Visualization

* Power BI

### Version Control

* Git & GitHub

---

## Project Structure

```text
bluestock_mf_capstone/
├── data/
│   ├── raw/
│   ├── processed/
│   └── db/
├── notebooks/
├── scripts/
├── sql/
├── dashboard/
├── reports/
├── assets/
├── README.md
└── requirements.txt
```

---

## Datasets Used

| Dataset               | Description                         |
| --------------------- | ----------------------------------- |
| Fund Master           | Scheme details and fund information |
| NAV History           | Historical NAV data                 |
| Investor Transactions | SIP, Lumpsum, Redemption records    |
| Portfolio Holdings    | Fund holdings and sector allocation |
| Industry AUM          | Industry growth statistics          |
| SIP Inflows           | Monthly SIP data                    |
| Benchmark Data        | Nifty 50 and Nifty 100 indices      |

---

## Key Analytics Performed

### Performance Analytics

* CAGR (1Y, 3Y, 5Y)
* Sharpe Ratio
* Sortino Ratio
* Alpha
* Beta
* Maximum Drawdown

### Advanced Analytics

* Historical VaR (95%)
* Conditional VaR (CVaR)
* Rolling 90-Day Sharpe Ratio
* Investor Cohort Analysis
* SIP Continuity Analysis
* Sector HHI Concentration
* Fund Recommendation Engine

---

## Dashboard Pages

### Page 1: Industry Overview

* Total AUM
* SIP Inflows
* Folio Count
* AUM by AMC

### Page 2: Fund Performance

* Risk vs Return Analysis
* Fund Scorecard
* NAV Trends
* Benchmark Comparison

### Page 3: Investor Analytics

* State-wise Analysis
* Age Group Analysis
* Transaction Trends

### Page 4: SIP & Market Trends

* SIP vs Nifty Trend
* Category-wise Inflows
* Market Comparison

---

## How to Run the Project

### 1. Clone Repository

```bash
git clone <repository-url>
cd bluestock_mf_capstone
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run ETL Pipeline

```bash
python scripts/etl_pipeline.py
```

### 4. Run Analytics

```bash
python scripts/compute_metrics.py
```

### 5. Run Recommendation Engine

```bash
python scripts/recommender.py
```

### 6. Open Dashboard

Open:

```text
dashboard/bluestock_mf.pbix
```

using Power BI Desktop.

---

## Project Deliverables

* Final_Report.pdf
* Bluestock_MF_Presentation.pptx
* bluestock_mf.pbix
* Advanced_Analytics.ipynb
* var_cvar_report.csv
* rolling_sharpe_chart.png
* recommender.py

---

## Key Outcomes

* Developed a scalable mutual fund analytics platform.
* Automated data ingestion and processing workflows.
* Generated risk-adjusted fund performance insights.
* Built interactive dashboards for business intelligence.
* Implemented a simple risk-based recommendation engine.

---

## Author

**Aniket Dhumal**

Data Analytics Capstone Project – Bluestock Fintech
