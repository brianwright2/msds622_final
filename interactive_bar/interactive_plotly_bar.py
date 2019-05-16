import pandas as pd
import numpy as np
import scipy as sp
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.figure_factory as ff


plotly.tools.set_credentials_file(username='jacquessham', api_key='14bH20sYKUAguWvoXoQu')

df = pd.read_csv("wine_w_sentiment_and_metadata.csv")

data = [go.Bar(x=['Africa','Asia','Australia','Europe','North America','South America'],
            y=df.groupby('continent').price.agg(['mean']))]

py.iplot(data, filename='my_index')
