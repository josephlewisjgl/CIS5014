import pandas as pd
import json
import plotly.express as px

df_admissions_covid = pd.read_csv('admissions_average.csv')

with open('Local_Health_Boards__April_2019__Boundaries_WA_BFE.geojson', 'r') as f:
    health_boards = json.load(f)

df_admissions_covid = df_admissions_covid.melt(id_vars='week_commencing', value_name='Number of Suspected/Confirmed COVID-19 Admissions',
                                               var_name='Health Board')

df_admissions_covid = df_admissions_covid.round({'Number of Suspected/Confirmed COVID-19 Admissions': 1})

df_admissions_covid = df_admissions_covid.rename(columns={
    'week_commencing' : 'Week Commencing'
})

fig = px.choropleth_mapbox(df_admissions_covid,
                           geojson=health_boards,
                           locations='Health Board',
                           color='Number of Suspected/Confirmed COVID-19 Admissions',
                           featureidkey="properties.lhb19nm",
                           color_continuous_scale="Reds",
                           mapbox_style="carto-positron",
                           zoom=6,
                           center={"lat": 52.1306607, "lon": -3.7837117},
                           opacity=0.5,
                           animation_frame='Week Commencing',
                           template='seaborn',
                           title='Chart 1: Number of Admissions with COVID-19 (Suspected and Confirmed) by Health Board '
                           )
fig.write_html('map_animation.html')
fig.show()