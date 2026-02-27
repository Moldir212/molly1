#1
# Генератор, который возвращает квадраты чисел от 1 до n
def squares(n):
    for i in range(1, n + 1):  # перебираем числа от 1 до n
        yield i * i           # возвращаем квадрат числа
# Ввод числа
n = int(input())
# Перебираем значения генератора
for i in squares(n):
    print(i)                                      #ЭТО ПЕРВОЕ ЗАДАНИЕ НА EDJUDGE!!!
#ввод: 5
#вывод:
#1
#4
#9
#16
#25

#2
# Генератор чётных чисел от 0 до n
def even_numbers(n):
    for i in range(0, n + 1, 2):  # шаг 2 = только чётные
        yield str(i)             # превращаем в строку для красивого вывода
n = int(input())
first = True  # флаг, чтобы не поставить запятую в начале
for i in even_numbers(n):
    if not first:
        print(",", end="")  # печатаем запятую без перехода строки
    print(i, end="")        # печатаем число
    first = False
#ввод: 10
#вывод: 0,2,4,6,8,10

#3
# Генератор чисел, которые делятся на 3 и на 4
def divtf(n):
    for i in range(0, n + 1):
        if i % 3 == 0 and i % 4 == 0:  # проверка делимости
            yield i
n = int(input())
first = True
for i in divtf(n):
    if not first:
        print(",", end="")
    print(i, end="")
    first = False
    #ввод: 50
    #вывод: 0,12,24,36,48


#4
# Генератор квадратов от a до b
def squares(a, b):
    for i in range(a, b + 1):
        yield i * i
# Ввод двух чисел
a, b = map(int, input().split())
# Вывод квадратов
for i in squares(a, b):
    print(i)
#ввод: 3 6
#вывод:
#9
#16
#25
#36

#5
# Генератор обратного отсчёта
def pri(n):
    while n >= 0:
        yield n  # возвращаем текущее число
        n -= 1   # уменьшаем на 1
n = int(input())
first = True
for i in pri(n):
    if not first:
        print(",", end="")
    print(i, end="")
    first = False
#ввод: 5
#вывод: 5,4,3,2,1,0