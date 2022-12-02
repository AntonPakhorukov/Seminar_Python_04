# Задача 1: Задайте строку из набора чисел.Напишите программу, которая покажет наибольшее и наименьшее число.
# В качестве символа-разделителя используйте пробел.

# Задача 2: Найдите корни квадратного уравнения ax2 + bx + c = 0 двумя способами:
# - с помощью математических формул нахождения корней квадратного уравнения
# - с помощзью дополнительных библиотек Python sympy

# Задача 3: Задайте два числа. Напишите программу, которая найдет НОК (наименьшее общее кратное)
# этих двух чисел

try:
    taskNumber = int(input('Введите номер задачи: '))
except ValueError:
    print('Не кооректный ввод')
    raise SystemExit
match taskNumber:
    case 1:
        try:
            solution = int(input('Введите способ решения: '))
        except ValueError:
            print('Не корректный ввод')
            raise SystemExit
        match solution:
            case 1:
                string = list(map(int, input('Введите числа в одну строку через пробел: ').split()))
                print(string)
                print(min(string))
                print(max(string))

            case 2:
                string = input('Введите числа в одну строку через пробел: ').split()
                print(string)
                minn = int(string[0])
                maxx = int(string[1])
                for el in range(len(string)):
                    if int(string[el]) < minn:
                        minn = int(string[el])
                    elif int(string[el]) > maxx:
                        maxx = int(string[el])
                print(minn)
                print(maxx)
    case 2:
        try:
            solution = int(input('Введите способ решения: '))
        except ValueError:
            print('Не корректный ввод')
            SystemExit
        match solution:
            case 1:
                a = float(input('Введите значения a: '))
                b = float(input('Введите значения b: '))
                c = float(input('Введите значения c: '))
                dis = b ** 2 - 4 * a * c
                print('Дискрименант = %.2f' % dis) # так выведется с 2 знаками после точки
                if dis > 0:
                    x1 = (-b + dis ** 0.5) / (2 * a)
                    x2 = (-b - dis ** 0.5) / (2 * a)
                    print('x1 = %.2f \nx2 = %.2f' % (x1, x2)) # выведет в две строчки иксы
                elif dis == 0:
                    x = -b / (2 * a)
                    print('x = %.2f' % x)
                else:
                    print('Корней нет')
            case 2:
                import sympy
                a = float(input('Введите значения a: '))
                b = float(input('Введите значения b: '))
                c = float(input('Введите значения c: '))
                x = sympy.Symbol('x') # обязательно сказали, что х - это символ
                print(sympy.solve(a * x ** 2 + b * x + c))
    case 3:
        try:
            solution = int(input('Введите способ решения: '))
        except ValueError:
            print('Ошибка ввода')
            SystemExit
        match solution:
            case 1:
                a, b = map(int, input('Введите числ: ').split())
                m = max(a, b)
                while True:
                    if m % a == 0 and m % b == 0:
                        print(f'НОК = {m}')
                        break
                    else:
                        m += 1
            case 2:
                import sympy
                a = int(input('Введите a: '))
                b = int(input('Введите b: '))
                print(sympy.lcm(a, b))

                        

                
                
        
