# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

# import os
import sys
# import shutil
import hw05_easy as easy

# easy.del_dirs()

print(sys.path)

# '''

def render_menu():
    menu = ['1. Перейти в папку',
            '2. Show current dir',
            '3. Make 9 dirs',
            '4. Del 9 dirs',
            '5. Make copy of this file',
            '7. Ciao',
            ]
    print()
    for item in menu:
        print(item)


do = {'1': easy.cd,
      '2': easy.show_dirs,
      '3': easy.make_dirs,
      '4': easy.del_dirs,
      '5': easy.cop_the_file,
      }


def run():
    while True:
        render_menu()

        key = input('Выбор: ')
        if key == '7':
            print('Ciao!')
            break

        if key in do.keys():
            do[key]()

        else:
            print('невернный ввод')


if __name__ == '__main__':
    run()

# '''