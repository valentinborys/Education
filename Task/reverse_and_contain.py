fruits = ["apple", "banana", "cherry", "pipa", "Xrry", "Test", "Tetu", "TaTa", "Atatat"]
fruits.reverse()

for element in fruits:
    rev_element = element[::-1]
    if "a" in rev_element:
        print(rev_element)
