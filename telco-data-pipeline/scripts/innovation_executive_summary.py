import pandas as pd
print("Innovation 5 - Executive Incident Summary Started")
alerts_df = pd.read_csv(
    "output/risk_predicted_alerts.csv"
)
kpi_df = pd.read_csv(
    "output/kpi_aggregated_5m.csv"
)
print("Datasets loaded successfully\n")
total_alerts = len(alerts_df)
critical_alerts = len(
    alerts_df[
        alerts_df["risk_category"]
        == "Critical"
    ]
)
high_alerts = len(
    alerts_df[
        alerts_df["risk_category"]
        == "High"
    ]
)
overloaded_cells = len(
    kpi_df[
        kpi_df["cell_load_category"]
        == "Critical"
    ]
)
top_risky_hosts = (
    alerts_df.groupby("host")["risk_score"]
    .max()
    .sort_values(ascending=False)
    .head(5)
)
top_root_causes = (
    alerts_df["problem_name"]
    .value_counts()
    .head(5)
)

print("")
print(" Telecom Executive Incident Summary ")
print("\n")

print(f"Total Alerts: {total_alerts}")

print(f"Critical Risk Alerts: {critical_alerts}")

print(f"High Risk Alerts: {high_alerts}")

print(f"Overloaded Cells: {overloaded_cells}")

print("\nTop Risky Hosts\n")

print(top_risky_hosts)

print("\nMost Frequent Problems\n")

print(top_root_causes)
summary_data = {

    "total_alerts": [total_alerts],

    "critical_alerts": [critical_alerts],

    "high_risk_alerts": [high_alerts],

    "overloaded_cells": [overloaded_cells]
}
summary_df = pd.DataFrame(summary_data)
summary_df.to_csv(
    "output/executive_summary.csv",
    index=False
)
print(
    "\nexecutive_summary.csv saved successfully"
)