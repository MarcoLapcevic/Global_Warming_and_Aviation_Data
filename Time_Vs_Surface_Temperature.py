# Necessary modules, libraries, and packages...etc.
import pandas as pd
# import numpy as np <----------------
import matplotlib.pyplot as plt
import seaborn as sns

# Cleaning the data on the dataset:

# Load the CSV file
df = pd.read_csv("./datasets/Global_Surface_Temperature_Anomolies.csv")

# Make dataframe contain only year and yearly average anomoly
df = df[["Year", "J-D"]]
df = df.loc[df["Year"] >= 1980, ["Year", "J-D"]].copy()

plt.figure(figsize=(12, 6))
sns.lineplot(x="Year", y="J-D", data=df, color='teal')
plt.xlabel("Time (Years)", fontname='Times New Roman',
           fontsize=12)
plt.ylabel("Land-Ocean Temperature Index", fontname='Times New Roman',
           fontsize=12)
plt.title("Surface Temperature Anomoly by Year", fontname='Monospace',
          fontsize=18)
plt.grid(True)
plt.tight_layout()
plt.plot(df["Year"], df["J-D"])