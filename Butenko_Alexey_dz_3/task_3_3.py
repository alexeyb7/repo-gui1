

def thesaurus(*args) -> dict:
    dict_out = {}  # результирующий словарь значений
    for i in args:
        if dict_out.get(i[0]) is None:
            dict_out.setdefault(i[0], [i])
        else:
            dict_out.get(i[0]).append(i)
    return dict_out


print(thesaurus("Иван", "Мария", "Петр", "Jenny", "Илья", "Марианна","John"))