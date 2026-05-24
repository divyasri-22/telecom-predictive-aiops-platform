import pandas as pd
print("Innovation 4 - Blast Radius Visualization Started")
df = pd.read_csv(
    "output/enriched_alerts.csv"
)
print("Dataset loaded successfully\n")
def build_blast_radius(row):
    host = str(row["host"])
    connected = str(row["connected_to"])
    if connected == "nan":
        return (
            host
            +
            "\n  ↓\n  No connected devices"
        )
    connected_devices = connected.split(",")
    blast_map = host
    for device in connected_devices:
        blast_map += (
            "\n  ↓\n  "
            +
            device.strip()
        )
    return blast_map
df["blast_radius_map"] = df.apply(
    build_blast_radius,
    axis=1
)

print("Blast radius mapping completed\n")
for i in range(min(10, len(df))):
    print(
        "\n"
    )

    print(
        f"Alert ID: {df.loc[i, 'alertid']}"
    )

    print(
        f"Host: {df.loc[i, 'host']}"
    )

    print("\nBlast Radius Map:\n")

    print(
        df.loc[i, "blast_radius_map"]
    )

print(
    "\nBlast radius visualization completed"
)
df.to_csv(
    "output/blast_radius_analysis.csv",
    index=False
)

print(
    "\nblast_radius_analysis.csv saved successfully"
)