while True:
    age_1 = input("Введите ваш возраст: ")

    if not age_1.isdigit():
        print("Введите целое положительное число.")
        continue

    age = int(age_1)

    if age >= 18:
        print("Вы можете приобрести алкоголь.")

    elif age < 18:
        print("Вам меньше 18. Вы не можете приобрести алкоголь.")
        break
