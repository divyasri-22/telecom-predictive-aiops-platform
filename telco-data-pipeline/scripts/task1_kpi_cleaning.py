import pandas as pd
print("Task 1 KPI Cleaning Started")
df = pd.read_csv("data/kpi_metrics.csv")
print("KPI dataset loaded successfully\n")
print(df.head())
print("\nMissing Values\n")
print(df.isnull().sum())
df["value"] = pd.to_numeric(
    df["value"],
    errors="coerce"
)
df = df[df["value"] >= 0]
print("\nNegative values removed\n")
pivot_df = df.pivot_table(
    index=["endtime_utc", "object_name"],
    columns="kpi_name",
    values="value"
).reset_index()
print("Pivot Transformation Completed\n")
print(pivot_df.head())
pivot_df.to_csv(
    "output/cleaned_kpi_wide.csv",
    index=False
)
print("\ncleaned_kpi_wide.csv saved successfully")
