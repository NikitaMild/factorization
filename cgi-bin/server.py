#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
u"""
1)!/usr/bin/env python3  2) -*- coding: UTF-8 -*- .

1)Эта строка сообщает cgi-серверу о том,
что используется язык программирования python >= v3.
2)Эта строка для подключения кодировки. В данном случае это UTF-8
"""
import cgi
import cgitb
import html
import math


def factorization_even_number(number, storage):
    u"""
    Функция факторизации четного числа.

    Number - факторизуемое четное число.
    storage - список, в который записываются простые множители.
    algorithm_in_cycle - фун-ция, которая применяет множество раз
    алгоритм Ферма для факторизации числа.
    """
    if number % 2 == 0:
        storage.append(2)
        number = int(number / 2)
        if number == 1:
            return storage
        return factorization_even_number(number, storage)
    else:
        tmp = []
        tmp = algorithm_in_cycle(number, tmp)
        storage += tmp
        return storage


def algorithm_Ferma(testing_number):
    u"""
    algorithm_Ferma - Алгоритм факторизации нечетного числа.

    Метод основан на поиске целых чисел [x,y] таких, что
    x^2 - y^2 = testing_number, что ведет к разложению
    testing_number = (x-y)*(x+y)
    testing_number - нечетное число, которое факторизуется.
    """
    if testing_number == 2:
        return False
    x = int(math.sqrt(testing_number))
    if x**2 == testing_number:
        return [x, x]
    while True:
        x += 1
        temp = (testing_number + 1) / 2
        if x == temp:
            return False
        else:
            z = x**2 - testing_number
            y = int(math.sqrt(z))
        if y**2 == z:
            return [x + y, x - y]


def Cycle(test_numb, information_storage):
    u"""
    Cycle - Рекурсивная функция для разложения числа на простые множители.

    Сначала применяется алгоритм Ферма.
    Если число уже простое, то записываем в список,
    иначе отправляем список снова в алгоритм до тех пор,
    Пока каждое число в списке на станет простым.
    test_numb - число, которое нужно факторизовать.
    information_storage - список с простыми множителями.
    """
    tmp_list = []
    numbs = algorithm_Ferma(test_numb)
    if numbs is False:
        information_storage.append(test_numb)
        return information_storage
    else:
        for numb in numbs:
            tmp_list.append(numb)
    if tmp_list == []:
        return information_storage
    return algorithm_in_cycle(tmp_list, information_storage)


def algorithm_in_cycle(numbers, storage):
    u"""
    algorithm_in_cycle - функция для разложения числа на простые множители.

    Принимает на вход два аргумента и отправляет их в
    рекурсию.
    numbers - список после первого разложения по алгоритму Ферма.
    storage - список, в который записываются простые множители.
    """
    try:
        for numb in numbers:
            tmp = Cycle(numb, storage)
    except TypeError:
        tmp = Cycle(numbers, storage)
    return tmp


def output_page(file_name, flag, number):
    u"""
    output_page - функция для вывода html страниц с факторизованным числом.

    file_name - имя файла, где лежит html страница.
    flag - флаг. Если None - число либо простое,
    либо в поле 'Введите число' на главной странице
    ввели неверный формат данных. Иначе это список
    простых множителей факторизованного числа.
    number - Изначальное число, что ввел пользователь.
    """
    f = open(file_name)
    from_file = f.read()
    f.close()
    print("Content-type: text/html\n")
    if flag is None:
        print(from_file.format(number))
    else:
        print(from_file.format(number, flag))


if __name__ == "__main__":
    info_storage = []
    cgitb.enable(display=0, logdir="cgi-bin/logs")
    form = cgi.FieldStorage()
    user_number = form.getfirst("InputNumber", "Not found")
    try:
        user_number = int(html.escape(user_number))
        if user_number % 2 == 0:
            answ = factorization_even_number(user_number, info_storage)
            output_page("page2.html", answ, user_number)
        else:
            answ = algorithm_Ferma(user_number)
            if answ is False:
                output_page("page1.html", None, user_number)
            else:
                answ = algorithm_in_cycle(answ, info_storage)
                output_page("page3.html", answ, user_number)
    except ValueError:
        output_page("ErrorPage.html", None, user_number)
