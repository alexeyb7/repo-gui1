import os

# создание списка папок, при необходимости на будущее - вложенные папки в dir_dir_list
root_name = 'my_project'
dir_list = ['settings', 'mainapp','adminapp', 'authapp']
dir_dir_list = ['']

if not os.path.exists(root_name):
   os.mkdir(root_name)

for i in dir_list:
   for i1 in dir_dir_list:
      dir_path = os.path.join(root_name, i, i1)
      if not os.path.exists(dir_path):
         os.makedirs(dir_path)