# math.py

import math
import random

# Built-in functions
print("Min:", min(3, 7, 1))
#ввод: 3, 7, 1
#вывод: Min: 1
print("Max:", max(3, 7, 1))
#ввод: 3, 7, 1
#вывод: Max: 7
print("Absolute:", abs(-10))
#ввод: -10
#вывод: Absolute: 10
print("Round:", round(3.6))
#ввод: 3.6
#вывод: Round: 4
print("Power:", pow(2, 3))
#ввод: 2, 3
#вывод: Power: 8


# math module
print("Square root:", math.sqrt(16))
#ввод: 16
#вывод: Square root: 4.0
print("Ceil:", math.ceil(4.3))
#ввод: 4.3
#вывод: Ceil: 5
print("Floor:", math.floor(4.9))
#ввод: 4.9
#вывод: Floor: 4
print("Sin:", math.sin(math.pi / 2))
#ввод: math.pi / 2
#вывод: Sin: 1.0
print("Cos:", math.cos(0))
#ввод: 0
#вывод: Cos: 1.0
print("Pi:", math.pi)
#ввод: math.pi
#вывод: Pi: 3.141592653589793
print("Euler:", math.e)
#ввод: math.e
#вывод: Euler: 2.718281828459045

# random module
print("Random number:", random.random())
І#ввод: 
#вывод: Random number: 9999999 (пример)
print("Random integer:", random.randint(1, 10))
#ввод: 1, 10
#вывод: Random integer: 7 (пример)
print("Random choice:", random.choice(["apple", "banana", "cherry"]))
#ввод: ["apple", "banana", "cherry"]
#вывод: Random choice: banana (пример)

numbers = [1, 2, 3, 4]
random.shuffle(numbers)  #shuffle - перемешивает элементы списка случайным образом
print("Shuffled list:", numbers)
#ввод: [1, 2, 3, 4]
#вывод: Shuffled list: [3, 1, 4, 2] (пример)