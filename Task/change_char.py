# string = str(input('Введіть текст: '))
# letter = str(input('Введіть символ який будемо змінювати: '))
# letter_to_change = str(input('Введіть символ на який будемо змінювати: '))
#
#
# def change_letter(string, letter, letter_to_change):
#     upd_string = string.replace(letter, letter_to_change)
#     return 'Змінений текст: ' + upd_string
#
# print(change_letter(string, letter, letter_to_change))

tuple1 = ('123', 1, 2, 3, 5, 'fox', 'fox', 'fox')

for i in tuple1:
    if i == 4.4:
        print(tuple1.index(i))


list2 = ['123', 1, 2, 3, 5, 'fox', 'fox', 'fox']
for i in list2:
    if i == 'fox':
        print(list2.index(i))

dictionary3 = {'test': 1, 'textik': 2}
print(dictionary3['test'])

my_set = {1, 2, 3, 3}
print(my_set)






