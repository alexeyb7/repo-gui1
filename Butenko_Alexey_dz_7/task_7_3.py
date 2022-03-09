from os import mkdir, sep, walk
from os.path import exists, join as path_join
from shutil import copy2

paths_files = {} # пути файлов
paths_dirs = [] # новые папки
base_dr = 'my_project'

for root, dirs, files in walk(base_dr):
    for file in files:
        if file.endswith('.html'):
            template = path_join(*root.split(sep)[-1:]) # название шаблона
            if template not in paths_files:
                paths_dirs.append(path_join(base_dr, 'templates', template))

            path_to_html = path_join(root, file)
            paths_files.update({path_to_html: path_join(base_dr, 'templates', template, file)})

# основная папка с шаблонами
if not exists(path_join(base_dr, 'templates')):
    mkdir(path_join(base_dr, 'templates'))

# папки шаблонов
for d in paths_dirs:
    if not exists(d):
        mkdir(d)
        print(f'Папка {d} создана')

for old, new in paths_files.items():
    if not exists(new):
        copy2(old, new)
        print(f'Файл {old} скопирован в {new}')