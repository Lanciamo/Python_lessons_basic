# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

# '''

def fibonacci(n, m):
    fibb_row = [1, 1]
    i = 0
    while i <= m:
        fibb_row.append(fibb_row[-1] + fibb_row[-2])
        i += 1
    return fibb_row[n:m]

print(fibonacci(5, 10))

# '''

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

# '''
def sort_to_max(n):
    for i in range(len(n)-1):
        for j in range(len(n)-1):
            if n[j] > n[j+1]:
                n[j], n[j+1] = n[j+1], n[j]
    return n

print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

# '''
# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

''' НЕ РЕШИЛ(
def myfil(j, n):
    if j(n) == True:
        return True
    else:
        return False



def numbs(x):
    if '0' <= x <= '9':
        return 1
    else:
        return 0

s = "5a 3 k 99 d00"

print(filter(numbs,s))
# '''
# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

x1 = 3
y1 = 3

x2 = 4
y2 = 4

x3 = 4
y3 = 2

x4 = 5
y4 = 3

if x2 - x1 == x4 - x3 and x3 - x1 == x4 - x3 and y2 - y1 == y4 - y3 and y1 - y3 == y2 - y4:
    print('This is the set of points of one parallelogram')
else:
    print('This set of points is not points of parallelogram')