prices = {
    "apple": 10,
    "banana": 7,
    "orange": 12,
    "kiwi": 15
}

x = []

for val in prices.values():
    x.append(val)

print('Максимальна ціна:', max(x))
print('Мінімальна ціна:', min(x))
