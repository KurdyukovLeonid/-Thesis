import pandas as pd
import matplotlib.pyplot as plt

# данные
data = pd.read_csv('data.csv')
labels = data['label']
values = data['value']
color = ['g', 'c', 'r', 'y', 'm']


# Вертикальная столбчатая диаграмма
plt.figure(figsize=(12, 7))
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
plt.tight_layout()
plt.show()


# Линейный график
plt.figure(figsize=(12, 7))
plt.plot(labels, values, marker='o', color='b', linestyle='-', alpha=0.75)
plt.xlabel('Районы', fontsize=14)
plt.ylabel('Проценты', fontsize=14)
plt.title('Количество СОЧ по районам', fontsize=16)
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

# Круговая диаграмма
plt.figure(figsize=(10, 10))
plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=140, colors=color)
plt.title('Количество СОЧ по районам', fontsize=16)
plt.axis('equal')
plt.show()


# График с областями
plt.figure(figsize=(12, 7))
plt.fill_between(labels, values, color='skyblue', alpha=0.4)
plt.plot(labels, values, marker='o', color='b', alpha=0.75)
plt.xlabel('Районы', fontsize=14)
plt.ylabel('Проценты', fontsize=14)
plt.title('Количество СОЧ по районам', fontsize=16)
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()


# Горизонтальная столбчатая диаграмма
plt.figure(figsize=(12, 7))
bars = plt.barh(labels, values, color=color, alpha=0.75, edgecolor='black', linewidth=1.5)
for bar in bars:
    plt.text(bar.get_width(), bar.get_y() + bar.get_height()/2, round(bar.get_width(), 2),
             ha='left', va='center', fontsize=12)
plt.xlabel('Проценты', fontsize=14)
plt.ylabel('Районы', fontsize=14)
plt.title('Количество СОЧ по районам', fontsize=16)
plt.grid(axis='x', linestyle=':', alpha=0.5)
plt.tight_layout()
plt.show()