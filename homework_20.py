def greet_user(data):
    first_name = data.get('first_name', 'Unknown')
    last_name = data.get('last_name', 'Unknown')

    return first_name.title(), last_name.title()


user_data = {'first_name': 'katya', 'last_name': 'mironova'}
first, last = greet_user(user_data)

print(first, last)




