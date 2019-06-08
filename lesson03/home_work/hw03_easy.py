# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

# '''
def my_round(number, ndigits):
    number = str(number)
    do_eq = number.find('.')
    if float(number[do_eq + ndigits + 2]) >= 5:
        after_eq = (float(number[:do_eq + ndigits + 1]) * 10 ** ndigits + 1) / 10 ** ndigits
    else:
        after_eq = number[:do_eq + ndigits + 1]
    return after_eq
print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))
# '''

# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить
# '''
def lucky_ticket(ticket_number):
    i = int(len(str(ticket_number)) / 2)
    b = list(map(int, str(ticket_number)))
    if len(str(ticket_number)) % 2 != 0:
        return f'The ticket with number {ticket_number} could not be Lucky or UnLucky'
    else:
        if sum(b[:i]) != sum(b[i:]):
            return f'The Ticket with number {ticket_number} is UnLucky'
        else:
            return f'The Ticket with number {ticket_number} is Lucky'

print(lucky_ticket(12300634))
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))

# '''