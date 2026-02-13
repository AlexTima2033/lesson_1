car = {'Model': 'Carla', 'Color': 'Black', 'Presence': 'No'}

if car['Presence'] == 'Yes' and car['Model'] == 'Carla':
    print("Машина есть в автосалоне")
elif car['Presence'] == 'Yes' and car['Color'] == 'Black':
    print("Чёрная машина")
else:
    print("Машины нет в автосалоне")