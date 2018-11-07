class Dist:
    def __init__(self, mt, ct):
        self.meters = mt
        self.centimeters = ct

    def get_dist(self):
        self.meters = int(input("Введите число метров: "))
        self.centimeters = int(input("Введите число сантиметров: "))

    def __str__(self):
        return "{} м {} см".format(self.meters, self.centimeters)

    def __format__(self, format_spec):
        return "{0:{1}}".format(self.__str__(), format_spec)

    def __add__(self, other):
        met = self.meters + other.meters
        cent = self.centimeters + other.centimeters
        if cent >= 100.:
            cent -= 100.
            met += 1
        return Dist(met, cent)

    def __sub__(self, other):
        met = self.meters - other.meters
        cent = self.centimeters - other.centimeters
        if cent < 0.:
            cent += 100.
            met -= 1
        return Dist(met, cent)

    def __mul__(self, other):
        self_decimal = float(self)
        other_decimal = float(other)
        res_decimal = self_decimal * other_decimal
        res_meters = int(res_decimal)
        return Dist(res_meters, round(res_decimal - res_meters, 2))

    def __truediv__(self, other):
        other_decimal = float(other)
        if other_decimal == 0:
            raise ZeroDivisionError("Делитель не может иметь нулевое значение")
        self_decimal = float(self)
        res_decimal = float(self_decimal / other_decimal)
        res_meters = int(res_decimal)
        return Dist(res_meters, round(res_decimal - res_meters, 2))

    def __iadd__(self, other):
        self.meters += other.meters
        self.centimeters += other.centimeters
        if self.centimeters >= 100.:
            self.centimeters -= 100.
            self.meters += 1
        return self

    def __lt__(self, other):
        bd1 = float(self)
        bd2 = float(other)
        return bd1 < bd2

    def __le__(self, other):
        bd1 = float(self)
        bd2 = float(other)
        return bd1 <= bd2

    def __eq__(self, other):
        bd1 = float(self)
        bd2 = float(other)
        return bd1 == bd2

    def __ne__(self, other):
        bd1 = float(self)
        bd2 = float(other)
        return bd1 != bd2

    def __gt__(self, other):
        bd1 = float(self)
        bd2 = float(other)
        return bd1 > bd2

    def __ge__(self, other):
        bd1 = float(self)
        bd2 = float(other)
        return bd1 >= bd2

    def __float__(self):
        return float(self.meters + self.centimeters / 100.)

    def __int__(self):
        return int(self.meters + self.centimeters / 100.)


class LongDist(Dist):
    def __init__(self, km, mt, ct):
        super().__init__(mt, ct)
        self.kilometers = km

    def __add__(self, other):
        res = super(LongDist, self).__add__(other)
        res.kilometers = self.kilometers + other.kilometers

        return res

    def get_dist(self):
        self.centimeters = int(input("Введите число метров: "))
        self.meters = int(input("Введите число сантиметров: "))


if __name__ == "__main__":
    a = LongDist(25, 25, 11)
    b = LongDist(50, 50, 22)
    print(repr(a))
    # b.get_dist()
    c = a + b
    print(c)
    print(type(c))
