from pprint import pprint


def get_parse_attrs(line: str) -> tuple:
    """Парсит строку на атрибуты и возвращает кортеж атрибутов (<remote_addr>, <request_type>, <requested_resource>)"""
#    pass  # Ваша реализация здесь
    str_spl = line.split()
    return  str_spl[0], str_spl[5].lstrip('"'), str_spl[6]# верните кортеж значений <remote_addr>, <request_type>, <requested_resource>


list_out = list()
with open('nginx_logs.txt', 'r', encoding='utf-8') as fr:
    pass  # передавайте данные в функцию и наполняйте список list_out кортежами
    for line in fr:
        list_out.append(get_parse_attrs(line))

pprint(list_out)