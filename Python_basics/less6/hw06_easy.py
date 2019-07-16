# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

class triangle:
    def __init__(self, ax, ay, bx, by, cx, cy):
        self.ax = ax
        self.ay = ay
        self.bx = bx
        self.by = by
        self.cx = cx
        self.cy = cy

        def len_side(x1, y1, x2, y2):  # ф. для вычисления длины сторон
            from math import sqrt
            return round(abs(sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)))

        self.len_ab = len_side(self.ax, self.ay, self.bx, self.by)  #вычисляем длину ab
        self.len_ac = len_side(self.ax, self.ay, self.cx, self.cy)
        self.len_bc = len_side(self.bx, self.by, self.cx, self.cy)

    def p_abc(self):  # периметр
        return self.len_ab + self.len_ac + self.len_bc


    def s_abc(self):  # площадь через периметр и стороны
        from math import sqrt
        perim_abc = self.p_abc()
        return sqrt((perim_abc / 2) * ((perim_abc / 2) - self.len_ab) * ((perim_abc / 2) - self.len_ac) * (
                    (perim_abc / 2) - self.len_bc))

    def h_abc(self):  # высоты через площадь и стороны
        s_abc = self.s_abc()
        ha = round((2 * s_abc) / self.len_ab)
        hb = round((2 * s_abc) / self.len_bc)
        hc = round((2 * s_abc) / self.len_ac)
        return (ha, hb, hc)


my_trangle1 = triangle(1, 2, 10, 12, 1, 7)

print(my_trangle1.p_abc())
print(my_trangle1.s_abc())
print(my_trangle1.h_abc())
print('Задача-2')

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.
class trapecia:
    def __init__(self, ax, ay, bx, by, cx, cy, dx, dy):
        self.ax = ax
        self.ay = ay
        self.bx = bx
        self.by = by
        self.cx = cx
        self.cy = cy
        self.dx = dx
        self.dy = dy
        def len_side(x1, y1, x2, y2):  # ф. для вычисления длины сторон
            from math import sqrt
            return round(abs(sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)))

        self.len_ab = len_side(self.ax, self.ay, self.bx, self.by)  #вычисляем длину ab
        self.len_da = len_side(self.dx, self.dy, self.ax, self.ay)
        self.len_bc = len_side(self.bx, self.by, self.cx, self.cy)
        self.len_cd = len_side(self.cx, self.cy, self.dx, self.dy)

    def check_abcd(self):  # проверка на равнобочность
        if self.len_ab == self.len_cd or self.len_da == self.len_bc:
            x = 'равнобочная'
        else: x = 'не равнобочная'
        return x


    def p_abcd(self):  # периметр
        return (self.len_ab + self.len_bc + self.len_cd + self.len_da)


    @property
    def s_abcd(self):  # площадь
        from math import sqrt
        return round(((self.len_ab + self.len_cd) / 4) * sqrt(4 * sqrt(4 * (self.len_da ** 2) - ((self.len_ab - self.len_cd) ** 2))))



my_trapecia1 = trapecia(2, 6, 10, 6, 1, 1, 12, 1)

print('проверка на равнобочность: ', my_trapecia1.check_abcd)
print('p:', my_trapecia1.p_abcd)
print('s:', my_trapecia1.s_abcd)
print(my_trapecia1.len_ab, my_trapecia1.len_bc, my_trapecia1.len_cd, my_trapecia1.len_da)