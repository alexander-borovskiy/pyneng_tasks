# -*- coding: utf-8 -*-
"""
Задание 25.2

Для заданий 25 раздела нет тестов!

В этом задании необходимо создать скрипт get_data.py.

Код в скрипте должен быть разбит на функции.
Какие именно функции и как разделить код, надо решить самостоятельно.
Часть кода может быть глобальной.

Скрипту могут передаваться аргументы и, в зависимости от аргументов,
надо выводить разную информацию.
Если скрипт вызван:
* без аргументов, вывести всё содержимое таблицы dhcp
* с двумя аргументами, вывести информацию из таблицы dhcp,
  которая соответствует полю и значению
* с любым другим количеством аргументов, вывести сообщение,
  что скрипт поддерживает только два или ноль аргументов

Файл БД можно скопировать из задания 25.1.

Примеры вывода для разного количества и значений аргументов:

$ python get_data.py
В таблице dhcp такие записи:
-----------------  ---------------  --  ----------------  ---
00:09:BB:3D:D6:58  10.1.10.2        10  FastEthernet0/1   sw1
00:04:A3:3E:5B:69  10.1.5.2          5  FastEthernet0/10  sw1
00:05:B3:7E:9B:60  10.1.5.4          5  FastEthernet0/9   sw1
00:07:BC:3F:A6:50  10.1.10.6        10  FastEthernet0/3   sw1
00:09:BC:3F:A6:50  192.168.100.100   1  FastEthernet0/7   sw1
00:E9:BC:3F:A6:50  100.1.1.6         3  FastEthernet0/20  sw3
00:E9:22:11:A6:50  100.1.1.7         3  FastEthernet0/21  sw3
00:A9:BB:3D:D6:58  10.1.10.20       10  FastEthernet0/7   sw2
00:B4:A3:3E:5B:69  10.1.5.20         5  FastEthernet0/5   sw2
00:C5:B3:7E:9B:60  10.1.5.40         5  FastEthernet0/9   sw2
00:A9:BC:3F:A6:50  10.1.10.60       20  FastEthernet0/2   sw2
-----------------  ---------------  --  ----------------  ---

$ python get_data.py vlan 10

Информация об устройствах с такими параметрами: vlan 10
-----------------  ----------  --  ---------------  ---
00:09:BB:3D:D6:58  10.1.10.2   10  FastEthernet0/1  sw1
00:07:BC:3F:A6:50  10.1.10.6   10  FastEthernet0/3  sw1
00:A9:BB:3D:D6:58  10.1.10.20  10  FastEthernet0/7  sw2
-----------------  ----------  --  ---------------  ---

$ python get_data.py ip 10.1.10.2

Информация об устройствах с такими параметрами: ip 10.1.10.2
-----------------  ---------  --  ---------------  ---
00:09:BB:3D:D6:58  10.1.10.2  10  FastEthernet0/1  sw1
-----------------  ---------  --  ---------------  ---

$ python get_data.py vln 10
Данный параметр не поддерживается.
Допустимые значения параметров: mac, ip, vlan, interface, switch

$ python get_data.py ip vlan 10
Пожалуйста, введите два или ноль аргументов

"""
import sqlite3
import sys
from tabulate import tabulate


def get_data(db_name):
    query_dict = {
        'vlan': 'select mac, ip, vlan, interface, switch from dhcp where vlan = ?',
        'mac': 'mac, ip, vlan, interface, switch from dhcp where mac = ?',
        'ip': 'select mac, ip, vlan, interface, switch from dhcp where ip = ?',
        'interface': 'select mac, ip, vlan, interface, switch from dhcp where interface = ?',
        'switch': 'select mac, ip, vlan, interface, switch from dhcp where switch = ?'
                }
    keys = query_dict.keys()
    if check_args():
        key, value = check_args()
    else:
        return
    if not key in keys:
        print('Данный параметр не поддерживается.\n'
        'Допустимые значения параметров: {}'.format(', '.join(keys)))
        return
    print('\nИнформация об устройствах с такими параметрами: ', key, value)
    query = query_dict[key]
    conn = db_connect(db_name)
    cursor = conn.cursor()
    result = cursor.execute(query, (value, ))
    print(tabulate(result))
    db_close(conn)


def get_alldata():
    print("В таблице dhcp такие записи:")
    conn = db_connect(db_name)
    cursor = conn.cursor()
    result = cursor.execute('select * from dhcp')
    print(tabulate(result))
    db_close(conn)


def check_args():
    args = sys.argv[1:]
    if len(args) > 2 or len(args) == 1:
        print('Пожалуйста, введите два или ноль аргументов')
        return False
    elif not args:
        get_alldata()
    else:
        return args


def db_connect(db_name):
    return sqlite3.connect(db_name)


def db_close(connect):
    connect.close()


if __name__ == "__main__":
    db_name = 'dhcp_snooping.db'
    get_data(db_name)
