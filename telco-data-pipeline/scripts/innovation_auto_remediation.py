import pandas as pd
print("Innovation 8 - Auto Remediation Suggestions Started")
df = pd.read_csv(
    "output/ai_root_cause_analysis.csv"
)

print("Dataset loaded successfully\n")
def generate_remediation(row):

    problem = str(row["problem_name"]).lower()

    recommendation = str(
        row["ai_root_cause_recommendation"]
    ).lower()
    if (
        "vpn" in problem
        or
        "tunnel" in problem
    ):

        return (
            "Verify VPN tunnel configuration, "
            "restart tunnel negotiation, "
            "and validate firewall policies."
        )

    elif (
        "temp" in problem
        or
        "temperature" in problem
    ):

        return (
            "Inspect cooling systems, "
            "verify airflow, "
            "and check server/GPU fan status."
        )
    elif (
        "link down" in problem
        or
        "interface" in problem
    ):

        return (
            "Inspect fiber connectivity, "
            "verify switch port health, "
            "and check interface stability."
        )

    elif (
        "power" in problem
    ):

        return (
            "Check redundant power supplies, "
            "inspect hardware components, "
            "and validate power redundancy."
        )

    elif (
        "snmp" in problem
    ):

        return (
            "Verify SNMP agent availability, "
            "check monitoring connectivity, "
            "and validate network reachability."
        )
    return (
        "Perform detailed operational "
        "investigation and infrastructure validation."
    )

df["auto_remediation_action"] = (
    df.apply(
        generate_remediation,
        axis=1
    )
)

print("Auto remediation generation completed\n")
print(
    df[
        [
            "alertid",
            "host",
            "problem_name",
            "auto_remediation_action"
        ]
    ].head(15)
)
df.to_csv(
    "output/auto_remediation_actions.csv",
    index=False
)

print(
    "\nauto_remediation_actions.csv saved successfully"
)