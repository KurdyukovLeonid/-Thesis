import seaborn as sns
import matplotlib.pyplot as plt

# прописываем данные графика
labels = ['Иваново', 'Кохма', 'Шуя', 'Лежнево', 'Савино']
values = [11.76, 5.88, 35.29, 23.53, 23.53]

# настраиваем стиль
sns.set(style="darkgrid")

# создаем график
plt.figure(figsize=(10, 6))
barplot = sns.barplot(x=labels, y=values, palette='colorblind', edgecolor='black')

# делаем настройки графика
plt.title('Количество СОЧ по муниципальным образованиям', fontsize=16, fontweight='bold')
plt.xlabel('Муниципальные образования', fontsize=14, fontweight='bold')
plt.ylabel('Проценты', fontsize=14)
plt.xticks(rotation=15, fontsize=12)

# выводим график
plt.tight_layout()
plt.show()