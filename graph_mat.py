import matplotlib.pyplot as plt
import matplotlib as mpl

# создаем стиль диаграммы
mpl.style.use(['classic'])

# прописываем данные диаграммы
labels = ['Иваново', 'Кохма', 'Шуя', 'Лежнево', 'Савино']
values = [11.76, 5.88, 35.29, 23.53, 23.53]

# делаем цветовую установку
colors = ['b','g','c','r','y']

# создаем сам график
fig1, ax1 = plt.subplots()
ax1.pie(values, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)

# делаем диаграмму круглой
ax1.axis('equal')

# заголовок диаграммы
plt.title('Количество СОЧ по муниципальным образованиям')

# добавляем легенду, чтобы ее левый верхний угол был сразу справа от диаграммы
plt.legend(loc='upper left', labels = labels, bbox_to_anchor=(0.90, 0.90))

# выводим диаграмму с оптимизацией
plt.tight_layout()
plt.show()