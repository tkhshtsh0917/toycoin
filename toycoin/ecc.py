""" Elliptic Curve Cryptography """


class FieldElement:
    """FieldElement"""

    def __init__(self, num, prime):
        if num >= prime or num < 0:
            error = f"Num {num} not in field range 0 to {prime-1}"
            raise ValueError(error)

        self.num = num
        self.prime = prime

    def __repr__(self):
        return f"FieldElement_{self.prime}({self.num})"

    def __eq__(self, other):
        if other is None:
            return False

        return self.num == other.num and self.prime == other.prime

    def __ne__(self, other):
        return not self == other

    def __add__(self, other):
        self.__check_prime(other, "add")

        num = (self.num + other.num) % self.prime
        return self.__class__(num, self.prime)

    def __sub__(self, other):
        self.__check_prime(other, "subtract")

        num = (self.num - other.num) % self.prime
        return self.__class__(num, self.prime)

    def __mul__(self, other):
        self.__check_prime(other, "multiply")

        num = (self.num * other.num) % self.prime
        return self.__class__(num, self.prime)

    def __pow__(self, exponent):
        exp = exponent % (self.prime - 1)
        num = pow(self.num, exp, self.prime)
        return self.__class__(num, self.prime)

    def __truediv__(self, other):
        self.__check_prime(other, "divide")

        num = self.num * pow(other.num, self.prime - 2, self.prime) % self.prime
        return self.__class__(num, self.prime)

    def __check_prime(self, other, calc_type):
        if self.prime != other.prime:
            raise TypeError(f"Cannot {calc_type} two numbers in different Fields")
