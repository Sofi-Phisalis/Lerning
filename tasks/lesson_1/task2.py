#  Напишите программу, которая получает от пользователя число и
#  выводит на экран два ответа — следующее и предыдущее числа. Результат:

#  Введите число: 5
#  После числа 5 идет 6
#  Перед числом 5 идет 4

n = input("Введите число:")
next = int(n)+1
prev = int(n)-1

print("После числа", n, "идет", next)
print("Перед числом", n, "идет", prev)

