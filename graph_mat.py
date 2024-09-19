import pandas as pd
import matplotlib.pyplot as plt

# читаем данные из CSV-файла
data = pd.read_csv('data.csv')

# достаем наши значения
labels = data['label']
values = data['value']

# создаем сам график и цветовую палитру
plt.figure(figsize=(12, 7))
color = ['g', 'c', 'r', 'y', 'm']

# используем стиль для графика
plt.style.use('classic')

# строим гистограмму с доп. данными
bars = plt.bar(labels, values, color=color, alpha=0.75, edgecolor='black', linewidth=1.5)

# добавляем проценты над стобами
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), ha='center', va='bottom', fontsize=12)

# выводим надписи и размеры шрифта
plt.xlabel('Районы', fontsize=14)
plt.ylabel('Проценты', fontsize=14)
plt.title('Количество СОЧ по районам', fontsize=16)
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle=':', alpha=0.5)

# показываем график
plt.tight_layout()
plt.show()

