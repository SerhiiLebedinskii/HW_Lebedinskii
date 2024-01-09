#Задача 1. Курьер
#Задача 2. Бриллиант
num = int(input("num then enter: "))
if num % 2 and num > 0:
    for i in range(1, num+1, 2):
            spaces = " " * ((num - i) // 2)
            star = "*" * i
            print(spaces, star)
    for i in range(num-2, 0, -2):
            spaces = " " * ((num - i) // 2)
            star = "*" * i
            print(spaces, star)
#Задача 3. Файл-тест. Есть файл, в котором хранятся числа в следующем формате: