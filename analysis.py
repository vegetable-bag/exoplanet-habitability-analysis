import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('../data/exoplanet_data.csv')

# Display basic info
print("Dataset Preview:\n")
print(df.head())

# --- Analysis 1: Flux vs Temperature ---
plt.figure()
plt.scatter(df['Flux_Earth'], df['Temperature_K'])

for i, planet in enumerate(df['Planet']):
    plt.text(df['Flux_Earth'][i], df['Temperature_K'][i], planet, fontsize=8)

plt.xlabel("Stellar Flux (Earth = 1)")
plt.ylabel("Temperature (K)")
plt.title("Flux vs Temperature Relationship")

plt.savefig('../results/flux_vs_temp.png')
plt.close()

# --- Analysis 2: Distance vs Temperature ---
plt.figure()
plt.scatter(df['Distance_AU'], df['Temperature_K'])

for i, planet in enumerate(df['Planet']):
    plt.text(df['Distance_AU'][i], df['Temperature_K'][i], planet, fontsize=8)

plt.xlabel("Distance (AU)")
plt.ylabel("Temperature (K)")
plt.title("Distance vs Temperature Relationship")

plt.savefig('../results/distance_vs_temp.png')
plt.close()

# --- Basic Insight ---
avg_temp = df['Temperature_K'].mean()
print(f"\nAverage Temperature of Dataset: {avg_temp:.2f} K")

# Habitability Filter
habitable = df[(df['Temperature_K'] >= 273) & (df['Temperature_K'] <= 373)]

print("\nPotentially Habitable Planets:\n")
print(habitable[['Planet', 'Temperature_K']])
