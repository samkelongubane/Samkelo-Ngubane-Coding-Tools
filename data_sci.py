#My code is not able to load the dataset due to network issues where I am
import pandas as pd
import matplotlib.pyplot as plt

# Loading the dataset
url = "https://raw.githubusercontent.com/annlntv/sg_da/main/nba_2023_2024.csv"
try:
    df = pd.read_csv(url)
except Exception as e:
    print("Error loading dataset. Please download the file manually and update the file path.")
    exit()

# Defining the high scorers and other players
high_scorers = df[df["PTS"] >= 20]
other_players = df[df["PTS"] < 20]

# Metrics
metrics = ["FGA", "3PA", "FT", "AST", "TRB"]

# Computing the mean values
mean_high_scorers = high_scorers[metrics].mean()
mean_other_players = other_players[metrics].mean()

# Creating a bar plot
plt.figure(figsize=(8, 5))
plt.bar(metrics, mean_high_scorers, label="High Scorers", alpha=0.7)
plt.bar(metrics, mean_other_players, label="Other Players", alpha=0.7)

# Labels and title
plt.xlabel("Metrics")
plt.ylabel("Mean Value")
plt.title("Comparison of Key Metrics")
plt.legend()
plt.show()

