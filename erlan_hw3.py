class Fraction:
    def __init__(self, num,dannum):
        self.num = num
        self.dannum = dannum

    def __add__(self, other):
        self.num += other
        self.dannum += other
        print("_add_ Method",self.num)

    def __sub__(self, other):
        self.num -= other
        self.dannum -= other
        print("sub Method",self.num)

    def __mul__(self, other):
        self.num *= other
        self.dannum *= other
        print("mul Method",self.num)

    def __floordiv__(self, other):
        self.num //= other
        self.dannum //= other
        print("floordiv Method",self.num)


num = Fraction(6,6)

num.__add__(1.2)
num.__sub__(4.1)
num.__mul__(2.0)
num.__floordiv__(1.8)
