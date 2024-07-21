# Додавання елементу до кортежу
set1 = {1, 2, 3}
x = 4
set1.add(x)
print("Додавання елементу до кортежу:", set1)


# Видалення елементу з множини
set1 = {1, 2, 3}
set1.remove(3)
print("Видалення елементу з множини:", set1)


# Поєднання множин
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = set1 | set2
print("Поєднання множин:", set3)


# Перетин множини
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = set1.intersection(set2)
print("Перетин множин", set3)


# Difference множини
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = set2.difference(set1)
print("Difference множини", set3)
