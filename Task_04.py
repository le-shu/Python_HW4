# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

import random

k = int(input('Введите степень многочлена k: '))
arr = []
for i in range(k+1):
    arr.append(random.randint(0,100))
print(arr)

text = ''
for i in range(len(arr) - 1):
    if arr[i] != 0:
        if (k-i) == 1:
            text += str(arr[i]) + 'x + '
        else:
            text += str(arr[i]) + 'x^' + str(k-i) + ' + '

text += str(arr[-1]) + ' = 0'
print(text)

file = open("file_HW_04.txt", "a")
file.write(text)
file.write('\n')
file.close()