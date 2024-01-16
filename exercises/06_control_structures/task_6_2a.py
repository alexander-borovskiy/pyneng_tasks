# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса.
Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'

Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
ip = input("Введите IP-адрес в формате 10.0.1.1: ")
if ip.count(".") == 3:
    oct = []
    for i in ip.split("."):
        if i.isdigit() and 0 <= int(i) <= 255:
            oct.append(int(i))
    if len(oct) == 4:
        if 1 <= oct[0] <= 223:
            print("unicast")
        elif 224 <= oct[0] <= 239:
            print("multicast")
        elif ip == "255.255.255.255":
            print("local broadcast")
        elif ip == "0.0.0.0":
            print("unassigned")
        else:
            print("unused")
    else:
        print("Неправильный IP-адрес")
else:
    print("Неправильный IP-адрес")
