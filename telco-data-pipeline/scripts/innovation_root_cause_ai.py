import pandas as pd
print("Innovation 3 - AI Root Cause Recommendation Started")
df = pd.read_csv(
    "output/risk_predicted_alerts.csv"
)
print("Dataset loaded successfully\n")
def recommend_root_cause(row):
    severity = str(row["severity"])
    problem = str(row["problem_name"]).lower()
    host = str(row["host"]).lower()
    if (
        "temp" in problem
        or
        "temperature" in problem
    ):
        return (
            "Possible overheating detected. "
            "Check cooling systems and GPU/server airflow."
        )
    elif (
        "vpn" in problem
        or
        "tunnel" in problem
    ):
        return (
            "Possible VPN negotiation failure or "
            "firewall policy mismatch."
        )
    elif (
        "link down" in problem
        or
        "interface" in problem
    ):
        return (
            "Possible fiber disconnect, "
            "switch port failure, or network instability."
        )
    elif (
        "power" in problem
    ):

        return (
            "Possible hardware degradation "
            "or redundant power supply failure."
        )
    elif (
        "snmp" in problem
    ):

        return (
            "Monitoring communication failure. "
            "Check SNMP agent/network reachability."
        )
    elif (
        "firewall" in host
    ):

        return (
            "Possible security policy conflict "
            "or HA synchronization issue."
        )
    elif severity == "Disaster":
        return (
            "Critical infrastructure instability detected. "
            "Immediate investigation required."
        )
    return (
        "Further investigation required."
    )
df["ai_root_cause_recommendation"] = (
    df.apply(
        recommend_root_cause,
        axis=1
    )
)

print("AI root cause recommendation completed\n")
print(
    df[
        [
            "alertid",
            "host",
            "problem_name",
            "ai_root_cause_recommendation"
        ]
    ].head(15)
)
df.to_csv(
    "output/ai_root_cause_analysis.csv",
    index=False
)

print(
    "\nai_root_cause_analysis.csv saved successfully"
)