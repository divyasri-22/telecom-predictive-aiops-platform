import pandas as pd
print("Innovation 7 - KPI Anomaly Detection Started")
df = pd.read_csv(
    "output/kpi_aggregated_5m.csv"
)
print("Dataset loaded successfully\n")
def detect_anomaly(row):
    prb = row["max_prb_utilization"]
    dl = row["avg_dl_throughput"]
    users = row["max_connected_users"]
    anomalies = []
    if prb >= 90:
        anomalies.append(
            "High PRB utilization"
        )
    if dl < 30:
        anomalies.append(
            "Low downlink throughput"
        )
    if users >= 200:
        anomalies.append(
            "High user congestion"
        )

    if len(anomalies) == 0:
        return "Normal"
    return ", ".join(anomalies)
df["detected_anomalies"] = (
    df.apply(
        detect_anomaly,
        axis=1
    )
)

df["anomaly_status"] = (
    df["detected_anomalies"]
    .apply(
        lambda x:
        "Anomaly Detected"
        if x != "Normal"
        else "Normal"
    )
)

print("KPI anomaly detection completed\n")
print(
    df[
        [
            "object_name",
            "avg_dl_throughput",
            "max_prb_utilization",
            "max_connected_users",
            "detected_anomalies",
            "anomaly_status"
        ]
    ]
)

df.to_csv(
    "output/kpi_anomaly_detection.csv",
    index=False
)

print(
    "\nkpi_anomaly_detection.csv saved successfully"
)