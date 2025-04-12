# Necessary modules, libraries, and packages...etc.
import pandas as pd
# import numpy as np <----------------
import matplotlib.pyplot as plt
import seaborn as sns

# Cleaning the data on the dataset:



# Load the CSV file
df = pd.read_csv("./datasets/global_warming_turbulence_data.csv")

# Convert 'time' column to datetime format (adjust the column name if necessary):
df['Year'] = pd.to_datetime(df['Year'])

# Sort by time to make the plot accurate:
df = df.sort_values(by='Year')

# Plotting the dataset to output visualization:
plt.figure(figsize=(12, 6))
sns.lineplot(x='Year', y='Avg_Wind_Shear_mps_per_km', data=df, color='teal')
plt.title("Wind Speed Over Time")
plt.xlabel("Year")
plt.ylabel("Wind Speed")
plt.grid(True)
plt.tight_layout()
plt.show()

