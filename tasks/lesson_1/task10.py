#  Пользователь вводит три числа.
#  Напишите программу,
#  которая выводит на экран максимальное из этих трёх чисел (все числа разные).
#  Можно использовать дополнительные переменные, если нужно

#a = int(input("Первое число:"))
#b = int(input("Второе число:"))
#d = int(input("Третье число:"))

#print(max(a, b, d))

print((max(int(input()),int(input()),int(input()))))
# TODO попробуй решить без функции макс

a, b, d = int(input()), int(input()), int(input())

if a > b:
    print (a) if a >= d else print (d)
else:
    print (b) if b >= d else print(d)