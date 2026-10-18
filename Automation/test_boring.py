
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


def test_first_count():
    numbers = [4, 7, 2, 7, 9, 4, 12, 7, 2]
    duplicate = []

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] == numbers[j]:
                if numbers[i] not in duplicate:
                    duplicate.append(numbers[i])

    for i in range(len(numbers)):
        if numbers[i] not in duplicate:
            print(numbers[i])
            return


def test_first_count_dict():
    numbers = [4, 7, 2, 7, 9, 4, 12, 7, 2]
    counts = {}

    for i in numbers:
        if i not in counts:
            counts[i] = 0

    for i in numbers:
        counts[i] +=1

    for x in counts:
        if counts[x] == 1:
            print(x)
            return


def test_duplicate_1():
    numbers = [4, 7, 2, 7, 9, 4, 12, 7, 2]
    dupl = []

    for i in numbers:
        if numbers.count(i) > 1 and i not in dupl:
            dupl.append(i)

    print(dupl)

def test_duplicate_2():
    numbers = [4, 7, 2, 7, 9, 4, 12, 7, 2]
    dupl = []

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] == numbers[j] and numbers[i] not in dupl:
                dupl.append(numbers[i])
    print(dupl)


def test_first_repeat():
    numbers = [1, 5, 3, 8, 3, 5, 9, 3, 12]

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] == numbers[j]:
                print(numbers[i])
                return numbers[i]

def test_first_uniq():
    numbers = [5, 3, 8, 3, 5, 9, 3, 12]
    dupl = []

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] == numbers[j] and numbers[i]not in dupl:
                dupl.append(numbers[i])

    result = [i for i in numbers if i not in dupl]
    uniq = result[0]
    print(uniq)

def test_array_take_away():
    numbers_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    numbers_2 = [1, 2, 3, 4]

    new_arr = [i for i in numbers_1 if i %2==0]
    new_arr_2 = [i for i in numbers_1 if i not in numbers_2]

    print(new_arr_2)



def test_sort_second():
    numbers = [12, 5, 8, 12, 3, 9, 8, 10]
    new_arr = []

    for i in numbers:
        if i not in new_arr:
                new_arr.append(i)


def test_bubble_sort_second():
    numbers = [5, 2, 8, 1]

    for i in range(len(numbers)):
        for j in range(len(numbers)-1-i):
            if numbers[j] < numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

    print(numbers)

def test_bubble_sort_second_uniq():
    numbers = [12, 5, 8, 12, 3, 9, 8, 10]
    numbers_uniq = []

    for i in numbers:
        if i not in numbers_uniq:
            numbers_uniq.append(i)

    for i in range(len(numbers_uniq)):
        for j in range(len(numbers_uniq)-1-i):
            if numbers_uniq[j] < numbers_uniq[j+1]:
                numbers_uniq[j], numbers_uniq[j+1] = numbers_uniq[j+1], numbers_uniq[j]

    print(numbers_uniq[1])

def test_str():
    text = "automation"
    counter = {}

    for i in text:
        if i not in counter:
            counter[i] = 1
        else:
            counter[i] += 1

    print(counter)

def test_str_uniq():

    text = "aabbcddee"
    counter = {}

    for i in text:
        if i not in counter:
            counter[i] = 1
        else:
            counter[i] += 1

    for y in counter:
        if counter[y] == 1:
            print(y)
            return y

def test_target():

    numbers = [9, 45, 5, 81, 0]
    target = 9

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                print(i, j)
                return i, j


def test_second_bigger():
    numbers = [14, 7, 22, 14, 9, 22, 18, 3]
    numbers_uniq = []

    for i in numbers:
        if i not in numbers_uniq:
            numbers_uniq.append(i)

    for i in range(len(numbers_uniq)):
        for j in range(len(numbers_uniq)-1-i):
            if numbers_uniq[j]<numbers_uniq[j+1]:
                numbers_uniq[j], numbers_uniq[j+1] = numbers_uniq[j+1], numbers_uniq[j]

    print(numbers_uniq[1])
    return numbers_uniq[1]

def test_second_bigger_213():
    numbers = [14, 7, 22, 14, 9, 22, 18, 3]
    numbers_uniq = []
    max_char = 0
    new_max = 0

    for i in numbers:
        if i not in numbers_uniq:
            numbers_uniq.append(i)

    for i in numbers_uniq:
        if i > max_char:
            max_char = i

    numbers_uniq.remove(max_char)

    for i in numbers_uniq:
        if i > new_max:
            new_max = i

    return new_max



def test_first_char():
    numbers = [4, 7, 2, 7, 9, 4, 12, 7, 2]
    duplicate = []


    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] == numbers[j]:
                duplicate.append(numbers[i])

    new_arr = [i for i in numbers if i not in duplicate]

    print(new_arr[0])

def test_palindrome_():
    text = "level".lower()
    text_2 = text[::-1]

    if text_2 == text:
        print("It's string is palindrome")
        return True
    else:
        print("This string is not palindrome")
        return False

def test_longest_word_():
    text = "python is great for automation"
    text = text.split(" ")
    current_length = 0
    max_length = ""

    for i in text:
        longest = len(i)
        if longest > current_length:
            current_length = longest
            max_length = i

    print(f"The longest word is '{max_length}', length: '{current_length}'")
    return

def test_unique_values():
    list_1 = [1, 2, 3, 4, 5]
    list_2 = [3, 4, 5, 6, 7]

    for i in list_2:
        if i not in list_1:
            list_1.append(i)

    print(list_1)

def test_brackets():
    text = "(()())"
    correct = 0
    open_bracket = "("
    close_bracket = ")"

    for i in text:
        if i == open_bracket:
            correct +=1
        if i == close_bracket:
            correct -=1
    if correct < 0:
        return False
    else:
        return True


def test_find_missing_users():
    expected_users = [101, 102, 103, 104, 105, 106]
    actual_users = [102, 104, 105, 107]

    missing_users = [i for i in expected_users if i not in actual_users]
    return missing_users

def test_common_users():
    first_response = [12, 7, 11, 2, 15, 7]
    second_response = [7, 2, 20, 12, 30]

    common_users = []
    for i in first_response:
        if i in second_response and i not in common_users:
            common_users.append(i)

    print(common_users)
    return common_users

