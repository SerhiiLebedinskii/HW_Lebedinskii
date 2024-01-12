#Задача 1. Курьер
need_apartment = int(input("Введіть номер квартири до якої потрібно потрапити:"))
while need_apartment == 0 or need_apartment > 30:
    need_apartment = int(input("Введіть номер квартири до якої потрібно потрапити:"))
else:
    floor_lst = [1,2,3,4,5]
    entrance_lst = [1,2,3]
    number_apartment = need_apartment
    def information_apartment (number_apartment):
        if 1 <= number_apartment <= 10:
            entrance = entrance_lst[0]
            floor = (number_apartment-1)//2+1
        elif 11 <= number_apartment <= 20:
            entrance = entrance_lst[1]
            floor = (number_apartment-11)//2+1
        else:
            entrance = entrance_lst[2]
            floor = (number_apartment-21)//2+1
        return [floor, entrance]
information = information_apartment(number_apartment)
print(f"Номер квартири {number_apartment}, поверх на якому знаходиться квартира {information[0]}, під'їзд квартири {information[1]}")

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
