# Поменять в строке n и n+1 символы
def switch_sym_with_next(string, n):
    string = ''.join([string[:n], string[n + 1], string[n], string[n + 2:len(string)]])
    return string


alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
frequency_ordered_letters = 'оеаинтсрвлкмдпуяыьгзбчйхжшюцщэфёъ'
try:
    file = open('ciphertext.txt', 'r', encoding="utf-8")
except IOError as e:
    print('Не удалось открыть файл!')
    exit()
frequency_ordered_letters_in_text = alphabet
amount = [0] * 33
# Подсчёт встречаемости букв в заданном тексте
while True:
    ch = file.read(1)
    if ch == '':
        break
    for i in range(0, len(alphabet)):
        if ch == alphabet[i] or ch == alphabet[i].upper():
            amount[i] += 1
# Сортировка
for i in range(0, len(alphabet)):
    for j in range(0, len(alphabet) - 1):
        if amount[j] < amount[j + 1]:
            amount[j], amount[j + 1] = amount[j + 1], amount[j]
            frequency_ordered_letters_in_text = switch_sym_with_next(frequency_ordered_letters_in_text, j)
# Отладка
print(frequency_ordered_letters_in_text)
print(amount)
# Замена букв в тексте в соответствии с частотным анализом
file.seek(0)
new_string = ''
while True:
    ch = file.read(1)
    if ch == '':
        break
    if alphabet.find(ch) != -1:
        new_string += frequency_ordered_letters[frequency_ordered_letters_in_text.find(ch)]
    elif alphabet.upper().find(ch) != -1:
        new_string += frequency_ordered_letters[frequency_ordered_letters_in_text.upper().find(ch)].upper()
    else:
        new_string += ch
print(new_string)
# Дополнительные замены
while True:
    print('\nДополнительные замены ("exit" для выхода)')
    print("Заменить: ")
    first_char = input().lower()
    if first_char == 'exit':
        file_output = open('planetext.txt', 'w', encoding='utf-8')
        file_output.write(new_string)
        file.close()
        file_output.close()
        exit()
    print("И: ")
    second_char = input().lower()
    if len(first_char) != 1 or len(second_char) != 1 or alphabet.find(first_char) == -1 or alphabet.find(
            second_char) == -1:
        print("Данные введены неверно\n")
        input()
    else:
        new_string = new_string.replace(first_char, '***').replace(second_char, first_char).replace('***', second_char)
        new_string = new_string.replace(first_char.upper(), '***').replace(second_char.upper(),
                                                                           first_char.upper()).replace('***',
                                                                                                       second_char.upper())
    print(new_string)
