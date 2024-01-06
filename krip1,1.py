import numpy as np

# Функция для аффинного шифрования
def affine_encrypt(text, key):
    result = ""
    for char in text:
        # Проверка, является ли символ буквой
        if char.isalpha():
            # Проверка, является ли буква заглавной
            if char.isupper():
                # Зашифровка для заглавных букв
                result += chr((key[0] * (ord(char) - 65) + key[1]) % 26 + 65)
            else:
                # Зашифровка для строчных букв
                result += chr((key[0] * (ord(char) - 97) + key[1]) % 26 + 97)
        else:
            # Не изменять не-буквенные символы
            result += char
    return result

# Функция для шифра Виженера
def vigenere_encrypt(text, key):
    result = ""
    key = key.upper()
    key_index = 0
    for char in text:
        # Проверка, является ли символ буквой
        if char.isalpha():
            # Вычисление сдвига для текущей буквы
            shift = ord(key[key_index]) - 65
            # Проверка, является ли буква заглавной
            if char.isupper():
                # Зашифровка для заглавных букв
                result += chr((ord(char) + shift - 65) % 26 + 65)
            else:
                # Зашифровка для строчных букв
                result += chr((ord(char) + shift - 97) % 26 + 97)
            # Обновление индекса ключа
            key_index = (key_index + 1) % len(key)
        else:
            # Не изменять не-буквенные символы
            result += char
    return result

# Функция для шифра Хилла
def hill_encrypt(text, key_matrix):
    result = ""
    # Преобразование текста в верхний регистр и удаление символов, не являющихся буквами
    text = ''.join([char.upper() for char in text if char.isalpha()])
    # Добавление необходимого количества "X" для выравнивания длины текста
    padding = len(text) % len(key_matrix)
    if padding > 0:
        text += 'X' * (len(key_matrix) - padding)

    # Преобразование текста в матрицу чисел (A=0, B=1, ..., Z=25)
    text_matrix = np.array([ord(char) - 65 for char in text])
    text_matrix = text_matrix.reshape((-1, len(key_matrix)))

    # Умножение матрицы текста на матрицу ключа и взятие по модулю 26
    encrypted_matrix = np.dot(text_matrix, key_matrix) % 26

    # Преобразование матрицы обратно в текст
    result = ''.join([chr(val + 65) for val in encrypted_matrix.flatten()])
    return result

# Пример использования
affine_key = (5, 7)
vigenere_key = "KEY"
hill_key_matrix = np.array([[6, 24, 1], [13, 16, 10], [20, 17, 15]])

original_text = "Soataliyev"

# Аффинный шифр
affine_result = affine_encrypt(original_text, affine_key)
print("Аффинный шифр:", affine_result)

# Шифр Виженера
vigenere_result = vigenere_encrypt(original_text, vigenere_key)
print("Шифр Виженера:", vigenere_result)

# Шифр Хилла
hill_result = hill_encrypt(original_text, hill_key_matrix)
print("Шифр Хилла:", hill_result)
