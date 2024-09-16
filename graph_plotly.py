import plotly.graph_objects as go

# прописываем данные графика
labels = ['Иваново', 'Кохма', 'Шуя', 'Лежнево', 'Савино']
values = [11.76, 5.88, 35.29, 23.53, 23.53]

# делаем цветовую установку
colors = ['b','g','c','r','y']

# создаем саму диаграмму
pie_chart = go.Figure(data=[go.Pie(
    labels=labels,
    values=values,
    marker=dict(colors=colors),
    hole=0.2,
    textinfo='label+percent',
    insidetextorientation='radial'
)])

#  делаем настройки диаграммы
pie_chart.update_layout(
    title_text='Количество СОЧ по муниципальным образованиям',
    title_x=0.5,
    annotations=[dict(text='Районы', x=0.5, y=0.5, font_size=20, showarrow=False)]
)

# выводим диаграмму
pie_chart.show()