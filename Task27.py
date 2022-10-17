# 3. Написать функцию, аргументы имена сотрудников, возвращает словарь,
#    ключи — первые буквы имён, значения — списки, содержащие имена,
#    начинающиеся с соответствующей буквы.

def thesaurus(*args):
    names_dict = {}
    for i in sorted(args):
        letter = i[0]
        if letter not in names_dict:
            names_dict[letter] = [i]
        names_dict[letter] += [i]

    return names_dict


print(thesaurus("Иван", "Мария", "Петр", "Илья", "Марина", "Алина", "Бибочка"))