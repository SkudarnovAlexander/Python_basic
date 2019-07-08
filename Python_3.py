# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.


def my_round(number, ndigits):
    str_number = str(number)
    start = str_number.find(".") + ndigits + 1
    number = float(str_number[:start])
    if int(str_number[start]) > 4:
        number += 10 ** - ndigits
    return(number)


print(my_round(2.1234537, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Постарайтесь использовать то, что мы прошли на уроке при решении этого ДЗ,
# вспомните про zip(), map(), lambda, посмотрите где лучше с ними, а где они излишни!

print("Задание - 1\n")

# Создайте функцию, принимающую на вход Имя, возраст и город проживания человека
# Функция должна возвращать строку вида "Василий, 21 год(а), проживает в городе Москва"


def information(name, age, town):
    print(f"{name}, {age} год(а), проживает в городе {town}")


information("Александр", "27", "Питер")

print("Задание - 2")
# Создайте функцию, принимающую на вход 3 числа, и возвращающую наибольшее из них


def max_of_three(num_1, num_2, num_3):
    print(max(num_1, num_2, num_3))


max_of_three(1, 56, 43)


print("Задание - 3")
# Создайте функцию, принимающую неограниченное количество строковых аргументов,
# верните самую длинную строку из полученных аргументов


def max_string(*string):
    print(max(string, key=len))


max_string("gfgf", "fdd", "fdgfwag4wg", "ff")




# Задание - 1
# Вам даны 2 списка одинаковой длины, в первом списке имена людей, во втором зарплаты,
# вам необходимо получить на выходе словарь, где ключ - имя, значение - зарплата.
# Запишите результаты в файл salary.txt так, чтобы на каждой строке было 2 столбца,
# столбцы разделяются пробелом, тире, пробелом. в первом имя, во втором зарплата, например: Vasya - 5000
# После чего прочитайте файл, выведите построчно имя и зарплату минус 13% (налоги ведь),
# Есть условие, не отображать людей получающих более зарплату 500000, как именно
#  выполнить условие решать вам, можете не писать в файл
# можете не выводить, подумайте какой способ будет наиболее правильным и оптимальным,
#  если скажем эти файлы потом придется передавать.
# Так же при выводе имя должно быть полностью в верхнем регистре!
# Подумайте вспоминая урок, как это можно сделать максимально кратко, используя возможности языка Python.


humans = ["Саша", "Вася", "Сергей", "Екатерина", "Полина", "Олег", "Ульяна"]
money = [5000, 20000, 750000, 15000, 670000, 320000, 75000]

dictionary = dict(zip(humans, money))

print(dictionary)
f = open('text.txt', 'w')
for index in dictionary:
    key_value = f"{index} - {dictionary[index]}"
    f.write(key_value + '\n')
f.close()

f = open('text.txt')
for line in f:
    new_list = line.split()
    if int(new_list[2]) * 0.87 < 500000:
        print(f"{new_list[0].upper()} {int(new_list[2]) * 0.87}")





# Задание - 1
# Давайте опишем пару сущностей player и enemy через словарь,
# который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health - 100,
# damage - 50.
# Поэксперементируйте с значениями урона и жизней по желанию.
# Теперь надо создать функцию attack(person1, person2), аргументы можете указать свои,
# функция в качестве аргумента будет принимать атакующего и атакуемого,
# функция должна получить параметр damage атакующего и отнять это количество
# health от атакуемого. Функция должна сама работать с словарями и изменять их значения.

# Задание - 2
# Давайте усложним предыдущее задание, измените сущности, добавив новый параметр - armor = 1.2
# Теперь надо добавить функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
# Следовательно у вас должно быть 2 функции, одна наносит урон, вторая вычисляет урон по отношению к броне.

# Сохраните эти сущности, полностью, каждую в свой файл,
# в качестве названия для файла использовать name, расширение .txt
# Напишите функцию, которая будет считывать файл игрока и его врага, получать оттуда данные, и записывать их в словари,
# после чего происходит запуск игровой сессии, где сущностям поочередно наносится урон,
# пока у одного из них health не станет меньше или равен 0.
# После чего на экран должно быть выведено имя победителя, и количество оставшихся единиц здоровья.

import random



def open_file(name_file):
    parameters = []
    values = []
    g = open(f'{name_file}.txt')
    for line in g:
        name_list = line.split()
        parameters.append(name_list[0])
        values.append(float(name_list[1]))
    return dict(zip(parameters, values))


player = {}
enemy = {}
player = open_file("player_param")
enemy = open_file("enemy_param")
print(player)
print(enemy)

player["name"] = input("Введите новое имя игрока:  ")
enemy["name"] = input("Введите новое имя врага:  ")


def attack_2(person1, person2):
    print("ход " + person2["name"])
    if random.randint(0, 100) <= (person1["evasion"]):
        if random.randint(0, 100) > person1["armor_chance"]:
            person1["health"] -= person2["damage"]
            print(f'{person2["name"]} наносит {person2["damage"]:.1f} урона.')
        else:
            print(person1["name"] + " закрылся щитом!")
            person1["health"] -= person2["damage"] / person1["armor"]
            print(f'{person2["name"]} наносит {person2["damage"] / person1["armor"]:.1f} урона.')
    else:
        print("мимо!")
    print(f'{person1["name"]} XP: {person1["health"]:.1f}, {person2["name"]} XP: {person2["health"]:.1f} \n')


def attack_1(person1, person2):
    print("ход " + person1["name"])
    if random.randint(0, 100) <= person2["evasion"]:
        if random.randint(0, 100) > person1["armor_chance"]:
            person2["health"] -= person1["damage"]
            print(f'{person1["name"]} наносит {person1["damage"]:.1f} урона.')
        else:
            print(person2["name"] + " закрылся щитом!")
            person2["health"] -= person1["damage"] / person2["armor"]
            print(f'{person1["name"]} наносит {person1["damage"] / person2["armor"]:.1f} урона.')
    else:
        print("мимо!")
    print(f'{person1["name"]} XP: {person1["health"]:.1f}, {person2["name"]} XP: {person2["health"]:.1f} \n')


while True:
    attack_1(player, enemy)
    if enemy["health"] <= 0:
        print(player["name"] + " WINS")
        break
    attack_2(player, enemy)
    if player["health"] <= 0:
        print(enemy["name"] + " WINS")
        break







