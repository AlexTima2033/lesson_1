mass_H = 1.0 #Задача 1
mass_O = 16.0

molecular_mass = 2 * mass_H + mass_O

with open('chemist_2.txt', 'w', encoding='utf-8') as file:
    input_data = f"Вводные данные для H2O:\nmass H - {mass_H}\nmass O - {mass_O}\n"
    file.write(input_data)
with open('chemist_2.txt', 'a', encoding='utf-8') as file_result:
    result = f"Молекулярная масса H2O: {molecular_mass} г/моль\n\n"
    file_result.write(result)

mass_C = 12.0 #Задача 2
mass_O = 16.0

molecular_mass = mass_C + 2 * mass_O
result_mass = molecular_mass
n_CO2 = result_mass / molecular_mass

with open('chemist_2.txt', 'a', encoding='utf-8') as file:
    input_data_2 = f"Вводные данные для CO2:\nmass C - {mass_C}\nmass O - {mass_O}\n"
    file.write(input_data_2)
with open('chemist_2.txt', 'a', encoding='utf-8') as file_result_2:
    result_2 = f"Количество молей в 44.0 г CO2: {n_CO2} моль\n\n"
    file_result_2.write(result_2)

mass_H2O = 18.0 #г/моль #Задача 3
mass_H2 = 2.0 #г/моль
mass_H2_sample = 10.0

n_H2 = mass_H2_sample / mass_H2
n_H2O = n_H2
mass_H2O_produced = n_H2O * mass_H2


with open('chemist_2.txt', 'a', encoding='utf-8') as file:
    input_data_3 = f"Вводные данные:\nmass H2O - {mass_H2O}\nmass H2 - {mass_H2}\nmass H2 sample - {mass_H2_sample}\n"
    file.write(input_data_3)
with open('chemist_2.txt', 'a', encoding='utf-8') as file_result_3:
    result_3 = f"Количество воды, образующееся из 10 г H2: {mass_H2O_produced} г\n\n"
    file_result_3.write(result_3)

mass_C = 12.0 #Задача 4
mass_O = 32.0
mass_sample = 5.0

molec_C = mass_sample / mass_C
mass_O2 = molec_C
mass_O2_result = mass_O2 * mass_O

with open('chemist_2.txt', 'a', encoding='utf-8') as file:
    input_data_4 = f"Вводные данные:\nmass C - {mass_C}\nmass O - {mass_O}\nmass sample - {mass_sample}\n"
    file.write(input_data_4)
with open('chemist_2.txt', 'a', encoding='utf-8') as file_result_4:
    result_4 = f"Масса кислорода, необходимое для реакции: {mass_O2_result:.2f} г\n\n"
    file_result_4.write(result_4)

mass_h2 = 3.0 #Задача 5
molar_mass_h2 = 2.0
molar_mass_nh3 = 17.0

moles_h2 = mass_h2 / molar_mass_h2
moles_nh3 = moles_h2 * (2 / 3)
mass_nh3 = moles_nh3 * molar_mass_nh3


with open('chemist_2.txt', 'a', encoding='utf-8') as file:
    input_data_5 = (f"Вводные данные:\nmass H2 - {mass_h2}\nmolar mass H2 - {molar_mass_h2}\n"
                    f"molar mass NH3 - {molar_mass_nh3}\n")
    file.write(input_data_5)
with open('chemist_2.txt', 'a', encoding='utf-8') as file_result_5:
    result_5 = f"Образуется {mass_nh3} г аммиака.\n\n"
    file_result_5.write(result_5)

mass_zn = 10.0 #Задача 6
molar_mass_zn = 65.38
vm = 22.4

moles_zn = mass_zn / molar_mass_zn
moles_h2 = moles_zn
v_h2 = moles_h2 * vm

with open('chemist_2.txt', 'a', encoding='utf-8') as file:
    input_data_6 = (f"Вводные данные:\n"
                    f"mass Zn - {mass_zn}\n"
                    f"molar mass Zn - {molar_mass_zn}\n"
                    f"molar V - {vm}\n")
    file.write(input_data_6)

with open('chemist_2.txt', 'a', encoding='utf-8') as file_result_6:
    result_6 = f"Из {mass_zn} г цинка можно получить {v_h2:.2f} л водорода.\n\n"
    file_result_6.write(result_6)

concentration_N2_initial = 1.0 #Задача 7
concentration_H2_initial = 3.0
order_N2 = 1
order_H2 = 3

def reaction_rate(concentration_N2, concentration_H2):
    k = 1
    return k * (concentration_N2 ** order_N2) * (concentration_H2 ** order_H2)

initial_rate = reaction_rate(concentration_N2_initial, concentration_H2_initial)

concentration_N2_new = concentration_N2_initial / 2
concentration_H2_new = concentration_H2_initial / 2
new_rate = reaction_rate(concentration_N2_new, concentration_H2_new)

with open('chemist_2.txt', 'a', encoding='utf-8') as file:
    input_data_8 = (f"Вводные данные:\n"
                   f"Начальная концентрация N2: {concentration_N2_initial} моль/л\n"
                   f"Начальная концентрация H2: {concentration_H2_initial} моль/л\n"
                   f"Порядок по N2: {order_N2}\n"
                   f"Порядок по H2: {order_H2}\n")
    file.write(input_data_8)

with open('chemist_2.txt', 'a', encoding='utf-8') as file_result_8:
    result_8 = (f"Скорость реакции до увеличения объёма: {initial_rate:.2f} моль/л·с\n"
              f"Скорость реакции после увеличения объёма: {new_rate:.2f} моль/л·с\n"
              f"Скорость реакции уменьшилась в {initial_rate / new_rate:.2f} раз\n")
    file_result_8.write(result_8)

