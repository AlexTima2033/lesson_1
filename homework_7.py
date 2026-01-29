my_name = input("Введите ваше имя: ")
partner_name = input("Введите имя партнёра: ")
my_age = int(input("Введите ваш возраст: "))
partner_age = int(input("Введите возраст партнёра: "))
message = f"Меня зовут {my_name.title()}, его зовут {partner_name.title()}."
message_age = f"На двоих нам {my_age + partner_age}."
print(message)
print(message_age)
