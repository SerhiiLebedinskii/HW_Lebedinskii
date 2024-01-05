#Надрукувати "We are the champions" за допомогою коду.
words = "We are the champions"
print(words)
print ("We are the champions")
"""Надрукувати "We are the champions", поклавши 'champions' у окрему змінну.
Використати конкатенацію (склійку рядків через плюс)."""
words1 = "We are the"
word2 = "champions"
print(words1 + ' ' + word2)
#Виконати передоднє завдання, користуючись форматуваннями через відсоток.
print('%s %s' % (words1,word2))
#Виконати передоднє завдання, користуючись форматуваннями через метод format.
S = "{0} are {1} champions"
S = "{} are {} champions"
print(S.format("We","the"))
#Виконати передоднє завдання, користуючись форматуваннями через префікс f.
print(f"We are the {word2}")
#Ввести імʼя, надрукувати "Hello, " й додати імʼя, яке було введено. Склійку робити за допомогою префіксу f.
name = input("What is your name:")
print(f"Hello, {name}")
#Ввести два імені, надрукувати рядок, де буде написано, що перше імʼя та друге імʼя пішли гуляти.
# Наприклад, якщо введені Alex та Mary, надрукувати "Alex and Mary go for a walk.", за допомогою префіксу.
name1 = input("What is your name:")
name2 = input("What is your name:")
print(f'{name1} and {name2} go for a walk')
#Ввести два цілих числа, трансформувати їх до цілих чисел, скласти, надрукувати суму.
int1 =  input("int1:")
int2 =  input("int2:")
print(int(int1)+int(int2))
#Ввести три цілих числа, трансформувати до цілих чисел, надрукувати суму.
int1 = input("int1:")
int2 = input("int2:")
int3 = input("int3:")
print(int(int1)+int(int2)+int(int3))
#Ввести два цілих числа num1, num2 й один рядок str1, надрукувати "num1 and num2 are str1",
#використовувати форматування f.
num1 = input("num1:")
num2 = input("num2:")
str1 = input()
print (f"{num1} and {num2} are {str1}")