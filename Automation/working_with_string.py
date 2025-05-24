# Часть 1: Создание кортежей и доступ к элементам

my_tuple = ("apple", "  banana   ", "cherry ")
print("Удаление пробелов между словами:", my_tuple[1].strip())


# Часть 2: Срезы кортежей

numbers = tuple(range(1, 11))
print("\nСоздание кортежа через range:", numbers)
print("Вывод пяти первых элементов кортежа", numbers[:5])
print("Вывод группы", numbers[3:7])


# Часть 3: Функции кортежей

mixed_tuple = (2, "hello", 4.2, "Test")
print("\nДовжина кортежу:", len(mixed_tuple))

if "hello" in mixed_tuple:
    print("Строка в кортежі є")
else:
    print("\nСтроки в кортежі немає")


# Часть 4: удаление элемента с кортежа

_tuple = (2, "hello", 4.2, "Test", "123", 1)

print("Основной кортеж:", _tuple)

deleted_index = list(_tuple[:]) # Преобразованный кортеж в list
updeted_list = deleted_index.remove("Test") # Удаление с листа элемента
updeted_tuple = tuple(deleted_index) # Преобразование листа в кортеж
print("Обновленный кортеж:", updeted_tuple)
