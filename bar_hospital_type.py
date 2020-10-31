import plotly.express as px
import pandas as pd

df = pd.read_csv('admissions_averages_type.csv')

df = df.drop('Total', axis=1)

df = df.melt(id_vars='Week Commencing', value_name='Hospitalisations', var_name='Hospital Type')

df = df.round({'Hospitalisations': 0})

fig = px.bar(df,
             x='Hospitalisations',
             y='Hospital Type',
             animation_frame='Week Commencing',
             orientation='h',
             range_x=[0, 5600],
             template='seaborn',
             color='Hospital Type',
             title='Chart 2: Average Number of Hospitalisations by Hospital Type'
             )
fig.update_layout(transition={'duration':1})
fig.write_html('bar_race.html')
fig.show()
