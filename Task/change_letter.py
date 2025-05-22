from dataclasses import replace

text = "Python is awesome"

replace_space = text.replace(" ", "_")
print(replace_space)


items = [1, 2, 2, 3, 1, 4, 3]
new_items = set()

for i in items:
    new_items.add(i)

print(new_items)

words = ["cat", "elephant", "dog", "hippo"]
less_word = [words[0]]

for i in words:

    if len(less_word[0])>len(i):
        less_word.clear()
        less_word.append(i)
print(less_word)

