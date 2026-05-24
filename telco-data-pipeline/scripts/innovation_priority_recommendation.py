import pandas as pd

print("Innovation 6 - Incident Priority Recommendation Started")

# Load risk predicted alerts
df = pd.read_csv(
    "output/risk_predicted_alerts.csv"
)

print("Dataset loaded successfully\n")

# Priority recommendation logic
def recommend_priority(row):

    risk = row["risk_score"]

    severity = str(row["severity"])

    # Critical incidents
    if (
        risk >= 9
        or severity == "Disaster"
    ):

        return "P1"

    # High incidents
    elif risk >= 7:

        return "P2"

    # Medium incidents
    elif risk >= 5:

        return "P3"

    # Low incidents
    return "P4"

# Apply recommendation
df["recommended_priority"] = (
    df.apply(
        recommend_priority,
        axis=1
    )
)

print("Priority recommendation completed\n")

# Show results
print(
    df[
        [
            "alertid",
            "host",
            "severity",
            "risk_score",
            "recommended_priority"
        ]
    ].head(15)
)

# Priority summary
print("\nPriority Distribution\n")

print(
    df["recommended_priority"]
    .value_counts()
)

# Save output
df.to_csv(
    "output/priority_recommendation.csv",
    index=False
)

print(
    "\npriority_recommendation.csv saved successfully"
)