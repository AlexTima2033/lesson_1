"""delta_H_f = {
    'NH3': -45.9,
    'O2': 0.0,
    'NO': 90.3,
    'H2O': -241.8
}
products = 4 * delta_H_f['NO'] + 6 * delta_H_f['H2O']
reactants = 4 * delta_H_f['NH3'] + 5 * delta_H_f['O2']

delta_H_reaction = products - reactants

print(f"Реакции {delta_H_reaction:.2f} кДж")"""

"""concentration_N2_initial = 1.0
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


print(f"Скорость реакции до увеличения объёма: {initial_rate:.2f} моль/л.с")
print(f"Скорость реакции после увеличения объёма: {new_rate:.2f} моль/л.с")
print(f"Скорость реакции уменьшилась в {initial_rate / new_rate:.2f} раз")"""

V_1 = 500
W_1 = 0.20
P_1 = 1.152
W_2 = 0.045
P_2 = 1.029

m_1 = V_1 * P_1
m_NaCl =W_1 * m_1
V  = m_NaCl / (W_2 *  P_2)
print(f"Необходимо разбавить до {V: .2f} cм3")
