# 1. Вывод двух строк
print("Привет, Python!")
print("Приятно познакомиться!")

# 2a. Вывод «Эхо-оо-о-о!» 5 раз через пробел
print("Эхо-оо-о-о! " * 5)

# 2b. Вывод «Эхо-оо-о-о!» 5 раз через табуляцию
print("Эхо-оо-о-о!\t" * 5)

# 3. Признание в чувствах с сердечком
name_masha = "Маша"
name_petya = "Петя"
heart = "\u2661"
print(f"{name_masha} + {name_petya} = {heart}")

# 4. Чтение трех строк и их вывод
phrase1 = input()
phrase2 = input()
phrase3 = input()
print(phrase1)
print(phrase2)
print(phrase3)

# 5. Бронирование билета
film = input("Введите название фильма: ")
cinema = input("Введите название кинотеатра: ")
time = input("Введите время: ")
print(f'Билет в "{cinema}" на "{film}" на {time} забронирован.')
