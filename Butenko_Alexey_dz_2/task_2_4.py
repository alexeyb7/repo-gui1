def convert_name_extract(list_in: list) -> list:
    """Извлекает имена из элементов и формирует список приветствий."""
    lst_out_tmp = []
    for i in list_in:
        lst_out_tmp.append('Привет, '+i.split(' ')[-1].capitalize()+'!')
    return lst_out_tmp


my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
result = convert_name_extract(my_list)
print(result)