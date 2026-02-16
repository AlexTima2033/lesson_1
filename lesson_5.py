"""while True:
    number = input("Введите число: ")
    if number.isdigit():
        number = int(number)
        if number % 2 == 0:
            print("Это чётное число")
        else:
            print("Это нечётное число")
    else:
        print("Это не число.")"""


"""while True:
    message = input("Введите сообщение: ")
    if message == "quit":
        break
    else:
        print(message)"""

"""current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)"""

fruits = ["apple", "banana", "cherry", "pineapple", "grape", "orange", "mango", "potato", "potato", "potato", "potato", "potato"]
print(fruits)
while True:
    if 'potato' in fruits:
        continue
print(fruits)


