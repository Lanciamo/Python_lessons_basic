# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
# '''
class Triangle:
    def __init__(self, tops):
        self.tops = tops
        if len(tops) != 3:
            print('ERROR!')

    def get_side_lenght(self, a, b):
        return (abs(b[0] - a[0]) ** 2 + abs(b[1] - a[1]) ** 2) ** 0.5

    @property
    def sides(self):
        side = []
        for i in range(len(self.tops)):
            side.append(self.get_side_lenght(self.tops[i], self.tops[(i + 1) % len(self.tops)]))
            # print(self.tops[i], self.tops[(i + 1) % len(self.tops)])
        return side

    @property
    def perimeter(self):
        return sum(self.sides)

    # возвращает список высот
    def high(self, high_num=None):
        if not -1 < high_num < 3 or type(high_num) != int:
            print('Введите верный номер вершины треугольника (0, 1, 2)')
            return False

        p = self.perimeter / 2
        h = []
        side = self.sides

        for i in side:
            h.append(round((2 * (p * (p - side[0]) * (p - side[1]) * (p - side[2])) ** 0.5) / i, 3))

        return h[high_num]

    @property
    def square(self):
        # print(self.sides[1] * self.high(1) / 2)
        return round(self.sides[0] * self.high(0) / 2, 4)


tr_1 = Triangle(((0, 0), (1, 1), (2, 0)))
print(tr_1.tops)
print(tr_1.perimeter)
print(tr_1.high(0))
print(tr_1.square)
print(tr_1.sides)
# '''
# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class Trapezium:
    def __init__(self, tops):
        self.tops = tops
        if len(tops) != 4:
            print('ERROR!')
            return False

    def get_side_lenght(self, a, b):
        return (abs(b[0] - a[0]) ** 2 + abs(b[1] - a[1]) ** 2) ** 0.5

    @property
    def sides(self):
        side = []
        for i in range(len(self.tops)):
            side.append(self.get_side_lenght(self.tops[i], self.tops[(i + 1) % len(self.tops)]))
            # print(self.tops[i], self.tops[(i + 1) % len(self.tops)])
        return side

    @property
    def perimeter(self):
        return sum(self.sides)

    def get_hor_lines(self): # так до конца и не понял зачем это возвращать координаты не равных линий(

        arrX = list(map(lambda x: x[1], self.tops))
        # print('!!!', arrX, self.tops)

        for i in self.tops:
            # print(arrX.count(i[0]))
            if arrX.count(i[1]) != 2:
                return False

        line2 = list(self.tops)
        line1 = [line2[0]]
        line2.pop(0)

        for i in line2:
            if line1[0][1] == i[1]:
                line1.append(i)
                line2.remove(i)

        # line1 = sorted(line1)
        # line2 = sorted(line2)
        # print(line1, line2)
        return line1, line2

    def is_right(self):
        if set(self.sides) == len(self.sides):
            return False

        return True

    @property
    def square(self):
        line1, line2 = self.get_hor_lines()
        line = (line1[1][0] - line1[0][0], line2[1][0] - line2[0][0])
        # print('line', line)

        arrY = [x[1] for x in self.tops]

        h = max(arrY) - min(arrY)
        # print(arrY, max(arrY), min(arrY), h, sum(line))

        return h * sum(line) / 2




trap_1 = Trapezium(((1, 5), (3, 1), (5, 1), (7, 5)))
print(trap_1.is_right())
print(trap_1.perimeter)
print(trap_1.square)
print(trap_1.sides)