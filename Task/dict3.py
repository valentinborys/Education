scores = {
    "math": 70,
    "physics": 80,
    "chemistry": 75
}

def diction(scores):
    for i in scores:
        scores[i] += 10
    return scores

print(diction(scores))
