names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

diction = {}

def create_dictionary(names, scores):
    return dict(zip(names, scores))

print (create_dictionary(names, scores))