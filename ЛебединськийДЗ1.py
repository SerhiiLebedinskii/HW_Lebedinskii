#1
"""Тип даних - це вид або характеристика значення, що присвоєнно змінній,
якщо якійсь змінній присвоїти значення цілого числа то тоді тип змінної буде int
для дробових тип змінної буде flot, як приклад.
Динамічна типізація - це коли тип змінної визначається на поточний момент, тобто навіть
якщо змінній на початку присвоїти числове значення то потім ми в цю змінну зможемо вкладати значення
інших типів відповідно тип змінної теж змінюватиметься.
Статична типізація - це коли тип змінної задають ще на початку і він є не змінним
тобто в змінну у якої тип int вже не можна вкласти значення іншого типу наприклад дробового числа
Cильна типізація - операцції виконуються над значеннями одного виду.
Слабка типізація - це коли мова сама може змінити тип змінної 
для того щоб виконати операцію над змінними різних типів."""
#3
necessityEnvelop = 0
freedomEnvelop = 0
educationEnvelop = 0
longTermEnvelop = 0
playEnvelop = 0
giveEnvelop = 0

necRate = 0.55
ffaRate = 0.1
eduRate = 0.1
ltssRate = 0.1
playRate = 0.1
giveRate = 0.05

expectedIncome = 1000

print ("""Hello.\n
We gonna fill your envelops by the money you input here!\n
Please input your amounts of money income and see the results.\n
Press Ctrl+c to exit script.
\n\n Enter the amount please:""")

sum = 0

while (sum < expectedIncome):
    line = int(input())
    sum += line

    necessityEnvelop += line * necRate
    freedomEnvelop += line * ffaRate
    educationEnvelop += line * eduRate
    longTermEnvelop += line * ltssRate
    playEnvelop += line * playRate
    giveEnvelop += line * giveRate
    print("\n Enter the amount please:")

print(f"At the end we have:\n\
    Necessity Envelop has:{int(necessityEnvelop)}\n\
    Financial Freedom Envelop has:{int(freedomEnvelop)}\n\
    Education Envelop:{int(educationEnvelop)}\n\
    Long Term Saving for Spending Envelop has:{int(longTermEnvelop)}\n\
    Play Envelop has:{int(playEnvelop)}\n\
    Give Envelop has:{int(giveEnvelop)}\n\
    _______________________________________________________________\n\
\
    Thanks for using our software :)")
