""" __main__ """

from toycoin.ecc import FieldElement

if __name__ == "__main__":
    a = FieldElement(7, 13)
    b = FieldElement(8, 13)

    print(a**-3 == b)
