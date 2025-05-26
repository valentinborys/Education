cars = {
    "Toyota": {
        "model": "Corolla",
        "year": 2020,
        "color": "blue",
        "price": 20000
    },
    "Honda": {
        "model": "Civic",
        "year": 2019,
        "color": "red",
        "price": 22000
    },
    "Ford": {
        "model": "Mustang",
        "year": 2021,
        "color": "black",
        "price": 35000
    }
}


print("Введіть марку автомобіля:")
marka = input()
found = False

for car, info in cars.items():
    if car == marka:
        found = True
        model = info["model"]
        year = info["year"]
        color = info["color"]
        price = info["price"]

        print(f"Модель выбранного автомобиля: {model}")
        print(f"Год выбранного автомобиля: {year} год")
        print(f"Цвет выбранного автомобиля: {color}")
        print(f"Цена выбранного автомобиля: {price}$")

if found == False:
    print("Выбранной марки авто нет")