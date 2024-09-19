import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# читаем данные из CSV-файла
data = pd.read_csv('data.csv')

# используем стиль для графика
sns.set(style='whitegrid')

# создаем сам график с доп. данными
plt.figure(figsize=(12, 7))
bars = sns.barplot(x='label', y='value', data=data, palette='Set2', alpha=0.75)

# добавляем проценты над столбами
for bar in bars.patches:
    yval = bar.get_height()
    bars.text(bar.get_x() + bar.get_width()/2,
               yval,
               round(yval, 2),
               ha='center', va='bottom', fontsize=12)

# выводим надписи и размеры шрифта
bars.set_xlabel('Районы', fontsize=14)
bars.set_ylabel('Проценты', fontsize=14)
bars.set_title('Количество СОЧ по районам', fontsize=16)
bars.set_xticklabels(bars.get_xticklabels(), rotation=45)

# показываем график
plt.tight_layout()
plt.show()