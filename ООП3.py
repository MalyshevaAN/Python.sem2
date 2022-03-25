import math


def summory(n):
    s = 0
    for i in range(1, n + 1):
        s = s + 1 / i
    return s


class Rational:

    @staticmethod
    def statics():
        zero = 0.0
        one = 1.0
        return zero, one


    def __init__(self, _n, _d=1):
        self.numerator = _n
        self.denominator = _d

    def __str__(self):
        if self.numerator == 0:
            return 0
        elif self.denominator == 1:
            return self.numerator
        else:
            return f"{self.numerator}/{self.denominator}"

    def as_number(self):
        m = self.numerator / self.denominator
        return m

    def gcd(self):
        if self.denominator < 0:
            self.numerator = -self.numerator
            self.denominator = -self.denominator
        nod = math.gcd(abs(self.numerator), abs(self.denominator))
        self.numerator = self.numerator // nod
        self.denominator = self.denominator // nod

    def __add__(self, other):
        x = self.numerator * other.denominator + other.numerator * self.denominator
        y = self.denominator * other.denominator
        r3 = Rational(x, y)
        r3.gcd()
        return r3

    def __iadd__(self, other):
        self.numerator = self.numerator * other.denominator + other.numerator * self.denominator
        self.denominator = self.denominator * other.denominator
        self.gcd()
        return self

    def __sub__(self, other):
        x = self.numerator * other.denominator - other.numerator * self.denominator
        y = self.denominator * other.denominator
        r3 = Rational(x, y)
        r3.gcd()
        return r3

    def __isub__(self, other):
        self.numerator = self.numerator * other.denominator - other.numerator * self.denominator
        self.denominator = self.denominator * other.denominator
        self.gcd()
        return self

    def __mul__(self, other):
        x = self.numerator * other.numerator
        y = self.denominator * other.denominator
        r3 = Rational(x, y)
        r3.gcd()
        return r3

    def __imul__(self, other):
        self.numerator = self.numerator * other.numerator
        self.denominator = self.denominator * other.denominator
        self.gcd()
        return self

    def __truediv__(self, other):
        x = self.numerator * other.denominator
        y = self.denominator * other.numerator
        r3 = Rational(x, y)
        r3.gcd()
        return r3

    def __itruediv__(self, other):
        self.numerator = self.numerator * other.denominator
        self.denominator = self.denominator * other.numerator
        self.gcd()
        return self

    def __pow__(self, p):
        x = 1
        y = 1
        for i in range(p):
            x *= self.numerator
            y *= self.denominator
        r3 = Rational(x, y)
        r3.gcd()
        return r3

    def __ipow__(self, p):
        self.gcd()
        x = self.numerator
        y = self.denominator
        for i in range(p - 1):
            self.numerator *= x
            self.denominator *= y
        return self

    def __eq__(self, other):
        return isinstance(other, Rational) and self.numerator * other.denominator == other.numerator * self.denominator

    def __ne__(self, other):
        return isinstance(other, Rational) and not self.__eq__(other)

    def __lt__(self, other):
        return isinstance(other, Rational) and self.numerator * other.denominator < other.numerator * self.denominator

    def __le__(self, other):
        return isinstance(other, Rational) and self.__eq__(other) or self.__lt__(other)

    def __gt__(self, other):
        return isinstance(other, Rational) and not self.__le__(other)

    def __ge__(self, other):
        return isinstance(other, Rational) and self.__gt__(other) or self.__eq__(other)



number1 = Rational(1, 6)
print(number1.__str__())
print(number1.__str__())
print(number1.as_number())
number2 = Rational(1, 3)
print(summory(number2.denominator))
number3 = number1.__add__(number2)
number4 = number1 - number2
print(number3.__str__())
print(number4.__str__())
number1 += number2
print(number1)
number5 = number1 ** 3
print(number5.__str__())
number1 **= 3
print(number1)
r1 = Rational(1, 3)
r2 = Rational(3, 8)
print(r1.__ne__(r2))
print(summory(3))


