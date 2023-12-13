import numpy as np


word = 'UFOPA'.upper()
key = np.array([[2, 1], [-1, 4]]) # Chave de criptografia
len_alphbt = 26
cod_letters = [ord(char) - ord('A') + 1 for char in word]
if len(word) % 2 != 0: cod_letters = cod_letters + [len_alphbt] # Completando com Z.
"""
    Criptografando a mensagem
"""
print(list(word))
print(cod_letters)
# Agrupando de dois em dois
cod_letters = np.array(cod_letters).reshape(-1, 2)

encrypted_msg = []
for group in cod_letters:
    # Multiplicando as matrizes e depois calcula resto da divisão por 26
    encrypted_msg.append(np.dot(key, group) % len_alphbt)
    
# Achatar a lista de arrays em uma única lista de números
encrypted_msg_flat = [num for array in encrypted_msg for num in array]

# Converter cada número em um caractere
encrypted_msg_chars = [chr(num + ord('A') - 1) for num in encrypted_msg_flat]

print(encrypted_msg_chars)
print([ord(dm) - ord('A') + 1 for dm in encrypted_msg_chars])

"""
    Descriptografando a mensagem
"""
# Matriz inversa da chave de criptografia
inverse_key = (10 * np.linalg.inv(key)).astype(int)

# Determinante da matriz da chave de criptografia
determinant = int(np.linalg.det(key))      

# Inverso modular do determinante da matriz inversa
mod_inverse = pow(determinant, -1, len_alphbt)

# Produto do inverso modular com a matriz inversa
product = np.dot(mod_inverse, inverse_key) 

# Resultado do módulo do produto do inverso modular com a matriz inversa
decrypt_key = product % len_alphbt 

decrypted_msg = []
for dec in encrypted_msg:
    decrypted_msg.extend([chr(msg + ord('A') - 1) if msg != 0 else chr(26 + ord('A') - 1) for msg in np.dot(decrypt_key, dec) % len_alphbt ])
print(decrypted_msg)
