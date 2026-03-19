import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Fix the random seed so the same results appear every time.
np.random.seed(42)

# Create two telecom usage arrays to simulate different traffic periods.
first_half_usage = np.random.randint(180, 320, size=180)
second_half_usage = np.random.randint(260, 420, size=180)

# Combine both arrays into one 360-element dataset.
telecom_usage_360 = np.concatenate((first_half_usage, second_half_usage))

# Reshape the 1D array into 12 months and 30 days.
telecom_usage_12x30 = telecom_usage_360.reshape(12, 30)

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

day_columns = [f"Day_{day}" for day in range(1, 31)]

# Convert the reshaped data into a Pandas DataFrame.
telecom_df = pd.DataFrame(telecom_usage_12x30, index=months, columns=day_columns)

# Add a monthly total column to summarize usage.
telecom_df["Monthly_Total"] = telecom_df.sum(axis=1)

print("Telecom usage array shape:", telecom_usage_360.shape)
print("Reshaped telecom dataset shape:", telecom_usage_12x30.shape)
print("\nTelecom DataFrame preview:")
print(telecom_df.head())

print("\nMonthly totals:")
print(telecom_df["Monthly_Total"])

# Plot the monthly totals using a line graph.
plt.figure(figsize=(10, 5))
plt.plot(
    telecom_df.index,
    telecom_df["Monthly_Total"],
    marker="o",
    linewidth=2,
    color="teal",
)
plt.title("Monthly Telecom Usage Total")
plt.xlabel("Month")
plt.ylabel("Total Usage")
plt.xticks(rotation=45)
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.show()
