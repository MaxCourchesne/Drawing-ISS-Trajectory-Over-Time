import pandas as pd
import time



df = pd.read_json("http://api.open-notify.org/iss-now.json")
df["latitude"] = df.loc["latitude", "iss_position"]
df["longitude"] = df.loc["longitude", "iss_position"]
df.reset_index(inplace=True)
df = df.drop(["message", "index", "iss_position"], axis=1)
df = df.drop([df.index[1]])



for _ in range(10000):
    time.sleep(30)
    df = pd.read_json("http://api.open-notify.org/iss-now.json")
    df["latitude"] = df.loc["latitude", "iss_position"]
    df["longitude"] = df.loc["longitude", "iss_position"]
    df.reset_index(inplace=True)
    df = df.drop(["message", "index", "iss_position"], axis=1)
    df = df.drop([df.index[1]])

    try:
        data = pd.read_csv("issLocations.txt")
        data = data.append(df)
        data.to_csv("issLocations.txt", index=False)
    except:
        df.to_csv("issLocations.txt", index=False)
    print(df)
