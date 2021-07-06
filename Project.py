import pandas as pd 
import plotly.figure_factory as ff
df = pd.read_csv('prodata.csv')
graph = ff.create_distplot([df['Rating'].tolist()],['Rating'])
graph.show()