#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Использовать словарь, содержащий следующие ключи: название начального пункта маршрута;
# название конечного пункта маршрута; номер маршрута. Написать программу, выполняющую
# следующие действия: ввод с клавиатуры данных в список, состоящий из словарей
# заданной структуры; записи должны быть упорядочены по номерам маршрутов;
# вывод на экран информации о маршрутах, которые начинаются или оканчиваются в пункте,
# название которого введено с клавиатуры; если таких маршрутов нет,
# выдать на дисплей соответствующее сообщение.

import bisect
import re
import sys


if __name__ == "__main__":
    routes = []
    while True:
        command = input(">>> ").lower()
        line = '+-{}-+-{}-+-{}-+'.format(
            '-' * 30,
            '-' * 20,
            '-' * 8
        )
        text = (
            '| {:^30} | {:^20} | {:^8} |'.format(
                "Начало",
                "Конец",
                "Номер"
            )
        )
        match command:
            case 'exit':
                break

            case 'add':

                start = input("Введите начальный пункт: ")
                end = input("Введите конечный пункт: ")
                count = int(input("Введите номер маршрута: "))

                route = {
                    'начальный пункт': start,
                    'конечный пункт': end,
                    'номер маршрута': count
                }


                if route not in routes:
                    bisect.insort(
                        routes, route, key=lambda item: item.get('номер маршрута'))
                else:
                    print("данный маршрут уже добавлен")

            case 'list':
                print(line)
                print(text)
                print(line)
                for route in routes:
                    print(
                        '| {:<30} | {:<20} | {:>8} |'.format(
                            route.get('начальный пункт', ''),
                            route.get('конечный пункт', ''),
                            route.get('номер маршрута', '')
                        )
                    )

                print(line)

            case _ if (m := re.match(r'select (.+)', command)) is not None:
                name_punct = m.group(1)
                found = False
                for route in routes:
                    if route['начальный пункт'].lower() == name_punct or route['конечный пункт'].lower() == name_punct:
                        if not found:
                            print(line, text, sep="\n")

                        print(
                            '| {:<30} | {:<20} | {:>8} |'.format(
                                route.get('начальный пункт', ''),
                                route.get('конечный пункт', ''),
                                route.get('номер маршрута', '')
                            )
                        )
                        found = True
                if not found:
                    print("Маршрутов с данным пунктом не найдено.")

            case 'help':
                # Вывести справку о работе с программой.
                print("Список команд:\n")
                print("add - добавить маршрут;")
                print("list - вывести список маршрутов;")
                print("select <название пункта> - запросить маршруты, которые начинаются\n"
                      "или заканчиваются в данном пункте;")
                print("help - отобразить справку;")
                print("exit - завершить работу с программой.")

            case _:
                print(f"Неизвестная команда {command}", file=sys.stderr)
