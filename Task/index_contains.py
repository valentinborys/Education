fruits = ["apple", "banana", "cherry", "pipa", "Xrry", "Test", "Tetu", "TaTa", "Atatat"]
word_with_a = []

for index, word in enumerate(fruits):
    if word.__contains__("a"):
        word_with_a.append(word)

for x in word_with_a:
    print(x)

