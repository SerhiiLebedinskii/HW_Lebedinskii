#1
#Перевірити, чи є введене число парним.
num = int(input("num:"))
if num % 2:
    print(f"{num} - odd number")
else:
    print(f"{num} - even number")
#Перевірити, чи є число не парним, ділиться чи на три і на п'ять одночасно, але так, щоб не ділитися на 10.
num = int(input("num:"))
if num%2 and num%3 == 0 and num%10 != 0:
    print(f"{num} is odd number")
else:
    pass
#Ввести число, вивести усі його дільники.
num = int(input("num:"))
for i in range(1, num+1):
    if num % i == 0:
        print(i, end = " ")
#Ввести число, вивести його розряди та їх множники.
num = int(input("Введіть значення, що менше або рівне 9999: \n"))
a = num%10
b = (num//10)%10
c = (num//100)%10
d = num//1000
print(f"Введене значення, містить: {d}-тисячі,{c}-сотні,{b}-десятки,{a}-одиниці")
#2
#Розвʼязати задачу:
#Задача fizz-buzz:
#Ви маєте три числа, вони вводяться з консолі. Перше число називається fizz, друге називається buzz.
#До третього необхідно дорахувати від одиниці. Дивлячись на поточне число, якщо воно кратне fizz – треба виводити F замість числа.
# Якщо число кратне buzz – треба виводити B замість числа. Якщо число кратне і fizz, і buzz, треба виводити FB.
# Якщо воно не кратне нічому, виводимо число. І так - поки не буде досягнуто третього введеного числа.
#Приклад умови та результату: Введено числа 2, 5, 18 Висновок має бути таким:
#1 F 3 F B F 7 F 9 FB 11 F 13 F B F 17 F

fizz = int(input("fizz:"))
buzz = int(input("buzz:"))
num = int(input("num:"))
for i in range(1, num + 1):
    fizz_buzz = ""
    if not i%fizz and not i%buzz:
        fizz_buzz += "FB"
    elif i%fizz == 0:
        fizz_buzz += "F"
    elif i%buzz == 0:
        fizz_buzz += "B"
    else:
        fizz_buzz += str(i)
    print(fizz_buzz,end=" ")




