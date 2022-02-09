
list_digits = {'zero' : 'ноль', 'one' : 'один', 'two' : 'два', 'three' : 'три',
               'four' : 'четыре', 'five' : 'пять', 'six' : 'шесть', 'seven' : 'семь',
               'eight' : 'восемь', 'nine' : 'девять', 'ten' : 'десять'}

def num_translate(value: str) -> str:
    """переводит числительное с английского на русский """
    str_out = list_digits.get(value)
    return str_out


print(num_translate("one"))
print(num_translate("eight"))
print(num_translate("zero"))
print(num_translate("zer"))