# 1. Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётной позиции.

from random import randrange
a = [randrange(1, 10) for i in range(5)]
print(a)
result = sum(a [0::2])
print(result)
