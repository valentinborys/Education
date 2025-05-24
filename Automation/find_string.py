main_string = "Это строка, в которой мы будем искать подстроку."

sub_string = "которой"

index = main_string.find(sub_string)

if index != -1:
    print("Подстрока найдена в позиции:", index)
else:
    print("Подстрока не найдена.")