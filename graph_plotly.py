import pandas as pd
import plotly.graph_objects as go

# читаем данные из CSV-файла
data = pd.read_csv('data.csv')

# достаем наши значения
labels = data['label']
values = data['value']

# создаем интерактивный график
fig = go.Figure()

# добавляем столбцы с указанием градиента
fig.add_trace(go.Bar(
    x=labels,
    y=values,
    marker=dict(
        color=values,
        colorscale='Viridis',
        colorbar=dict(title='Проценты'),
        line=dict(width=1.5, color='black'),
    ),
    opacity=0.85,
    text=[round(value, 2) for value in values],
    textposition='auto',
    hoverinfo='text',
))

# выводим надписи и размеры шрифта
fig.update_layout(
    title=dict(
        text='Количество СОЧ по районам',
        font=dict(size=24)
    ),
    xaxis_title='Районы',
    yaxis_title='Проценты',
    xaxis_tickangle=-45,
    template='plotly_white',
    hovermode='closest',
    margin=dict(l=40, r=40, t=60, b=40)
)

# показываем график
fig.show()