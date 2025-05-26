import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def test_test():
    # 1. Створимо простий DataFrame
    data = {
        'Швидкість_км_год': [30, 40, 50, 60, 70, 80, 90, 100],
        'Витрата_л_100км': [5.5, 6.0, 	6.5, 7.2, 8.0, 9.0, 10.5, 12.0]
    }
    df = pd.DataFrame(data)

    plt.scatter(df['Швидкість_км_год'], df['Витрата_л_100км'], color='green')
    plt.xlabel('Швидкість (км/год)')
    plt.ylabel('Витрата літрів на 100км')
    plt.title('Залежність витрати палива від від швидкості')
    plt.grid(True)
    plt.show()

    # Вчимо модель
    x = df[['Швидкість_км_год']]  # ознаки
    y = df['Витрата_л_100км']  # ціль

    model = LinearRegression()
    model.fit(x, y)

    predicted_price = model.predict([[75]])
    print(f'Прогнозована витрата палива при скорості для 75 км/год: {predicted_price[0]:.2f} тис. $')

    coef = model.coef_[0]
    intercept = model.intercept_

    print(f"Коефіцієнт (за кожен 1 м²): {coef:.2f} тис. $")
    print(f"Базова ціна (при площі 0 м²): {intercept:.2f} тис. $")

    plt.scatter(x, y, color='blue')
    plt.plot(x, model.predict(x), color='red', linewidth=2)
    plt.xlabel('Швидкість (км/год)')
    plt.ylabel('Витрата літрів на 100км')
    plt.title('Лінійна регресія')
    plt.grid(True)
    plt.show()






