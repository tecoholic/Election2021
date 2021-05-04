import pandas as pd

filepath = "may2021/TN/all_candidate.csv"

data = pd.read_csv(filepath)

winners = data[data["Position"] == 1]

winners.to_csv("winners.csv", index=False)
