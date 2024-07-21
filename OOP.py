# Визначення классу

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def model_display(self):
        return self.model

    def make_display(self):
        return self.make

    def year_display(self):
        return self.year


# Створення екземпляра класу
car = Car("Brr", "Audi", "2025")


# Звернення до свойств екщепляра
print(car)
print(car.make)
print(car.model)
print(car.year)
