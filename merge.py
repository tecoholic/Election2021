import os
import pandas as pd

states = {
    "AS": 126,
    "KL": 140,
    "PY": 30,
    "TN": 234,
    "WB": 294
}


def get_code(party):
    if party.lower() == "none of the above":
        return "NOTA"
    party = party.replace("of ", "")  # handle CPIM
    parts = party.split(" ")
    parts = [p.strip() for p in parts]
    return "".join(p[0] if not p.startswith("(") else p[0:2]+p[-1] for p in parts).upper()


def main():
    for state in states:
        print("Merging files of ", state)
        base_dir = os.path.join("may2021", state)
        df = None

        for i in range(1, states[state] + 1):
            filename = os.path.join(base_dir, f"{i}.csv")
            try:
                data = pd.read_csv(filename)
            except FileNotFoundError:
                print("Cannot find file: ", filename)
                continue

            data["AC_NO"] = i
            data["Position"] = data["Total Votes"].rank(
                ascending=False).astype('int')
            data["Party Code"] = data["Party"].apply(get_code)

            if df is None:
                df = data
            else:
                df = df.append(data)

        fname = os.path.join(base_dir, "all_candidate.csv")
        df.to_csv(fname, index=False)


if __name__ == "__main__":
    main()
