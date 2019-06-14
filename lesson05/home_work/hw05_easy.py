# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
# '''

def make_dirs():
    for i in range(1, 10):
        os.mkdir(f'dir_{i}')

def del_dirs():
    for i in range(1, 10):
        os.removedirs(f'dir_{i}')

def show_dirs():
    print(os.listdir())

def cop_the_file():
    pass

print('1. Make 9 dirs')
print('2. Del 9 dirs')
print('3. Show dirs in current directory')
print(f'4. Make copy of this file {__name__}')
selector_menu = input('What option will you choose: ')
if selector_menu == '1':
    make_dirs()

if selector_menu == '2':
    del_dirs()

if selector_menu == '3':
    show_dirs()

if selector_menu == '4':
    cop_the_file()


'''
# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

# print(__name__)
'''
