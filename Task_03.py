# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.

def Non_rep(arr):
    new_arr = []
    for i in arr:
        if i not in new_arr:
            new_arr.append(i)
    print(f"Список из неповторяющихся элементов: {new_arr}")

arr = []
arr = list(map(int, input('Введите числа через пробел:\n').split()))
Non_rep(arr)
