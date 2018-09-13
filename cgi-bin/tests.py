# -*- coding: UTF-8 -*-
u"""Тесты для проверки простых, четных и нечетных чисел на простоту."""
import server


def test_for_prime_numbers():
    u"""
    Тест для проверки на факторизацию простых чисел.

    Читаем простые числа из файла.
    Если приходит от алгоритма Ферма флаг False, то
    это значит число простое, иначе выводим число
    и выходим из цикла.
    """
    f = open("SimpleNumbers.txt")
    simple_numbers = f.read()
    f.close()
    data = []
    data = simple_numbers.split(',')
    for x in data:
        x = int(x)
        flag = server.algorithm_Ferma(x)
        if flag is False:
            continue
        else:
            print("number: ", x)
            flag = True
            break
    if flag is True:
        print("the simplicity test is not passed")
    else:
        print("test for simplicity passed")


def test_for_even_numbers():
    u"""
    Тест для проверки четных чисел на факторизацию.

    Цикл по четным числам от 4 до 2000.
    Число раскладывается на простые множители, затем
    множители перемножаются и сравниваются с исходным
    числом. Если совпали, то идем дальше по циклу, иначе
    вывод чисел и выход из цикла.
    """
    for x in range(4, 2000, 2):
        numb = 1
        tmp = []
        x = int(x)
        flags = server.factorization_even_number(x, tmp)
        for flag in flags:
            numb = numb * flag
        if x == numb:
            continue
        else:
            print("x: ", x)
            print("numb: ", numb)
            flag = True
            break
    if flag is True:
        print("the test for even numbers is not complete")
    else:
        print("the test on even numbers is completed")


def odd_number_test():
    u"""
    Тест для проверки нечетных чисел на факторизацию.

    Цикл по четным числам от 5 до 2001.
    Число раскладывается на простые множители, затем
    множители перемножаются и сравниваются с исходным
    числом. Если совпали, то идем дальше по циклу, иначе
    вывод чисел и выход из цикла.
    """
    for x in range(5, 2001, 2):
        numb = 1
        tmp = []
        x = int(x)
        flags = server.algorithm_in_cycle(x, tmp)
        for flag in flags:
            numb = numb * flag
        if x == numb:
            continue
        else:
            print("x: ", x)
            print("numb: ", numb)
            flag = False
            break
    if flag is False:
        print("the test is not completed")
    else:
        print("odd numbered test completed")


test_for_prime_numbers()
# test_for_even_numbers()
# odd_number_test()
