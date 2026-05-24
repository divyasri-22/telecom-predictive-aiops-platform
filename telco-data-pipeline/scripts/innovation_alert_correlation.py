import pandas as pd
print("Innovation 1 - Alert Correlation Started")
df = pd.read_csv(
    "output/enriched_alerts.csv"
)
print("Dataset loaded successfully\n")
df["clock"] = pd.to_datetime(df["clock"])
df = df.sort_values("clock")
df["correlation_id"] = None
correlation_counter = 1
for i in range(len(df)):
    if pd.isna(df.loc[i, "correlation_id"]):
        current_host = df.loc[i, "host"]
        current_time = df.loc[i, "clock"]
        correlation_id = (
            f"INCIDENT_{correlation_counter}"
        )
        df.loc[i, "correlation_id"] = (
            correlation_id
        )
        for j in range(i + 1, len(df)):
            compare_host = df.loc[j, "host"]
            compare_time = df.loc[j, "clock"]
            time_diff = abs(
                (
                    compare_time - current_time
                ).total_seconds()
            ) / 60
            if (
                time_diff <= 30
                and (
                    current_host == compare_host
                    or
                    df.loc[i, "connected_to"]
                    ==
                    df.loc[j, "connected_to"]
                )
            ):
                df.loc[j, "correlation_id"] = (
                    correlation_id
                )

        correlation_counter += 1
print("Alert correlation completed\n")
print(
    df[
        [
            "alertid",
            "host",
            "problem_name",
            "correlation_id"
        ]
    ].head(15)
)
df.to_csv(
    "output/correlated_alerts.csv",
    index=False
)

print(
    "\ncorrelated_alerts.csv saved successfully"
)