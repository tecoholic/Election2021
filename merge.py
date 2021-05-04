import os
import pandas as pd

base_dir = os.path.join("may2021", "TN")

df = None


def get_code(party):
    parts = party.split(" ")
    return "".join(p[0] for p in parts).upper()


for i in range(1, 235):
    filename = os.path.join(base_dir, f"{i}.csv")

    data = pd.read_csv(filename)
    data["AC_NO"] = i
    data["Position"] = data["Total Votes"].rank(ascending=False).astype('int')
    data["Party Code"] = data["Party"].apply(get_code)

    if df is None:
        df = data
    else:
        df = df.append(data)

fname = os.path.join(base_dir, "all_candidate.csv")
df.to_csv(fname, index=False)
