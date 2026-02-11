"""fruits = ["apple", "banana", "cherry"]
fruit = "strawberry"

if fruit not in fruits:
    print(f"{fruit} Такого фрукта нет")"""

"""age = 21
if age < 6:
    print("Cтоимость проезда 50 рублей")
elif age < 20:
    print("Стоимость проезда 100 рублей")
else:
    print ("Cтоимость проезда 150 рублей")"""

person = {'name': 'Sasha', 'age': 21}
person['age'] = 27
person['name'] = 'Maria'
print(person['name'])
print(person['age'])

car = {'speed': 300, 'model': 'Chevrolet', 'color': 'red'}
if car['speed'] > 250:
    print("Car speed is medium")
elif car['speed'] <= 100:
    print("Car speed is slow")
else:
    print("Car speed is fast")

age = 20
if age == 15 or 18:
    print('success')
else:
    print('fail')


