
def transform_string(number: int) -> str:
    if number % 10 == 0 or 11 <= number <= 14:
        return str(number) + ' процентов'
    elif number % 10 == 1:
        return str(number) + ' процент'
    elif number % 10 <=4:
        return str(number) + ' процента'
    elif number % 10 <=9:
        return str(number) + ' процентов'
    #return 'верните отформатированную строку'


for n in range(1, 101):  # по заданию учитываем только значения от 1 до 100
    print(transform_string(n))

