import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


# 1. Створимо простий DataFrame
data = {
    'Площа_м2': [30, 40, 50, 60, 70, 80],
    'Ціна_тис_дол': [35, 50, 55, 65, 70, 85]
}
df = pd.DataFrame(data)

# 2. Візуалізуємо дані
plt.scatter(df['Площа_м2'], df['Ціна_тис_дол'], color='blue')
plt.xlabel('Площа (м2)')
plt.ylabel('Ціна (тис. $)')
plt.title('Залежність ціни від площі')
plt.grid(True)
plt.show()

# 3. Навчимо модель лінійної регресії
X = df[['Площа_м2']]  # ознаки
y = df['Ціна_тис_дол']  # ціль

model = LinearRegression()
model.fit(X, y)

# 4. Передбачимо ціну для квартири 75 м²
predicted_price = model.predict([[75]])
print(f'Прогнозована ціна для 75 м²: {predicted_price[0]:.2f} тис. $')

# ➕ Додатково: виведемо коефіцієнти моделі
coef = model.coef_[0]        # нахил (градієнт)
intercept = model.intercept_ # зсув (перетин)

print(f"Коефіцієнт (за кожен 1 м²): {coef:.2f} тис. $")
print(f"Базова ціна (при площі 0 м²): {intercept:.2f} тис. $")

# 5. Побудуємо лінію регресії
plt.scatter(X, y, color='blue')
plt.plot(X, model.predict(X), color='red', linewidth=2)
plt.xlabel('Площа (м2)')
plt.ylabel('Ціна (тис. $)')
plt.title('Лінійна регресія')
plt.grid(True)
plt.show()

