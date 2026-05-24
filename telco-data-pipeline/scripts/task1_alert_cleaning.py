import pandas as pd
import json
import re

print("Task 1 Alert Cleaning Started")
with open("data/network_alerts.json", "r") as file:
    data = json.load(file)

print("JSON loaded successfully")

alerts = data["result"]

df = pd.DataFrame(alerts)

print("\nDataFrame Created Successfully\n")

df["clock"] = pd.to_numeric(
    df["clock"],
    errors="coerce"
)

df["clock"] = pd.to_datetime(
    df["clock"],
    errors="coerce",
    unit="s"
)

print("Timestamp Converted Successfully\n")


def extract_host(message):
    match = re.search(r"Host:\s*(.*)", str(message))
    return match.group(1) if match else None


def extract_severity(message):
    match = re.search(r"Severity:\s*(.*)", str(message))
    return match.group(1) if match else None


def extract_problem_name(message):
    match = re.search(r"Problem name:\s*(.*)", str(message))
    return match.group(1) if match else None

df["host"] = df["message"].apply(extract_host)

df["severity"] = df["message"].apply(
    extract_severity
)

df["problem_name"] = df["message"].apply(
    extract_problem_name
)


df["host"] = df["host"].str.strip()

df["severity"] = df["severity"].str.strip()

df["problem_name"] = df["problem_name"].str.strip()

print("Message Extraction Completed\n")


df["invalid_clock"] = df["clock"].isna()

df["empty_subject"] = (
    df["subject"].astype(str).str.strip() == ""
)

df["empty_message"] = (
    df["message"].astype(str).str.strip() == ""
)


df["alert_status"] = df["subject"].apply(
    lambda x: "Resolved"
    if "Resolved" in str(x)
    else "Problem"
)

print("Data Quality Checks Completed\n")


print(
    df[
        [
            "alertid",
            "clock",
            "host",
            "severity",
            "problem_name",
            "invalid_clock",
            "empty_subject",
            "empty_message",
            "alert_status"
        ]
    ].head(10)
)


df.to_csv(
    "output/cleaned_alerts.csv",
    index=False
)

print("\ncleaned_alerts.csv saved successfully")