while True:
    try:
        number = int(input("Введите число: "))

        if number % 2 == 0:
            print(f"Число {number} - чётное")
        else:
            print(f"Число {number} - нечётное")
    except ValueError:
        print("Это не число.")