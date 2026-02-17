while True:
    number = input("Введите число: ")
    if number.isdigit():
        number = int(number)
        if number % 2 == 0:
            print(f"Число {number} — чётное")
        else:
            print(f"Число {number} — нечётное")
    else:
        print("Это не число.")