#!/usr/bin/env python3

"""
This script takes the U.S.Presidents_Birth_and_Death_Information.csv and creates
a dataframe. It calcualtes how long each president has lived and outputs the
data into a formatted table. It also calculates the mean, weighted mean, media,
mode, max, and standard deviation of how many days each president has lived and
plots it into a bar graph.

"""

import pandas as pd
import matplotlib.pyplot as plt
import dataframe_image as dfi


# Read the csv file as the dataframe
presidents_df = pd.read_csv(
    "U.S.Presidents_Birth_and_Death_Information.csv", index_col=False
)


# Drop last row
presidents_df.drop(presidents_df.tail(1).index, inplace=True)


# Convert BIRTH DATE and DEATH DATE to datetime
presidents_df["BIRTH DATE"] = pd.to_datetime(presidents_df["BIRTH DATE"])
presidents_df["DEATH DATE"] = pd.to_datetime(presidents_df["DEATH DATE"])

year_of_birth = presidents_df["BIRTH DATE"].dt.year

lived_years = round(
    (presidents_df["DEATH DATE"] - presidents_df["BIRTH DATE"]).dt.days / 365, 1
)

lived_months = round(
    (presidents_df["DEATH DATE"] - presidents_df["BIRTH DATE"]).dt.days / 30.5, 1
)

lived_days = (presidents_df["DEATH DATE"] - presidents_df["BIRTH DATE"]).dt.days

presidents_df["LIVED YEARS"] = lived_years
presidents_df["LIVED MONTHS"] = lived_months
presidents_df["LIVED DAYS"] = lived_days

# Export the table as png
dfi.export(
    presidents_df.sort_values("LIVED YEARS", ascending=True)
    .head(10)
    .style.hide_index()
    .format(
        {"LIVED YEARS": "{:.1f}", "LIVED MONTHS": "{:.1f}", "LIVED DAYS": "{:.1f}"}
    ),
    "presidents_short_lived.png",
)

dfi.export(
    presidents_df.sort_values("LIVED YEARS", ascending=False)
    .head(10)
    .style.hide_index()
    .format(
        {"LIVED YEARS": "{:.1f}", "LIVED MONTHS": "{:.1f}", "LIVED DAYS": "{:.1f}"}
    ),
    "presidents_long_lived.png",
)


# Find mean
my_mean = presidents_df["LIVED DAYS"].mean()

# Find weighted mean
# Same as mean as every lived days value is unique?
my_weighted_mean = presidents_df["LIVED DAYS"].mean()

# Find meadian
my_median = presidents_df["LIVED DAYS"].median()

# Find mode
# No presidents lived the same number of days
my_mode = presidents_df["LIVED DAYS"].mode()[0]

# Find max
my_max = presidents_df["LIVED DAYS"].max()

# Find min
my_min = presidents_df["LIVED DAYS"].min()

# Find standard deviation
my_std = presidents_df["LIVED DAYS"].std()

# Create table with new data
calculations_data = {
    "MEAN": my_mean,
    "WEIGHTED MEAN": my_weighted_mean,
    "MEDIAN": my_median,
    "MODE": my_mode,
    "MAX": my_max,
    "MIN": my_min,
    "STANDARD DEVIATION": my_std,
}
calculations_df = pd.DataFrame(data=calculations_data, index=[0])


# Create bar graph and output it to .png
plot_data = [my_mean, my_weighted_mean, my_median, my_mode, my_max, my_min, my_std]
plt.figure(figsize=(10, 8))
plt.bar(
    ["MEAN", "WEIGHTED MEAN", "MEDIAN", "MODE", "MAX", "MIN", "STANDARD DEVIATION"],
    plot_data,
)
plt.savefig("bar_graph.png")
