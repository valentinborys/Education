
def test_list():
    a = ['A', 2, True, False, 1.1, 0, {}, {'id': 777}]
    filtered_items = [item for item in a if item]
    print(filtered_items)
