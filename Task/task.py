import random


def rep(text):
    text1 = text.replace("e", "x")
    print("Результат: " + text1)


rep("eeemoboy")


def fibonacci(x):
    a, b = 0, 1
    while a <= x:
        a, b = b, a + b

        print(a)


print(fibonacci(100))

x = [2, 4, 56, 345, 332, 23, 234, 23, 235, 67]
re = []
for y in x:
    if y % 3 == 0:
        re.append(y)

print(re)

b = "TEST, HOW ARE U?"
c = b.replace("TEST", "VALENTYN")

print(c)

s = [1, 7, 3, 4]
b = sorted(s)
print(b)

t = []
for b in range(0, 100):
    if b % 3 == 0:
        t.append(b)

print(random.sample(t, 3))
