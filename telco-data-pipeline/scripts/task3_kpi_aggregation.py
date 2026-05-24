import pandas as pd

print("Task 3 KPI Aggregation Started")

df = pd.read_csv(
    "output/cleaned_kpi_wide.csv"
)

print("Dataset loaded successfully\n")

df["endtime_utc"] = pd.to_datetime(
    df["endtime_utc"]
)

df["time_window"] = df["endtime_utc"].dt.floor("5min")

print("5-minute window created\n")

agg_df = (
    df.groupby(
        ["time_window", "object_name"]
    )
    .agg({
        "4G_DL_Throughput_Mbps": "mean",
        "4G_UL_Throughput_Mbps": "mean",
        "4G_DL_PRB_Utilization_Pct": "max",
        "4G_Connected_Users": "max"
    })
    .reset_index()
)

agg_df.rename(
    columns={
        "4G_DL_Throughput_Mbps":
        "avg_dl_throughput",

        "4G_UL_Throughput_Mbps":
        "avg_ul_throughput",

        "4G_DL_PRB_Utilization_Pct":
        "max_prb_utilization",

        "4G_Connected_Users":
        "max_connected_users"
    },
    inplace=True
)
def classify_load(prb):

    if prb < 50:
        return "Low"

    elif prb < 80:
        return "Medium"

    elif prb < 90:
        return "High"

    return "Critical"

agg_df["cell_load_category"] = (
    agg_df["max_prb_utilization"]
    .apply(classify_load)
)

print("KPI aggregation completed\n")

print(agg_df.head())

agg_df.to_csv(
    "output/kpi_aggregated_5m.csv",
    index=False
)

print("\nkpi_aggregated_5m.csv saved successfully")