# Telecom Data Shape Fix using NumPy and Pandas

**Student Name:** ______________________________

**Register Number:** ______________________________

**Subject Name:** Data Science

**Faculty Name:** ______________________________

**College Name:** ______________________________

\newpage

# Abstract

This mini-project explains how NumPy and Pandas can be used to organize telecom usage data into a proper tabular form. In many real datasets, values may first appear as a long one-dimensional array, which is difficult to read and analyze. In this work, a telecom dataset with 360 values is created and then reshaped into a 12 x 30 structure to represent 12 months and 30 days. The project also shows how `concatenate()` can combine separate usage arrays into one complete dataset. After reshaping, the data is converted into a Pandas DataFrame for easier analysis. Monthly totals are calculated to understand network activity over time. Finally, a line graph is plotted to visualize changes in monthly usage in a simple and clear way.

# Problem Statement

Telecom companies collect a large amount of usage data every day from calls, messages, and internet activity. Sometimes this data is not stored in a clean table format and may appear as a long list of values. When the shape of the data is not correct, it becomes difficult to read, compare months, and find trends in network usage. Students and analysts need a simple method to fix the structure of this data before doing any meaningful analysis.

In this project, the telecom dataset starts as a one-dimensional array with 360 values. This raw structure is not easy to interpret because it does not clearly show monthly or daily usage. The task is to reshape the data into a proper 12 x 30 format, combine separate arrays, convert the result into a Pandas DataFrame, and calculate monthly totals. This makes the dataset ready for analysis and visualization.

# Objectives

- To create a telecom usage dataset with 360 values.
- To reshape the one-dimensional dataset into a 12 x 30 monthly structure using NumPy.
- To use `concatenate()` to merge multiple telecom usage arrays into a single dataset.
- To convert the reshaped data into a Pandas DataFrame for better readability.
- To calculate monthly usage totals for comparison.
- To visualize the monthly telecom trend using a Matplotlib line graph.
- To understand how data shape correction helps in real telecom data analysis.

# Tools and Technologies Used

- **Python** for writing and running the program.
- **NumPy** for array creation, reshaping, and concatenation.
- **Pandas** for tabular data handling and monthly total calculation.
- **Matplotlib** for plotting the line graph.
- **Jupyter Notebook / VS Code / Python IDLE** can be used to execute the program.
- **Microsoft Word** for final report preparation and formatting.

# Methodology

The first step in this project is to create a telecom usage dataset in NumPy. Two separate arrays are generated to represent different periods of telecom activity. This is done to show how raw data may come from multiple sources or time periods before being joined together. Each array contains 180 values, and after combining them, the final dataset contains 360 values.

The second step is data shape correction. The 360-value array is reshaped into a 12 x 30 array using the `reshape()` function. In this structure, each row represents one month and each column represents one day. This makes the data much easier to understand compared to the original one-dimensional form.

The third step is combining data with `concatenate()`. Instead of directly creating a single large array, two arrays are first prepared and then merged. This reflects a practical telecom scenario where data can arrive from two different periods, systems, or network zones. Concatenation helps create one continuous dataset for analysis.

The fourth step is conversion into a Pandas DataFrame. After reshaping, the array is turned into a labeled table with month names as row labels and day numbers as column labels. This makes the output more readable and supports easy calculations. A new column called `Monthly_Total` is added by summing the daily usage values for each month.

The final step is visualization. The monthly totals are plotted using a line graph in Matplotlib. This graph helps identify low-usage and high-usage months in a quick visual form. The plotted output gives a simple picture of network load changes across the year.

# Implementation

The following Python code completes the full task of creating the telecom dataset, fixing the shape, converting it to a DataFrame, calculating totals, and plotting the final graph.

```python
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
```

**Suggested placement for screenshots in this section:**

- Insert **Screenshot 1** after the code block to show the program running in Python, Jupyter Notebook, or VS Code.
- Insert **Screenshot 2** below the console output to show the printed array shapes and DataFrame preview.

# Output and Visualization

When the code is executed, the first visible output shows the shape of the original array as `(360,)`. After that, the reshaped data appears with the shape `(12, 30)`, confirming that the data structure has been corrected successfully. A preview of the Pandas DataFrame is then displayed, where each row represents a month and each column represents a day.

The program also prints the `Monthly_Total` values for all 12 months. These totals help compare the level of telecom usage across the year. Because the second half of the dataset is generated with slightly higher values, the later months are expected to show heavier usage than the earlier months.

For the given sample run, the monthly totals are:

- January: 7523
- February: 7471
- March: 7448
- April: 7322
- May: 7692
- June: 7976
- July: 10593
- August: 10878
- September: 9990
- October: 10267
- November: 10244
- December: 10189

The final output is a line graph of monthly totals. The x-axis represents the months, and the y-axis represents total telecom usage. This graph makes it easy to identify which months have lower traffic and which months have higher network load.

**Suggested screenshot locations:**

- Insert **Screenshot 3** after the DataFrame preview to show the monthly table output.
- Insert **Screenshot 4** after the monthly totals list to show the summary values.
- Insert **Figure 1** in this section to display the line graph of monthly telecom usage.

**What screenshots to take from code output:**

- Screenshot of the Python editor or notebook containing the full code.
- Screenshot of console output showing `(360,)` and `(12, 30)` shapes.
- Screenshot of the DataFrame preview with month labels and day columns.
- Screenshot of the printed monthly totals.
- Screenshot of the final Matplotlib line graph.

# Analysis and Discussion

The reshaped dataset gives a much clearer view of telecom activity than the raw one-dimensional array. Once the data is arranged month-wise, it becomes easier to compare usage patterns and identify which parts of the year carry more network demand. The DataFrame format also improves readability because it adds proper labels for months and days.

From the monthly totals and line graph, the later months show higher usage when compared to the earlier months. This suggests that network traffic increases during the second half of the year in the sample dataset. In simple terms, the graph shows a stronger load on the telecom network as the months progress. In this output, **August** is the peak month with a total usage of **10878**, while **April** shows the lowest usage with **7322**. This difference helps explain when the network may experience maximum pressure and when demand is comparatively lighter.

This small project also shows why data shape is important in data science. If the shape is not correct, analysis can become confusing or even wrong. After correcting the shape, the data becomes suitable for aggregation, comparison, and visualization. This is a basic but important step in any real telecom analytics workflow.

# Conclusion

This project successfully demonstrates how NumPy and Pandas can be used to fix the shape of telecom data and prepare it for analysis. A 360-value telecom usage array was created, combined using `concatenate()`, reshaped into a 12 x 30 format, converted into a DataFrame, and analyzed through monthly totals and a line graph. The process shows that even simple shape correction can make raw data much more meaningful.

In the real world, telecom companies depend on properly structured data to monitor usage patterns, detect peak traffic periods, and optimize network performance. When monthly demand is identified clearly, service providers can improve capacity planning, reduce overload, and maintain better user experience. Therefore, this project gives a small but practical example of how data science supports telecom optimization.

# References

1. Wes McKinney, *Python for Data Analysis*. O'Reilly Media.
2. Travis E. Oliphant, *Guide to NumPy*. USA: Trelgol Publishing.
3. Jake VanderPlas, *Python Data Science Handbook*. O'Reilly Media.
4. Matplotlib Development Team. *Matplotlib Documentation*. Available in the official project documentation.
