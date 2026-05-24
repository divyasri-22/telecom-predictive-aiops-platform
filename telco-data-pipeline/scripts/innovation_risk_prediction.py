import pandas as pd
print("Innovation 2 - Risk Prediction Started")
alerts_df = pd.read_csv(
    "output/correlated_alerts.csv"
)
tickets_df = pd.read_csv(
    "output/extracted_ticket_data.csv"
)
kpi_df = pd.read_csv(
    "output/kpi_aggregated_5m.csv"
)
print("Datasets loaded successfully\n")
def calculate_risk(row):
    score = 0
    severity = str(row["severity"])

    if severity == "Disaster":
        score += 5

    elif severity == "High":
        score += 4

    elif severity == "Average":
        score += 3

    elif severity == "Warning":
        score += 2
    host = str(row["host"])

    if (
        "CORE" in host
        or
        "FIREWALL" in host
    ):
        score += 3

    elif (
        "SERVER" in host
        or
        "SWITCH" in host
    ):
        score += 2
    topology = str(row["connected_to"])

    connected_count = len(
        topology.split(",")
    )

    if connected_count >= 3:
        score += 3

    elif connected_count >= 2:
        score += 2

    elif connected_count >= 1:
        score += 1

    return min(score, 10)
alerts_df["risk_score"] = alerts_df.apply(
    calculate_risk,
    axis=1
)
def classify_risk(score):

    if score >= 9:
        return "Critical"

    elif score >= 7:
        return "High"

    elif score >= 5:
        return "Medium"

    return "Low"

alerts_df["risk_category"] = (
    alerts_df["risk_score"]
    .apply(classify_risk)
)

print("Risk prediction completed\n")
print(
    alerts_df[
        [
            "alertid",
            "host",
            "severity",
            "risk_score",
            "risk_category"
        ]
    ].head(15)
)
alerts_df.to_csv(
    "output/risk_predicted_alerts.csv",
    index=False
)

print(
    "\nrisk_predicted_alerts.csv saved successfully"
)