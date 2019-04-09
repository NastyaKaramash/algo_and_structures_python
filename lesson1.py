from random import random

#Задача1
num = int(input('Введите трехзначное число: '))
num1 = num % 10
num2 = num // 100
num3 = num % 100 // 10
sum = num1 + num2 + num3
mult = num1 * num2 * num3
print('Сумма: ', sum)
print('Произведение: ', mult)
#Задача2
five = bin(5)
six = bin(6)
print(five)
print(six)
n1 = int(five, 2)
n2 = int(six, 2)
bit_and = n1 & n2
bit_or = n1 | n2
bit_eor = n1 ^ n2
left = n1 << 2
right = n1 >> 2
print('Побитовое и: ', bin(bit_and))
print('Побитовое или: ', bin(bit_or))
print('Побитовое исключающее или: ', bin(bit_eor))
print('Побитовый сдвиг влево: ', bin(left))  # сдвигает влево биты, начиная с младшего, на пустые места 0
print('Побитовый сдвиг вправо: ', bin(right)) # сдвигает вправо, на пустое место 0
#Задача3
x1 = float(input('Введите коородинаты точки 1 по х: '))
y1 = float(input('Введите коородинаты точки 1 по y: '))
x2 = float(input('Введите коородинаты точки 2 по х: '))
y2 = float(input('Введите коородинаты точки 2 по y: '))
k = (y1 - y2) / (x1 - x2)
b = y2 - k*x2
print('Уравнение прямой y =',k,'*x +', b)

#Задача4
m1 = int(input('Введите первое целое число: '))
m2 = int(input('Введите второе целое число: '))
n = int(random() * (m2 - m1 + 1)) + m1
print('Случайное число ', n)

m1 = float(input('Введите первое число: '))
m2 = float(input('Введите второе число: '))
n = random() * (m2 - m1) + m1
print('Случайное число ', round(n, 3))

m1 = ord(input('Введите первую букву: '))
m2 = ord(input('Введите вторую букву: '))
n = int(random() * (m2 - m1 + 1)) + m1
print('Случайная буква: ', chr(n))

#Задача5
a = ord(input('Введите первую букву: '))
b = ord(input('Введите вторую букву: '))
a = a - ord('a') + 1
b = b - ord('a') + 1
print('Позиции: %d и %d' % (a, b))
print('Между буквами символов:', abs(a - b) - 1)

#Задача6
na = int(input('Номер буквы в алфавите: '))
na = ord('a') + na - 1
print('Это буква', chr(na))

#Задача7
sta = int(input('Сторона а: '))
stb = int(input('Сторона b: '))
stc = int(input('Сторона c: '))

if sta + stb <= stc or sta + stc <= stb or stb + stc <= sta:
    print('Треугольник не существует')
elif sta != stb and sta != stc and stb != stc:
    print('Треугольник разносторонний')
elif sta == stb == stc:
    print('Треугольник равносторонний')
else:
    print('Треугольник равнобедренный')

#Задача8
y = int(input('Введите год: '))
if y % 4 = 0:
    print('високосный год')
elif y % 400 == 0:
    if y % 100 !== 0:
        print('Високосный')
    else:
        print('Не високосный')
else:
    print('Не високосный')

#Задача9
a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))

if b < a < c or c < a < b:
    print('Среднее:', a)
elif a < b < c or c < b < a:
    print('Среднее:', b)
else:
    print('Среднее:', c)
