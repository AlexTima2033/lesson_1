"""massa_H = 1.0
massa_О = 16.0
molecular_mass = 2 * massa_H + massa_О
print(f"Молекулярная масса веществ {molecular_mass} г/моль")"""

"""massa_C = 12.0
massa_О = 16.0
molecular_mass = massa_C + 2 * massa_О
print(molecular_mass)
result_mass = molecular_mass
n_CO2 = result_mass / molecular_mass
print(f"Количество молей в 44.0 г: {n_CO2} моль")"""

"""massa_H2O = 18.0 #г/моль
massa_H2 = 2.0 #г/моль
massa_H2_sample = 10.0
n_H2 = massa_H2_sample / massa_H2
n_H2O = n_H2
massa_H2O_produced = n_H2O * massa_H2
print(f"Количество воды, образующееся из 10 г H2: {massa_H2O_produced} г")"""

"""massa_C = 12.0
massa_O = 32.0
massa_sample = 5.0
molec_C = massa_sample / massa_C
massa_O2 = molec_C
massa_O2_result = massa_O2 * massa_O
print(f"Масса кислорода, необходимое для реакции: {massa_O2_result:2f} г")"""

"""mass_h2 = 3.0
molar_mass_h2 = 2.0
molar_mass_nh3 = 17.0
moles_h2 = mass_h2 / molar_mass_h2
moles_nh3 = moles_h2 * (2 / 3)
mass_nh3 = moles_nh3 * molar_mass_nh3
print(f"Образуется {mass_nh3} г аммиака")"""

mass_zn = 10.0
molar_mass_zn = 65.38
vm = 22.4
moles_zn = mass_zn / molar_mass_zn
moles_h2 = moles_zn
v_h2 = moles_h2 * vm
print(f"Из {mass_zn} г цинка можно получить {v_h2:.2f} л водорода.")



