flag = True
while flag:
    message = input("Введите число: ")

    if message == "stop":
        flag = False
        continue

    if message.isdigit():
        number = int(message)
        if number % 2 == 0:
            print(f"{number} — чётное число")
        else:
            print(f"{number} — нечётное число")
    else:
        print("Введите целое положительное число")