# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв". В тексте используется разделитель пробел.
# in
# Number of words: 10

# out
# авб абв бав абв вба бав вба абв абв абв
# авб бав вба бав вба

from random import choices, sample

def list_new(n, word):
    new_list =[]
    for i in range(n):
        a=sample(word,k=3)
        new_list.append(''.join(a))
    return new_list

def list_search(my_list):
    new_list = []
    i=0
    for i in range(len(my_list)):
        if my_list[i] != 'abc':
            new_list.append(my_list[i])
    return new_list

print(f'Введите количество слов:', )
result = list_new(int(input()), "abc")
print(f'Текст: ', " ".join(result))
print(f'Обработанный текст: ', " ".join(list_search(result)))