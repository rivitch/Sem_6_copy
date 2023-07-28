# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону (т.е. не 
# меньше заданного минимума и не больше заданного 
# максимума)

min = ""
max = ""
list_1 = list()
res = list()
from random import randint
a = int(input("Введите количество элементов массива, a = "))
min = int(input("Введите минимум диапазона, min = "))
max = int(input("Введите максимум диапазона, max = "))
for i in range(a):
    b = randint(0,20)
    list_1.append(b)
print("Элементы массива -",*list_1) # вывод массива
for i in range(len(list_1)):
    if list_1[i] >= min and list_1[i] <= max:        
        res.append(i)
print("индексы элементов массива (списка) - ",*res)