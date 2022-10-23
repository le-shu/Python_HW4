# Вычислить число c заданной точностью d

def Calc_pi():
    accuracy = float(input('Введите точность: '))
    sum = 0
    number = 1
    sign = 1
    a = 1

    while a >= accuracy:
        a = 4/number
        sum = sum + sign * a
        sign = - sign
        number = number + 2

    print(sum)
    
Calc_pi()