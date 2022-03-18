import os
from itertools import zip_longest
# рабочая папка
folder = 'some_data'
s1 = []
s = []

for i in range (1, 6):
    size_threshold1 = 10**(i-1)
    size_threshold = 10**i
# формирование списков ключей и значений
    small_files_2 = [item.name
            for item in os.scandir(folder)
            if size_threshold1 < item.stat().st_size < size_threshold]
    s1.append(str(len(small_files_2)))
    s.append(str(size_threshold))
# формирование словаря
result = {}
result = dict(zip_longest(s,s1))

print (result)


