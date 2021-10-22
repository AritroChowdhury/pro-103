import pandas as pd
import plotly.express as px 

df=pd.read_csv('Copy+of+data+-+data (3).csv')

fig=px.line(df, x='date', y='cases', color='country', title='cases')

fig=px.scatter(df, x='data', y='cases', size='percentage', color='country')

fig.show()