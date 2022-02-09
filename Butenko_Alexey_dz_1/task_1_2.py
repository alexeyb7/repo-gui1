

def sum_list_1(dataset: list) -> int:
    sum_del_7_1: int = 0
    for i in range (len(dataset)):
        sum = 0
        num = dataset[i]
        for i1 in range (len(str(num))):
            element = str(dataset[i]) # преобразует элемент списка число в строку
            sum = sum + int(element[i1]) # складывает цифры элемента списка
        if sum % 7 == 0: # проверка деления на 7
            sum_del_7_1 += dataset[i]
    return sum_del_7_1
#
def sum_list_2(dataset: list) -> int:
    sum_del_7_2: int = 0
    for i in range (len(dataset)):
        sum = 0
        num = dataset[i]+17
        for i1 in range (len(str(num))):
            element = str(num)
            sum = sum + int(element[i1])
        if sum % 7 == 0:
            sum_del_7_2 += num
    return sum_del_7_2


my_list = []  # Соберите нужный список по заданию
for indx_list in range(1, 1000, 2): # для нечетных чисел
    my_list.append(indx_list**3) # сборка списка кубов

result_1 = sum_list_1(my_list)
print('сумма:', result_1)
result_2 = sum_list_2(my_list)
print('сумма +17:', result_2)