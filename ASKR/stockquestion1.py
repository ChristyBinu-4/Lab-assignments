import plotly.graph_objects as go

import pandas as pd
from datetime import datetime

df = pd.read_csv('chart.csv')
print(df.copy())

# fig = go.Figure(data=[go.Candlestick(x=df['DateTime'],open=df['TATAMOTORSEQN'],close=['TATAMOTORSEQN'], high=['TATAMOTORSEQN'], low=['TATAMOTORSEQN'])])

# fig.show()