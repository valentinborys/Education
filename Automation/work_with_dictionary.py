cities = {
    "New York": {
        "country": "USA",
        "population": 8399000,
        "famous_landmarks": ["Statue of Liberty", "Empire State Building", "Central Park"]
    },
    "Paris": {
        "country": "France",
        "population": 2141000,
        "famous_landmarks": ["Eiffel Tower", "Louvre Museum", "Notre-Dame Cathedral"]
    },
    "Tokyo": {
        "country": "Japan",
        "population": 13960000,
        "famous_landmarks": ["Tokyo Tower", "Shibuya Crossing", "Senso-ji Temple"]
    }
}

print("Введіть назву вашого міста:")
city_name = input()

for city, info in cities.items():
    if city_name == city:
        country = info["country"]
        population = info["population"]
        famous_landmarks = info["famous_landmarks"]

        print(f"Країна: {country}")
        print(f"Населення: {population}")
        print("Популярні місця:")

        for landmark in famous_landmarks:
            print(f"- {landmark}")
        break
else:
    print("Місто не знайдено")
