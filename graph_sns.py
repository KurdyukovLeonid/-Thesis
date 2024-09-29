import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# данные
data = pd.read_csv('data.csv')

# Вертикальная столбчатая диаграмма
sns.set(style='whitegrid')
plt.figure(figsize=(12, 7))
bars = sns.barplot(x='label', y='value', data=data, palette='Set2', alpha=0.75)
for bar in bars.patches:
    yval = bar.get_height()
    bars.text(bar.get_x() + bar.get_width()/2,
               yval,
               round(yval, 2),
               ha='center', va='bottom', fontsize=12)
bars.set_xlabel('Районы', fontsize=14)
bars.set_ylabel('Проценты', fontsize=14)
bars.set_title('Количество СОЧ по районам', fontsize=16)
bars.set_xticklabels(bars.get_xticklabels(), rotation=45)
plt.tight_layout()
plt.show()


# Линейный график
plt.figure(figsize=(12, 7))
sns.lineplot(x='label', y='value', data=data, marker='o', palette='Set2')
plt.xticks(rotation=45)
plt.title('Количество СОЧ по районам', fontsize=16)
plt.xlabel('Районы', fontsize=14)
plt.ylabel('Проценты', fontsize=14)
plt.grid(True)
plt.tight_layout()
plt.show()


# Круговая диаграмма
plt.figure(figsize=(12, 7))
plt.pie(data['value'], labels=data['label'], autopct='%1.1f%%', startangle=140)
plt.title('Количество СОЧ по районам', fontsize=16)
plt.axis('equal')
plt.tight_layout()
plt.show()


# График распределения
plt.figure(figsize=(12, 7))
sns.histplot(data['value'], bins=10, kde=True, color='skyblue', alpha=0.75)
plt.title('Количество СОЧ по районам', fontsize=16)
plt.xlabel('Проценты', fontsize=14)
plt.ylabel('Частота', fontsize=14)
plt.grid(True)
plt.tight_layout()
plt.show()

# Тепловая карта
heat_data = data.pivot_table(index='label')
plt.figure(figsize=(12, 7))
sns.heatmap(heat_data, annot=True, cmap='coolwarm', cbar=True)
plt.title('Количество СОЧ по районам', fontsize=16)
plt.xlabel('Районы', fontsize=14)
plt.ylabel('Проценты', fontsize=14)
plt.tight_layout()
plt.show()