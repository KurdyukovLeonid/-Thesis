import pandas as pd
import plotly.graph_objects as go

# данные
data = pd.read_csv('data.csv')
labels = data['label']
values = data['value']

# Вертикальная столбчатая диаграмма
fig = go.Figure()
fig.add_trace(go.Bar(
    x=labels,
    y=values,
    marker=dict(
        color=values,
        colorscale='Viridis',
        colorbar=dict(title='Проценты'),
        line=dict(width=1.5, color='black'),),
    opacity=0.85,
    text=[round(value, 2) for value in values],
    textposition='auto',
    hoverinfo='text',))
fig.update_layout(
    title=dict(
        text='Количество СОЧ по районам',
        font=dict(size=24)),
    xaxis_title='Районы',
    yaxis_title='Проценты',
    xaxis_tickangle=-45,
    template='plotly_white',
    hovermode='closest',
    margin=dict(l=40, r=40, t=60, b=40))
fig.show()

# Линейный график
line_fig = go.Figure()
line_fig.add_trace(go.Scatter(
    x=labels,
    y=values,
    mode='lines+markers',
    name='Значения',
    line=dict(color='blue', width=3),
    marker=dict(size=8)))
line_fig.update_layout(
    title='Количество СОЧ по районам',
    xaxis_title='Районы',
    yaxis_title='Проценты',
    xaxis_tickangle=-45,
    template='plotly_white',
    margin=dict(l=40, r=40, t=60, b=40))
line_fig.show()

# Круговая диаграмма
pie_fig = go.Figure()
pie_fig.add_trace(go.Pie(
    labels=labels,
    values=values,
    hole=0.3,
    textinfo='label+percent',
    title='Количество СОЧ по районам',))
pie_fig.update_layout(
    title='Количество СОЧ по районам',
    template='plotly_white')
pie_fig.show()


# График с областями
area_fig = go.Figure()
area_fig.add_trace(go.Scatter(
    x=labels,
    y=values,
    mode='lines',
    fill='tozeroy',
    name='Значения',
    line=dict(color='orange', width=3),))
area_fig.update_layout(
    title='Количество СОЧ по районам',
    xaxis_title='Районы',
    yaxis_title='Проценты',
    xaxis_tickangle=-45,
    template='plotly_white',
    margin=dict(l=40, r=40, t=60, b=40))
area_fig.show()

# Объединенный график
combined_fig = go.Figure()
combined_fig.add_trace(go.Bar(
    x=labels,
    y=values,
    name='Столбцы',
    marker=dict(color='lightblue'),
    text=[round(value, 2) for value in values],
    textposition='auto',))
combined_fig.add_trace(go.Scatter(
    x=labels,
    y=values,
    name='Линия',
    mode='lines+markers',
    line=dict(color='red', width=4)))
combined_fig.update_layout(
    title='Количество СОЧ по районам',
    xaxis_title='Районы',
    yaxis_title='Проценты',
    xaxis_tickangle=-45,
    template='plotly_white',
    margin=dict(l=40, r=40, t=60, b=40),)
combined_fig.show()