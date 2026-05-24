import pandas as pd
print("Innovation 10 - Self-Healing Automation Started")
df = pd.read_csv(
    "output/predictive_forecasting.csv"
)
print("Dataset loaded successfully\n")
def self_healing_action(row):
    anomalies = str(
        row["detected_anomalies"]
    ).lower()
    forecast = str(
        row["predictive_forecast"]
    ).lower()
    if (
        "congestion" in anomalies
        or
        "congestion" in forecast
    ):
        return (
            "Recommend automatic traffic redistribution, "
            "dynamic load balancing, and subscriber rerouting."
        )
    elif (
        "throughput" in anomalies
    ):
        return (
            "Recommend automated QoS optimization "
            "and bandwidth reallocation."
        )
    elif (
        "high prb utilization" in anomalies
    ):

        return (
            "Recommend automatic spectrum optimization "
            "and congestion mitigation policies."
        )
    return (
        "No self-healing action required. "
        "Infrastructure operating normally."
    )
df["self_healing_recommendation"] = (
    df.apply(
        self_healing_action,
        axis=1
    )
)

print("Self-healing recommendation completed\n")
print(
    df[
        [
            "object_name",
            "detected_anomalies",
            "predictive_forecast",
            "self_healing_recommendation"
        ]
    ]
)
df.to_csv(
    "output/self_healing_recommendations.csv",
    index=False
)

print(
    "\nself_healing_recommendations.csv saved successfully"
)