import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv(r"C:\Users\Mokitha\OneDrive\Desktop\Data Science\Task 4\output.csv")

# Basic info
print("Dataset Info:\n", df.info())
print("\nFirst 5 rows:\n", df.head())

# Drop rows with missing population
df_clean = df.dropna(subset=['Historical_Population'])

# Calculate deaths per 100,000 people
df_clean['Deaths_per_100k'] = (df_clean['Deaths'] / df_clean['Historical_Population']) * 100000

# Plot trend of total deaths over years (aggregated globally)
global_trend = df.groupby('Year')['Deaths'].sum().reset_index()
plt.figure(figsize=(10, 5))
sns.lineplot(data=global_trend, x='Year', y='Deaths')
plt.title("Global Traffic Deaths Over Time")
plt.xlabel("Year")
plt.ylabel("Total Deaths")
plt.grid(True)
plt.tight_layout()
plt.savefig("global_trend.png")
plt.show()

# Top 5 countries with highest average deaths per 100k
avg_deaths = df_clean.groupby('Entity')['Deaths_per_100k'].mean().sort_values(ascending=False).head(5)
print("\nTop 5 Countries by Average Deaths per 100,000 People:")
print(avg_deaths)

# Visualize those top 5 countries over time
top_countries = avg_deaths.index.tolist()
df_top = df_clean[df_clean['Entity'].isin(top_countries)]

plt.figure(figsize=(12, 6))
sns.lineplot(data=df_top, x='Year', y='Deaths_per_100k', hue='Entity')
plt.title("Traffic Deaths per 100,000 People (Top 5 Countries)")
plt.xlabel("Year")
plt.ylabel("Deaths per 100,000")
plt.legend(title="Country")
plt.grid(True)
plt.tight_layout()
plt.savefig("top5_trend.png")
plt.show()