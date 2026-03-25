import csv
with open('history_lessons.csv', 'w', newline='', encoding='utf-8-sig') as csvfiles:
    writer = csv.writer(csvfiles)
    writer.writerow(["DATE", "TOPIC NAME"])
    writer.writerow(["2026-01-09", "Функция вывода - print()"])
    writer.writerow(["2026-01-12", "Списки, string значения. Методы форматирования строк"])
    writer.writerow(["2026-01-16", "Цикл for in, кортеж. Функции: range и type "])
    writer.writerow(["2026-01-28", "Пользовательский ввод - input(). Конструкция if else. int, float"])
    writer.writerow(["2026-02-11", "Конструкция if-elif-else. Словари"])
    writer.writerow(["2026-02-16", "Цикл while. Операторы continue и break. Чётность числа. Флаги true и false"])
    writer.writerow(["2026-02-18", "Функция с ключевым словом def. Параметры"])
    writer.writerow(["2026-02-26", "Классы и наследование. Файлы, with open"])
    writer.writerow(["2026-03-09", "Решение задач по химии на Python. Школьная программа"])
    writer.writerow(["2026-03-13", "Решение задач по химии на Python. Вузовская программа"])
    writer.writerow(["2026-03-19", "Запись и перезапись файла. Вводные данные хим. задачи и результат"])
    writer.writerow(["2026-03-24", "Библиотека. CSV-файлы (таблицы)"])


    with open('history_lessons.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)