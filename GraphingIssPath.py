import pandas as pd
import plotly.express as px

df = pd.read_csv("issLocations.txt")
fig = px.scatter_geo(df, lat="latitude", lon="longitude", title=f"Position of the iss, from {df['timestamp'].iloc[0]} to {df['timestamp'].iloc[-1]}")
fig.show()