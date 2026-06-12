import pandas as pd
import sqlite3

fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/02_nav_history.csv")

conn = sqlite3.connect(
    "data/db/bluestock_mf.db"
)

fund_master.to_sql(
    "fund_master",
    conn,
    if_exists="replace",
    index=False
)

nav_history.to_sql(
    "nav_history",
    conn,
    if_exists="replace",
    index=False
)

conn.close()

print("ETL Pipeline Completed")