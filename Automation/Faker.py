from faker import Faker
fake = Faker()

password = fake.password(length=10)
mail = fake.email()

print(password)
print(mail)