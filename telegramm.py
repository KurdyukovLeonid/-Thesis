import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
from io import BytesIO
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, InputFile
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes


TELEGRAM_TOKEN = 'здесь мой токен'

# читаем данные из CSV-файла
data = pd.read_csv('data.csv')

# достаем наши значения
labels = data['label']
values = data['value']

# создание графика на matplotlib с сохранением графика в png
def create_matplotlib_graph():
    plt.figure(figsize=(12, 7))
    color = ['g', 'c', 'r', 'y', 'm']
    plt.style.use('classic')
    bars = plt.bar(labels, values, color=color, alpha=0.75, edgecolor='black', linewidth=1.5)

    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), ha='center', va='bottom', fontsize=12)

    plt.xlabel('Районы', fontsize=14)
    plt.ylabel('Проценты', fontsize=14)
    plt.title('Количество СОЧ по районам', fontsize=16)
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle=':', alpha=0.5)

    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close()
    return buf


# # создание графика на seaborn с сохранением графика в png
def create_seaborn_graph():
    sns.set(style='whitegrid')
    plt.figure(figsize=(12, 7))
    bars = sns.barplot(x='label', y='value', data=data, palette='Set2', alpha=0.75)

    for bar in bars.patches:
        yval = bar.get_height()
        bars.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), ha='center', va='bottom', fontsize=12)

    bars.set_xlabel('Районы', fontsize=14)
    bars.set_ylabel('Проценты', fontsize=14)
    bars.set_title('Количество СОЧ по районам', fontsize=16)
    bars.set_xticklabels(bars.get_xticklabels(), rotation=45)

    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close()
    return buf


# # создание графика на plotly с сохранением графика в png
def create_plotly_graph():
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=labels,
        y=values,
        marker=dict(color=values, colorscale='Viridis', colorbar=dict(title='Проценты'), line=dict(width=1.5, color='black')),
        opacity=0.85,
        text=[round(value, 2) for value in values],
        textposition='auto',
        hoverinfo='text',
    ))

    fig.update_layout(
        title=dict(text='Количество СОЧ по районам', font=dict(size=24)),
        xaxis_title='Районы',
        yaxis_title='Проценты',
        xaxis_tickangle=-45,
        template='plotly_white',
        hovermode='closest',
        margin=dict(l=40, r=40, t=60, b=40)
    )

    buf = BytesIO()
    fig.write_image(buf, format='png')
    buf.seek(0)
    return buf

# создаем основные функции бота
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Информация о студенте", callback_data='student_info')],
        [InlineKeyboardButton("Дипломная работа", callback_data='diplom_work')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Здравствуйте, выберите действие:', reply_markup=reply_markup)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == 'student_info':
        await query.message.reply_text('Информация о студенте: Курдюков Леонид Андреевич, 13.10.1998 г.р., '
                                       'группа 3.10')
    elif query.data == 'diplom_work':
        keyboard = [
            [InlineKeyboardButton("Matplotlib", callback_data='matplotlib')],
            [InlineKeyboardButton("Seaborn", callback_data='seaborn')],
            [InlineKeyboardButton("Plotly", callback_data='plotly')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.message.reply_text('Здравстуйте, выберете на примере какой библиотеки '
                                       'вы бы хотели посмотреть график:', reply_markup=reply_markup)
    elif query.data == 'matplotlib':
        buf = create_matplotlib_graph()
        await query.message.reply_photo(photo=InputFile(buf, filename='matplotlib_graph.png'))
    elif query.data == 'seaborn':
        buf = create_seaborn_graph()
        await query.message.reply_photo(photo=InputFile(buf, filename='seaborn_graph.png'))
    elif query.data == 'plotly':
        buf = create_plotly_graph()
        await query.message.reply_photo(photo=InputFile(buf, filename='plotly_graph.png'))

# запускаем бота
if __name__ == '__main__':
    application = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))
    application.run_polling()