monthly = {
    "january": 1200,
    "february": 1200,
    "march": 1200,
    "april": 1200,
    "may": 1200,
    "june": 1200,
    "july": 1200,
    "august": 1200,
    "september": 1200,
    "october": 1200,
    "november": 1200,
    "december": 1200
}

def abandoned_now(dictionary, now):
    sum1 = []
    for i in monthly:
        if monthly == now:
            return sum1
        else:
            for x in monthly.values():
                sum1.append(x)

    return sum1


