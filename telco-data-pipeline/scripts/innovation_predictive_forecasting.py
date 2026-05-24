import pandas as pd
print("Innovation 9 - Predictive Incident Forecasting Started")
risk_df = pd.read_csv(
    "output/risk_predicted_alerts.csv"
)
anomaly_df = pd.read_csv(
    "output/kpi_anomaly_detection.csv"
)
print("Datasets loaded successfully\n")
def forecast_incident(row):
    anomalies = str(
        row["detected_anomalies"]
    ).lower()
    users = row["max_connected_users"]
    prb = row["max_prb_utilization"]
    if (
        "high prb utilization" in anomalies
        and users >= 200
    ):

        return (
            "High probability of congestion escalation "
            "in upcoming monitoring cycles."
        )
    elif (
        "low downlink throughput" in anomalies
    ):
        return (
            "Potential service degradation risk "
            "for connected subscribers."
        )
    elif prb >= 95:
        return (
            "Possible cell instability or overload "
            "condition predicted."
        )
    return (
        "Infrastructure operating within "
        "expected thresholds."
    )
anomaly_df["predictive_forecast"] = (
    anomaly_df.apply(
        forecast_incident,
        axis=1
    )
)
print("Predictive forecasting completed\n")
print(
    anomaly_df[
        [
            "object_name",
            "detected_anomalies",
            "predictive_forecast"
        ]
    ]
)
anomaly_df.to_csv(
    "output/predictive_forecasting.csv",
    index=False
)

print(
    "\npredictive_forecasting.csv saved successfully"
)