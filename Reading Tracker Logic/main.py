import pandas as pd

# Load CSV
df = pd.read_csv("database.csv")

# Get inputs
date = input("Enter date: ")
title = input("Enter book title: ")
start = input("Enter start time (HH:MM AM/PM): ")
end = input("Enter end time (HH:MM AM/PM): ")

# Convert to datetime
start_time = pd.to_datetime(start, format="%I:%M %p")
end_time = pd.to_datetime(end, format="%I:%M %p")

# Calculate total time
total_time = (end_time - start_time).total_seconds() / 3600
if total_time < 0:  # overnight case
    total_time += 24

# Build new row
new_row = {
    "Date": date,
    "Book Title": title,
    "Time Start": start,
    "Time End": end,
    "Total Time": f"{int(total_time)}:{int((total_time%1)*60):02d}"
}

# Append
df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

# Save back
df.to_csv("database.csv", index=False)
print("Row added successfully!")

print(df.head())