x = input("Введіть значення для обчислення: ")

try:
    result = eval(x)
    print("Результат обчислення:", result)
except Exception as error:
    print("Помилка: ", error)