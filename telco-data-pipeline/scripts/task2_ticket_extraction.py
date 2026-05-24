import pandas as pd
import re
print("Task 2 Ticket Extraction Started")
df = pd.read_csv("data/trouble_tickets.csv")
print("Trouble tickets dataset loaded successfully\n")
print(df.head())
def extract_cells(text):
    cells = re.findall(
        r"(Cell_[A-Za-z]+_\d+|BTS-\d+)",
        str(text)
    )
    return ", ".join(cells)
def extract_devices(text):
    devices = re.findall(
        r"(SWITCH-[A-Z\-0-9]+|SERVER-[A-Z\-0-9]+|FIREWALL-[A-Z\-0-9]+)",
        str(text)
    )
    return ", ".join(devices)
def extract_users(text):
    match = re.search(
        r"(\d+)\s*(users|subscribers)",
        str(text),
        re.IGNORECASE
    )
    if match:
        return int(match.group(1))
    return 0
def extract_root_cause(text):
    patterns = [
        r"root cause is (.*?)(\.|,)",
        r"suspected cause is (.*?)(\.|,)",
        r"caused by (.*?)(\.|,)",
        r"due to (.*?)(\.|,)"
    ]
    for pattern in patterns:
       match = re.search(
            pattern,
            str(text),
            re.IGNORECASE
        )

        if match:
            return match.group(1)
    return None
df["affected_cells"] = df["description"].apply(
    extract_cells
)
df["affected_devices"] = df["description"].apply(
    extract_devices
)
df["affected_users"] = df["description"].apply(
    extract_users
)
df["root_cause"] = df["description"].apply(
    extract_root_cause
)
print("\nExtraction Completed\n")
def calculate_impact_score(row):
    score = 1
    if row["priority"] == "P1":
        score += 4

    elif row["priority"] == "P2":
        score += 3

    elif row["priority"] == "P3":
        score += 2

    if row["status"] == "Open":
        score += 2
    users = row["affected_users"]

    if users >= 1000:
        score += 3

    elif users >= 100:
        score += 2

    elif users > 0:
        score += 1
    return min(score, 10)
df["impact_score"] = df.apply(
    calculate_impact_score,
    axis=1
)
print("Impact Score Calculation Completed\n")
print(
    df[
        [
            "ticket_id",
            "priority",
            "status",
            "affected_users",
            "impact_score",
            "root_cause"
        ]
    ].head()
)
df.to_csv(
    "output/extracted_ticket_data.csv",
    index=False
)
print("\nextracted_ticket_data.csv saved successfully")