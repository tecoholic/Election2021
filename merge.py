import os
import pandas as pd


def get_symbol(full):
    parts = full.split(" ")
    return "".join(p[0] for p in parts).upper()


df = None
for i in range(1, 235):
    fname = os.path.join("may2021", "TN", f"{i}.csv")
    data = pd.read_csv(fname)
    data["AC_NO"] = i
    data["Position"] = data["Total Votes"].rank(ascending=False).astype('int')
    data["Party Code"] = data["Party"].apply(get_symbol)
    if df is None:
        df = data
    else:
        df = df.append(data)

df.to_csv(os.path.join("may2021", "TN", "all_candidate.csv"), index=False)
