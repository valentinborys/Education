from Demos.SystemParametersInfo import new_w
from numpy.ma.core import repeat


def test_1():
    variable1 = [1, 2, 3]
    variable2 = variable1
    variable1[0] = 100
    variable2[1] = 20
    variable3=variable2
    variable3[2] = 300
    variable4 = variable3.append(4)
    print(variable1, variable2, variable3)


def test_2():
    variable1 = {1, 2, 3, 2, 3, 1, 5}
    print(variable1)


def test_3():

    results = [
        "passed",
        "failed",
        "passed",
        "skipped",
        "failed",
        "passed",
        "failed"
    ]

    counts = {}
    for result in results:
        if result in counts:
            counts[result] += 1
        else:
            counts[result] = 1
    return print(counts)


def test_find_duplicates():
    ids = [101, 102, 101, 103, 102, 104, 101]

    seen = []
    duplicates = []

    for id in ids:
        if id in seen:
            if id not in duplicates:
                duplicates.append(id)
        else:
            seen.append(id)

    print(duplicates)


def test_find_duplicates_2():
    ids = [101, 102, 101, 103, 102, 104, 101]
    duplicates = []

    for i in ids:
        if ids.count(i)>1 and i not in duplicates:
            duplicates.append(i)

    print(duplicates)


def test_find_unique():
    numbers = [1, 2, 3, 2, 4, 1, 5, 3, 6]
    uniq = []

    for i in numbers:
        if numbers.count(i)<=1:
            uniq.append(i)

    print(uniq)

def test_find_duplicates_names():
    names = ["Alex", "Bob", "Alex", "Mike", "Bob", "Kate", "Alex"]
    uniq = []

    for i in names:
        if names.count(i)>1 and i not in uniq:
            uniq.append(i)
    print(uniq)

def test_reverse():
    text = "automation"
    text_reverse = text[::-1]
    print(text_reverse)

def test_palindrome():
    text = "Level".lower()
    text_rev = text[::-1]

    if text_rev == text:
        print("palindrome")
    else:
        print("String is not palindrome")

def test_count_vowels():
    text = "automation"
    vowels = "aeiou"
    count_vowels = 0

    for i in text:
        if i in vowels:
            count_vowels += 1

    print(count_vowels)

def test_remove_spaces():
    text = "hello world python"
    text_new = text.replace(" ", "")
    print(text_new)

def test_count_char():
    text = "automation"
    char = "a"
    count = 0

    for i in text:
        if char == i:
            count +=1

    print(count)

def test_capitalize():
    text = "python automation"
    upper = text[0].upper()
    new_text = text.replace(text[0], upper)
    print(new_text)

def test_longest_word():
    text = "python is great for automation"
    array_text = text.split(" ")
    count = 0

    for i in array_text:
        if len(i) > count:
            count = len(i)

    print(count)

def test_longest_third():
    text = "python is great for automation"
    array_text = text.split(" ")
    max_word = len(max(array_text, key=len))
    print(max_word)

def test_even_number():
    number = 42
    if number % 2 == 0:
        print(True)

def test_sum_digits():
    number = 123456
    string = str(number)
    summ = 0
    for i in string:
        summ += int(i)

    print(summ)

def test_replace_char():
    text = "hello world"
    y = text.replace("o", "0")
    print(y)

def test_anagram():
    text1 = "liSten n".replace(" ", "").lower()
    text2 = "silent N".replace(" ", "").lower()

    checker = []

    for t_1 in text1:
        checker.append(t_1)

    for t_2 in text2:
        if t_2 in checker:
            checker.remove(t_2)
        else:
            return False

    if not checker:
        print(True)
        return True
    else:
        print(False)
        return False


def test_anagram_2():
    text1 = "listen"
    text2 = "silent"

    sort_text1 = sorted(text1)
    sort_text2 = sorted(text2)

    if sort_text1 == sort_text2:
        print(True)
    else:
        print(False)

def test_big_char():
    numbers = [13, 12, 10, 5, 8, 10, 3, 8, 7]
    x = list(set(sorted(numbers)))
    print(x[-2])



def test_char_list():
    numbers = [4, 2, 7, 2, 9, 2, 4, 7, 7, 7, 1]

    rep = 0
    char = 0

    for i in numbers:
        x = numbers.count(i)
        if x > rep:
            rep = x
            char = i

    print(char)


def test_char_list_2():
    numbers = [4, 2, 7, 2, 9, 2, 4, 7, 7, 7, 1]
    print(max(set(numbers), key=numbers.count))


def test_char_dict():
    numbers = [4, 2, 7, 2, 9, 2, 4, 7, 7, 7, 1]

    counts = {}

    for i in numbers:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1

    rep = 0
    char = 0

    for k, v in counts.items():
        if v>rep:
            rep = v
            char = k

    print(char)

    print(counts)


def test_double():
    numbers = [4, 2, 7, 2, 9, 2, 4, 7, 7, 7, 1]
    new_list = []

    for i in numbers:
        if i not in new_list:
            new_list.append(i)

    print(new_list)

def test_double_set():
    numbers = [4, 2, 7, 2, 9, 2, 4, 7, 7, 7, 1]
    new_list = set(numbers)
    print(new_list)


def test_sum_index():
    numbers = [2, 12, 56, 7, 11, 15]
    x = 9

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i]+numbers[j] == x:
                print(f"Index first element: {i}, index second element: {j}")


def test_sum_index_2():
    numbers = [2, 12, 56, 7, 11, 15]
    x = 9
    summ =0

    for index, value in enumerate(numbers):
        summ+= value
        if summ>x:
            print(index)

    print(summ)

def test_same_number():
    numbers = [62, 12, 56, 7, 12, 15, 2]

    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] == numbers[j]:
              print(f"The same numbers was found, indexes: {i} and {j}. "
                    f"Same number is: {numbers[i]}")


def test_same_numbers():
    numbers = [62, 12, 56, 7, 12, 15, 2, 12, 12]
    indexes = []
    numbers_all = []

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] == numbers[j]:
                if i not in indexes:
                    indexes.append(i)
                if numbers[i] not in numbers_all:
                    numbers_all.append(numbers[i])

    # ind = set(indexes)
    # num = set(numbers_all)

    print(indexes, numbers_all)


def test_duplicates():
    numbers = [4, 7, 2, 7, 9, 4, 12, 7, 2]
    duplicates = []

    for i in numbers:
        if numbers.count(i) > 1:
            if numbers[i] not in duplicates:
                duplicates.append(numbers[i])

    for i in duplicates:
        print(i)


def test_unique_number():
    numbers = [4, 7, 2, 7, 9, 4, 12, 7, 2]

    for i in numbers:
        if numbers.count(i)==1:
            print(i)
            return


def test_second_largest():
    numbers = [10, 5, 8, 10, 3, 8, 7]
    uniq_num = []

    for i in numbers:
        if i not in uniq_num:
            uniq_num.append(i)

    biggest = max(uniq_num)
    uniq_num.remove(biggest)
    new_biggest = max(uniq_num)

    print(new_biggest)


def test_two_sum():
    numbers = [12, 7, 11, 2, 15]
    target = 9

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i]+numbers[j] == target:
                print(i, j)
                return


def test_longest_word_list():
    text = "python is great for automation"
    words_list = text.split(" ")

    longest = 0
    longest_word = ""

    for i in words_list:
        if longest < len(i):
            longest = len(i)
            longest_word = i

    print(longest_word)


def test_char_count():
    text = "automation"
    chars = {}

    for i in text:
        chars[i] = 0

    for i in text:
        chars[i] += 1

    print(chars)