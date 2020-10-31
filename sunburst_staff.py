import plotly.express as px
import pandas as pd

df = pd.read_csv('period_staff.csv')

df = df.melt(id_vars='week_commencing', value_name='Percentage of Staff', var_name='code')

df['iso_sick'] = df.apply(lambda row: 'Isolating' if ('iso' in row['code']) else 'Sick', axis=1)

df['staff type'] = df.apply(
    lambda row: 'Nursing Staff' if 'nursing' in row['code'] else 'Medical or Dental Staff' if 'medical' in row[
        'code'] else 'Other Staff', axis=1)

df = df.round({'Percentage of Staff': 1})

period_one = df.loc[df['week_commencing'] == 'Period One: 14/04/2020 to 08/06/2020']

period_two = df.loc[df['week_commencing'] == 'Period Two: 09/06/2020 to 03/08/2020']

period_three = df.loc[df['week_commencing'] == 'Period Three: 17/08/2020 to 19/10/2020']

fig1 = px.sunburst(period_one,
                   path=['iso_sick', 'staff type'],
                   template='seaborn',
                   values='Percentage of Staff',
                   title='Period One: 14/04/2020 to 08/06/2020')

fig1.write_html('sunburst_period_one.html')
fig1.show()

fig2 = px.sunburst(period_two,
                   path=['iso_sick', 'staff type'],
                   template='seaborn',
                   values='Percentage of Staff',
                   title='Period Two: 09/06/2020 to 03/08/2020')

fig2.write_html('sunburst_period_two.html')
fig2.show()

fig3 = px.sunburst(period_three,
                   path=['iso_sick', 'staff type'],
                   template='seaborn',
                   values='Percentage of Staff',
                   title='Period Three: 17/08/2020 to 19/10/2020')

fig3.write_html('sunburst_period_three.html')
fig3.show()