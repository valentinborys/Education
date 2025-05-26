data = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']

result = {}

for fruit in data:
    if fruit in result:
        result[fruit] += 1
    else:
        result[fruit] = 1

print(result)
