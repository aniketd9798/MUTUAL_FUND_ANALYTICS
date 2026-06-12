import pandas as pd

scorecard = pd.read_csv(
    "data/processed/fund_scorecard.csv"
)

risk = input(
    "Enter Risk Appetite (Low/Moderate/High/Very High/Moderately High): "
).strip()

if risk == "High":

    recommendations = scorecard[
        scorecard["risk_grade"].isin(
            ["High", "Very High", "Moderately High"]
        )
    ]

else:

    recommendations = scorecard[
        scorecard["risk_grade"] == risk
    ]

recommendations = (
    recommendations
    .sort_values(
        "sharpe_ratio_y",
        ascending=False
    )
    .head(3)
)

print("\nTop 3 Recommended Funds\n")

print(
    recommendations[
        [
            "scheme_name",
            "risk_grade",
            "sharpe_ratio_y",
            "fund_score"
        ]
    ]
)