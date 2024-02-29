# -*- coding: utf-8 -*-
"""
Задание 15.4

Создать функцию get_ints_without_description, которая ожидает как аргумент
имя файла, в котором находится конфигурация устройства.

Функция должна обрабатывать конфигурацию и возвращать список имен интерфейсов,
на которых нет описания (команды description).

Пример итогового списка:
["Loopback0", "Tunnel0", "Ethernet0/1", "Ethernet0/3.100", "Ethernet1/0"]

Пример интерфейса с описанием:
interface Ethernet0/2
 description To P_r9 Ethernet0/2
 ip address 10.0.19.1 255.255.255.0
 mpls traffic-eng tunnels
 ip rsvp bandwidth

Интерфейс без описания:
interface Loopback0
 ip address 10.1.1.1 255.255.255.255

Проверить работу функции на примере файла config_r1.txt.
"""
import re


def get_ints_without_description(filename):
    """
    Функция должна обрабатывать конфигурацию и возвращать список имен интерфейсов,
    на которых нет описания (команды description).
    """
    no_description_list = []
    regex = re.compile(r'^interface (?P<interface>\S+)'
                       r'| description .+')
    with open(filename) as f:
        for line in f:
            m = regex.search(line)
            if m:
                if m.lastgroup == 'interface':
                    interface = m.group(m.lastgroup)
                    no_description_list.append(interface)
                else:
                    no_description_list.remove(interface)
    return no_description_list


if __name__ == '__main__':
    print(get_ints_without_description('config_r1.txt'))
