import os

print("Starting Telecom Data Pipeline...\n")

# Run Task 1A
print("Running Task 1A - Alert Cleaning")
os.system("py scripts/task1_alert_cleaning.py")

# Run Task 1B
print("\nRunning Task 1B - KPI Cleaning")
os.system("py scripts/task1_kpi_cleaning.py")

# Run Task 2
print("\nRunning Task 2 - Ticket Extraction")
os.system("py scripts/task2_ticket_extraction.py")

# Run Task 3A
print("\nRunning Task 3A - Alert Enrichment")
os.system("py scripts/task3_alert_enrichment.py")

# Run Task 3B
print("\nRunning Task 3B - KPI Aggregation")
os.system("py scripts/task3_kpi_aggregation.py")

print("\nTelecom Data Pipeline Completed Successfully")