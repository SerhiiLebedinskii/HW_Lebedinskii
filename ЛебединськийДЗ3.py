#Кожен пише суму списку за допомогою for та while.
#1.1
num = int(input("num:"))
i=sum_num=0
while i<= num:
  sum_num += i
  i +=1
print (sum_num)
#1.2
num = int(input("num:"))
sum_num = 0
for i in range(1, num+1):
    sum_num += i
print(sum_num)
#Написати програму, яка виводить сама себе
file = "program3дз.txt"
fille_open = open(file,'r')
print(fille_open.read())
fille_open.close()
#Написати програму, яка виводить саму себе задом наперед
file = "program3дз.txt"
fille_open = open(file,'r')
text = fille_open.read()
print(text[::-1])
fille_open.close()
#Банкомат видає суму максимально можливими купюрами
a = [1000 for i in range(1,11)]
b = [500 for i in range(1,11)]
c = [200 for i in range(1,11)]
d = [100 for i in range(1,11)]
e = [50 for i in range(1,11)]
f = [20 for i in range(1,11)]
g = [10 for i in range(1,11)]
note = a+b+c+d+e+f+g
amount_note_atm = sum(note)
need_amount = int(input("Вкажіть бажану суму, що кратна 10 та не перевищує 5000 грн:"))
if 0<need_amount<=5000 and not need_amount%10:
    withdrawal_amount = []
    for banknote in note:
        while need_amount >= banknote:
            withdrawal_amount.append(banknote)
            need_amount -= banknote
    print(f"Видано: {sum(withdrawal_amount)}, наступними купюрами: {withdrawal_amount}")
else:
    print("Нажаль введена сума не є кратною 10, або введено суму, що перевищує 5000 грн")
#Банкомат видає суму дрібними, але не більше 10 штук кожної дрібної купюри

#Продовжуємо писати практики з заняття.
"""Написати fizzbuzz для 20 комплектів по три числа, які записані в файл. 
Читайте із файлу перший рядок з трьома числами, беріть із нього числа, рахуйте для них fizzbuzz, виводите, продовжуйте з наступним рядком і так до кінця файла."""
file_input = "fizzbuzzinput3.txt"
file_reading = open (file_input,"r")
for line in file_reading:
    fizz, buzz, num = map(int, line.split(","))
    for i in range(1, num + 1):
        fizz_buzz = ""
        if not i % fizz and not i % buzz:
            fizz_buzz += "FB"
        elif i % fizz == 0:
            fizz_buzz += "F"
        elif i % buzz == 0:
            fizz_buzz += "B"
        else:
            fizz_buzz += str(i)
        print(fizz_buzz, end = " ")
    print()
file_reading.close()
#Переробити другу задачу так, щоб результат писався в інший файл. Додаємо list comprehension, map та інші свіжеотримані знання до виконання завдання.
file_input = "fizzbuzzinput3.txt"
file_output = "fizzbuzzoutput3.txt"
file_writing = open (file_output, "w")
with open (file_input,"r") as file_reading:
    for line in file_reading:
        fizz, buzz, num = map(int, line.split(","))
        for i in range(1, num + 1):
            fizz_buzz = ""
            if not i % fizz and not i % buzz:
                fizz_buzz += "FB"
            elif i % fizz == 0:
                fizz_buzz += "F"
            elif i % buzz == 0:
                fizz_buzz += "B"
            else:
                fizz_buzz += str(i)
            print(fizz_buzz, end = " ")
            file_writing.write(fizz_buzz + " ")
        file_writing.write("\n")
        print()
file_writing.close()