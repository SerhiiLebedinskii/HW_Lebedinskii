#Ввести два цілі числа, знайти більше з них та вивести його, якщо вони рівні, вивести будь яке.
num1 = int(input("num1:"))
num2 = int(input("num2:"))
if num1>num2:
    print(num1)
elif num1<num2:
    print(num2)
else:
    print(num1)
#Ввести два цілі числа, знайти більше з них та вивести його, якщо вони рівні, вивести окреме повідомлення, що вони рівні.
num1 = int(input("num1:"))
num2 = int(input("num2:"))
if num1>num2:
    print(num1)
elif num1<num2:
    print(num2)
else:
    print(f"{num1} = {num2}")
#Ввести три цілі числа, знайти серед них найбільше, найменше й середнє, ігнорувати рівність. Надрукувати результати за допомогою конкатенації.
num1 = int(input("num1:"))
num2 = int(input("num2:"))
num3 = int(input("num3:"))
if num1 != num2 and num2 != num3:
    num = [num1, num2, num3]
    sortnum = sorted(num)
    print("Max:" + str(sortnum[2]) + " "
          "Avg:" + str(sortnum[1]) + " "
          "Min:" + str(sortnum[0]))
#Ввести три цілі числа, знайти серед них найбільше, найменше й середнє, ігнорувати рівність. Надрукувати результати за допомогою метода format.
num1 = int(input("num1:"))
num2 = int(input("num2:"))
num3 = int(input("num3:"))
if num1 != num2 and num2 != num3:
    num = [num1, num2, num3]
    sortnum = sorted(num)
    max_num = sortnum[2]
    avg_num = sortnum[1]
    min_num = sortnum[0]
    s = "Max:{} Avg:{} Min:{}"
    print(s.format(max_num, avg_num, min_num))
#Ввести три цілі числа, знайти серед них найбільше, найменше й середнє, опрацювати всі варианти рівності.
#Надрукувати результати за допомогою префіксу f.
num1 = int(input("num1:"))
num2 = int(input("num2:"))
num3 = int(input("num3:"))
if num1 != num2 and num2 != num3:
    num = [num1, num2, num3]
    sortnum = sorted(num)
    max_num = sortnum[2]
    avg_num = sortnum[1]
    min_num = sortnum[0]
    print (f"max:{max_num}, avg:{avg_num}, min:{min_num}")
else:
    print (f"Введені значення рівні")
#Ввести два числа - роки хлопчика та дівчинки. Якщо обом більше 18-ти, то їм можна
#до клубу, якщо їм більше 60 - то їм краще порадити санаторій, якщо їм менше 18 - то можна порадити їм піццерію.
#Якщо роки змішані, пропорнувати те, що на менші роки. Пропозиції друкувати через префікс.
age_girl = int(input("How many years:"))
age_boy = int(input("How many years:"))
if 18<=age_girl<60 and 18<=age_boy<60:
    print("Клуб: вам обом можна до клубу")
elif age_girl<18 and age_boy<18:
    print("Піццерія: вам краще відвідати піццерію")
elif age_girl>=60 and age_boy>=60:
    print("Санаторій: вам краще відвідати санаторій")
else:
    print("Кіно: вам обом краще відвідати кіно")
#Ввести два числа - роки хлопчика та дівчинки. Якщо обом більше 18-ти, то їм можна до
#клубу, якщо їм більше 55 - то їм краще порадити санаторій, якщо їм менше 18 - то можна порадити
#їм піццерію. Якщо роки змішані, пропорнувати те, що на менші роки. Пропозиції друкувати через префікс."""
