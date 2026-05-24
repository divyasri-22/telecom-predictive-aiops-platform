import pandas as pd

print("Task 3 Alert Enrichment Started")

alerts_df = pd.read_csv(
    "output/cleaned_alerts.csv"
)

topology_df = pd.read_csv(
    "data/topology.csv"
)

print("Datasets loaded successfully\n")

print(topology_df.head())

topology_grouped = (
    topology_df.groupby("hostname")
    .agg({
        "destination_node": lambda x:
        ", ".join(x.astype(str)),
        "ip_address": "first"
    })
    .reset_index()
)

print("\nTopology aggregation completed\n")

topology_grouped.rename(
    columns={
        "destination_node": "connected_to"
    },
    inplace=True
)

enriched_df = pd.merge(
    alerts_df,
    topology_grouped,
    left_on="host",
    right_on="hostname",
    how="left"
)

enriched_df["topology_found"] = (
    enriched_df["hostname"].notna()
)

print("Alert enrichment completed\n")

print(
    enriched_df[
        [
            "alertid",
            "host",
            "ip_address",
            "connected_to",
            "topology_found"
        ]
    ].head()
)

enriched_df.to_csv(
    "output/enriched_alerts.csv",
    index=False
)

print("\nenriched_alerts.csv saved successfully")