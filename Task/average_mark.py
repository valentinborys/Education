students = {
    "Anna": [80, 90, 85],
    "Ivan": [75, 70, 80],
    "Oksana": [90, 95, 100]
}

def names(student):
    name = []
    for i in students:
         name.append(i)

    return name

def marks(student):
    mark = []
    for i in students.values():
        quantity = len(i)
        summ = sum(i)
        av_mark = summ/quantity
        mark.append(av_mark)

    return mark

names = names(students)
marks = marks(students)

print(dict(zip(names, marks)))

