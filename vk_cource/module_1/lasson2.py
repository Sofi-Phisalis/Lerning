my = input()
print("Hello,", my)

# С версии питона 3.0 появился метод .format() который позволяет вставлять переменные в тест:
print("Hello, {}".format(my))
# С версии питона 3.6 появились f строки. Они быстрее и удобнее:
print(f"Hello, {my}")
# Так же работает с несколькими переменными
location = input()
time = input()
print("Current location is", location, "and time is", time)
print("Current location is {} and time is {}".format(location, time))
print(f"Current location is {location} and time is {time}")

# А еще вызовы функций сразу можно вставлять в print
print(f"Current location is {input()} and time is {input()}")

