import random
import datetime
from datetime import datetime

from decorators import my_decorate


def x(string):
    y = string[::-1]
    print(y)
    return y

x('Хелоу, мучачос')


def dev(*args):
    arr = [_ for _ in args if _ % 2 == 0]
    print(arr)
    return arr

dev(3, 4, 10, 11, 1034)


def filter_even(arr):
    y = [x for x in arr if x % 3 == 0]
    print(y)
    return arr

filter_even([1, 2, 3, 4, 5, 6])  # [2, 4, 6]


def create_matrix(weight, hight):
    matrix = []
    for _ in range(weight):
        row = random.sample(range(1, 10), hight)
        matrix.append(row)
    print(matrix)
    return matrix

create_matrix(2, 4)


def reverse_word(word):
    rev_world = word[::-1].replace("о", "OOO")
    print(rev_world)

reverse_word('Оклахома')


def is_palindrome(word):
    word = word.lower()
    rev_word = word[::-1].lower()
    x = [print("This worf is palindrome") if rev_word == word else print("This word isn't palindrome")]

is_palindrome('кок')
is_palindrome('Kok')
is_palindrome("Test")

def count_letters(world):
    arr = []
    for i, x in world:
        if i in arr:
            arr.append(i)
    print(arr)


def count_letter(word):
    result = {}
    for char in word:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    print(result)
    return result

count_letter("hhello")

def are_anagrams(word1):
    return sorted(word1)

print(are_anagrams('acbetd'))


def fizzbuzz(number):
    if number % 3 == 0 and number % 5 == 0:
        print('The number is divisible by 3 and 5')
        return number
    elif number % 3 == 0:
        print('The number is divisible by 3')
        return number
    elif number % 5 == 0:
        print('The number is divisible by 5')
        return number

fizzbuzz(15)


def gcd(num1, num2):
    min_number = min(num1, num2)
    x = []
    for i in range(1, min_number):
        if num1 % i  == 0 and num2 % i  == 0:
            x.append(i)
    print(max(x))
    return max(x)


gcd(24, 36)


def remove_duplicates(arr):
    uniq = set(arr)
    list_uniq = list(uniq)
    print(list_uniq)
    return list_uniq

remove_duplicates([1, 2, 2, 3, 1])


def char_frequency(word):
    x = {}
    for i in word:
        if i in x:
            x[i] += 1
        else:
            x[i] = 1
    print(x)

char_frequency("banana")


@my_decorate
def is_prime(num):
    all_dev = []
    for i in range(1, num):
        if num % i == 0:
            all_dev.append(i)
    if len(all_dev) <= 2:
        return True

    return False

is_prime(13)


def word_count(string):
    diction = {}
    arr = string.replace(', ', ' ').replace('! ', ' ').replace('.', '').lower().split(' ')
    for i in arr:
        if i in diction:
            diction[i] += 1
        else:
            diction[i] = 1
    print(diction)
    return diction
    # print(i)

word_count("Hello, world! Hello Python.")

def longest_word(string):
    x = string.replace("?", "").replace(", ", " ").replace("!", "").lower().split(" ")
    longest = []
    for i in x:
        longest.append(len(i))
    y = max(longest)
    print(y)
    return y

longest_word("В чащах юга жил-был цитрус? Да, но фальшивый экземпляр!")


def longest_word_2(string):
    x = string.replace("?", "").replace(", ", " ").replace("!", "").lower().split(" ")
    longest = 0
    for i in x:
        if len(i)>longest:
            longest = int(len(i))
    print(longest)
    return longest

longest_word_2("В чащах юга жил-был цитрус? Да, но фальшивый экземпляр!")
