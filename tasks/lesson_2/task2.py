# TODO Написать программу которая вроверяет корректное название файла
#  - файлы не должны называться на спец символы:  '@', '№', '$', '%', '^', '&', '\\', '*', '(', ')'
#  - заканчиваться только на .txt или .docx.
#  Пример:
#  Ввод названия файла
#  "Ошибка: название начинается на один из специальных символов."
#  "Ошибка: неверное расширение файла. Ожидалось .txt или .docx."
#  "Файл назван верно."

text = input("Название файла: ")
# if че то там:
print("Ошибка: название начинается на один из специальных символов.")
# чето еще
print("Ошибка: неверное расширение файла. Ожидалось .txt или .docx.")
# если все ок
print("Файл назван верно.")