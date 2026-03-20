V_NaCl_initial = 500
W_NaCl_initial = 0.20
P_NaCl_initial = 1.152
W_NaCl_final = 0.045
P_NaCl_final = 1.029

m_1 = V_NaCl_initial * P_NaCl_initial
m_NaCl =W_NaCl_initial * m_1
V  = m_NaCl / (W_NaCl_final *  P_NaCl_final)


with open('chemist.txt', 'w', encoding='utf-8') as file:
    input_data = (
        f"Вводные данные:\nNaCl_V_in - {V_NaCl_initial}\nNaCl_W_in - {W_NaCl_initial}"
        f"\nNaCl_P_in - {P_NaCl_initial}\nNaCl_W_fin - {W_NaCl_final}\nNaCl_P_fin - {P_NaCl_final} " )
    file.write(input_data)
with open('chemist.txt', 'a', encoding='utf-8') as file_result:
    result = f"Необходимо разбавить до {V: .2f} cм3"
    file_result.writelines(str(result))