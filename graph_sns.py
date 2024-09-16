import seaborn as sns
import matplotlib.pyplot as plt

# Данные
labels = ['Иваново', 'Кохма', 'Шуя', 'Лежнево', 'Савино']
values = [11.76, 5.88, 35.29, 23.53, 23.53]

# Настройка стиля Seaborn
sns.set(style="darkgrid")

# Создание графика
plt.figure(figsize=(10, 6))
barplot = sns.barplot(x=labels, y=values, palette='colorblind', edgecolor='black')

# Настройка заголовка и меток
plt.title('Данные по городам', fontsize=16, fontweight='bold')
plt.xlabel('Города', fontsize=14, fontweight='bold')
plt.ylabel('Значения', fontsize=14)
plt.xticks(rotation=15, fontsize=12)

# Показать график
plt.tight_layout()  # Автоматическая подстройка параметров
plt.show()