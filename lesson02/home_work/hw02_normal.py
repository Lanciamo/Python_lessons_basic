# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]
# '''
import math
a = [2, -5, 8, 9, -25, 25, 4]
b = []
for i in a:
    if i > 0 and (math.sqrt(i)).is_integer():
        b.append(int(math.sqrt(i)))
print(b)
# '''

# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)

'''
mese = {'12':'декабря', '11':"ноября", '10':"октября", '09':"сентября", '08':"августа", '07':"июля",
        '06':"июня", '05':"мая", '04':"апреля", '03':"марта", '02':"февраля", '01':"января"}

oggi1 = {'9':'девятое', "8":"восьмое", "7":"седьмое", "6":"шестое", "5":"пятое", "4":"четвертое", "3":"третье",
         "2":"второе", "1":"первое", "0":"двадцатое"}

oggi2 = {'9':'девятнадцатое', "8":"восемнадцатое", "7":"семнадцатое", "6":"шестнадцатое", "5":"пятнадцатое",
         "4":"четырнадцатое", "3":"тринадцатое", "2":"двенадцатое", "1":"одиннадцатое", "0":"десятое"}
while True:
    user_data = input("Введите дату в формате dd.mm.yyyy, (например: 02.11.2013):  ")
    if len(user_data) != 10 or user_data[2] != '.' or user_data[5] != '.':
        print("ошибка ввода")
    elif int(user_data[0]) not in range(0, 4) or int(user_data[1]) not in range(0, 10) or int(user_data[3]) not in range(0, 2) or int(user_data[4]) not in range(0, 10) or int(user_data[6:10]) not in range(1, 2020):
        print("такой даты не бывает")
    else :
        # break
        if user_data[0] == '0':
            a = oggi1[user_data[1:2]]
        elif user_data[0] == '1':
            a = oggi2[user_data[1:2]]
        elif user_data[0] == '2' and user_data[1] != '0':
            a = 'двадцать' + oggi1[user_data[1:2]]
        else :
            a = oggi1[user_data[1:2]]
        print(a, mese[user_data[3:5]], user_data[6:10], 'года')
# '''
# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random
'''
import random
a = []
us_vol = int(input("Введите необходимое количество значений списка: "))
while us_vol > 0:
    a.append(random.randint(-100, 100))
    us_vol -= 1
print(a)
# '''
# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут: 
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]
# '''
aran = [1, 2, 4, 5, 6, 2, 5, 2, 8, 1]
print(aran)
bran = list(set(aran))
print('Ответ А', bran)
cran = list(aran)
for j, lran in enumerate(aran):
    for m in bran:
        if lran == m:
            aran.pop(j)
bran = list(set(cran) - set(aran))
print("Ответ Б", bran)
# '''