def count_unique_elements(lst):
    uniq = []
    for x in lst:
        if x not in uniq:
            uniq.append(x)
    return len(uniq)

print(count_unique_elements([1, 3, 4, 5, 5, 3, 99]))