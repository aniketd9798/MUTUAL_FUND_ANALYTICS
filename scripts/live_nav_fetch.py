import requests
import pandas as pd
import os

# Fetch HDFC Top 100 Direct Fund

if not os.path.exists("data/raw/hdfc_top100_live_nav.csv"):

    scheme_code = 125497

    url = f"https://api.mfapi.in/mf/{scheme_code}"

    response = requests.get(url)

    print("Status Code:", response.status_code)

    data = response.json()

    nav_df = pd.DataFrame(data["data"])

    nav_df.to_csv(
        "data/raw/hdfc_top100_live_nav.csv",
        index=False
    )

    print("HDFC Top 100 NAV saved")

# Fetch 5 major schemes

schemes = {
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_LargeCap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

for name, code in schemes.items():

    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url)

    data = response.json()

    nav_df = pd.DataFrame(data["data"])

    nav_df.to_csv(
        f"data/raw/{name}.csv",
        index=False
    )

    print(f"{name} downloaded successfully")

# Verify files

csv_files = [
    f for f in os.listdir("data/raw")
    if f.endswith(".csv")
]

print("\nTotal CSV Files:", len(csv_files))

