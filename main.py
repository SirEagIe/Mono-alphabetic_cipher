# Поменять в строке n и n+1 символы
def switch_sym_with_next(string, n):
    string = ''.join([string[:n], string[n + 1], string[n], string[n + 2:len(string)]])
    return string


alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
frequency_ordered_letters = 'оеаинтсрвлкмдпуяыьгзбчйхжшюцщэфёъ'
string = 'Тест'
frequency_ordered_letters_in_text = alphabet
amount = [0] * 33
# Подсчёт встречаемости букв в заданном тексте
for i in range(0, len(string)):
    for j in range(0, len(alphabet)):
        if string[i] == alphabet[j] or string[i] == alphabet[j].upper():
            amount[j] += 1
# Сортировка
for i in range(0, len(alphabet)):
    for j in range(0, len(alphabet) - 1):
        if amount[j] < amount[j + 1]:
            amount[j], amount[j + 1] = amount[j + 1], amount[j]
            frequency_ordered_letters_in_text = switch_sym_with_next(frequency_ordered_letters_in_text, j)
# Отладка
print(frequency_ordered_letters_in_text)
print(amount)
# Замена букв в тексте
new_string = ''
for i in range(0, len(string)):
    if alphabet.find(string[i]) != -1:
        new_string += frequency_ordered_letters[frequency_ordered_letters_in_text.find(string[i])]
    elif alphabet.upper().find(string[i]) != -1:
        new_string += frequency_ordered_letters[frequency_ordered_letters_in_text.upper().find(string[i])].upper()
    else:
        new_string += string[i]
print(new_string)
