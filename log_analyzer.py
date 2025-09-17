import re
from collections import Counter

# -----------------------------
# Step 1: Regex pattern to parse logs
# -----------------------------
# Example log format: [2025-09-17 10:05:33] ERROR: Database connection failed
pattern = r"\[(.*?)\]\s+(\w+):\s+(.*)"

# -----------------------------
# Step 2: Read logs into a list
# -----------------------------
logs = []

with open("app.log", "r") as file:
    for line in file:
        match = re.match(pattern, line)
        if match:
            timestamp, level, message = match.groups()
            logs.append({"timestamp": timestamp, "level": level, "message": message})

# -----------------------------
# Step 3: Generate Reports
# -----------------------------
print("Log Report")
print("=====================")

# Count Errors
error_count = sum(1 for log in logs if log["level"] == "ERROR")
print(f"Total Errors: {error_count}")

# Count Warnings
warning_count = sum(1 for log in logs if log["level"] == "WARNING")
print(f"Total Warnings: {warning_count}")

# Most common error message
error_messages = [log["message"] for log in logs if log["level"] == "ERROR"]
if error_messages:
    common_error, count = Counter(error_messages).most_common(1)[0]
    print(f"Most Common Error: '{common_error}' ({count} times)")
