data = (1, 2, 3, 4, 5)

def add_to_touple(data):
    new_list = list(data)
    new_list.append(6)
    return tuple(new_list)

print(add_to_touple(data))