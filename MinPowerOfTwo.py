"""
Способ 1 (С применением логарифма из библиотеки math)
"""

from math import (ceil,log2)

def min_power_of_2_v1(n):


    if n<=0:
        return ('-∞')

    if log2(n) % 1==0:              # Проверка на совпадение n с целой степенью двойки
        return ceil(log2(n)+1)
    else:
        return ceil(log2(n))


print(min_power_of_2_v1(-10))          # -∞
print(min_power_of_2_v1(0))            # -∞
print(min_power_of_2_v1(0.3))          # -1
print(min_power_of_2_v1(0.25))         # -1
print(min_power_of_2_v1(5.25))         # 3
print(min_power_of_2_v1(4))            # 3



"""
Способ 2 (Перебором с сравнением)
"""

def min_power_of_2_v2(n):

    i = 0

    if n <= 0:
        return ('-∞')

    elif n < 1:
        while(2 ** i > n):
            i-=1
        return i + 1

    else:
        while (2 ** i <= n):
            i += 1
        return i


print(min_power_of_2_v2(-10))          # -∞
print(min_power_of_2_v2(0))            # -∞
print(min_power_of_2_v2(0.3))          # -1
print(min_power_of_2_v2(0.25))         # -1
print(min_power_of_2_v2(5.25))         # 3
print(min_power_of_2_v2(4))            # 3



"""
Способ 3 (С помощью двоичной системы счисления)
"""
def min_power_of_2_v3(n):
    counter = 0

    if n<=0:
        return ('-∞')

    elif n < 1:
        m = n
        n = int(1 / n)                    # Преобразуем дробное n в целое число для работы в двоичной системе


        while (n != 0):                   # Сдвигаем биты числа n вправо по одному за шаг
            n >>= 1
            counter += 1
        if 1/(2 ** (counter-1)) == m:     # Проверка на совпадение n с целой степенью двойки
            return -(counter-2)
        else:
            return -(counter-1)

    else:
        n = int(n)
        while (n != 0):
            n >>= 1
            counter += 1

        return counter



print(min_power_of_2_v3(-10))          # -∞
print(min_power_of_2_v3(0))            # -∞
print(min_power_of_2_v3(0.3))          # -1
print(min_power_of_2_v3(0.25))         # -1
print(min_power_of_2_v3(5.25))         # 3
print(min_power_of_2_v3(4))            # 3


"""
Способ 4 (Работа с двоичной записью как с строкой)
"""

from math import ceil

def min_power_of_2_v4(n):

    if n<=0:
        return ('-∞')

    elif n < 1:
        s = bin(ceil(1/n))              # Преобразуем дробное n в целое число для работы в двоичной системе
        if s.rfind('1') == 2:           # Проверка на совпадение n с целой степенью двойки
            return -(len(s) - 4)
        else:
            return -(len(s) - 3)

    else:
        s = bin(int(n))
        return len(s) - 2


print(min_power_of_2_v4(-10))       # -∞
print(min_power_of_2_v4(0))         # -∞
print(min_power_of_2_v4(0.3))       # -1
print(min_power_of_2_v4(0.25))      # -1
print(min_power_of_2_v4(4))         # 3
print(min_power_of_2_v4(5.25))      # 3
