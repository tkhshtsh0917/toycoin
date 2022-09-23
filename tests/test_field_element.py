""" Testing FieldElement """

from toycoin.ecc import FieldElement


def test_equal():
    """
    Testing eq method
    """

    element_1 = FieldElement(7, 13)
    element_2 = FieldElement(6, 13)
    element_3 = FieldElement(7, 13)

    assert element_1 != element_2
    assert element_1 == element_3


def test_add():
    """
    Testing add method
    """

    expected = FieldElement(20, 57)

    element_1 = FieldElement(44, 57)
    element_2 = FieldElement(33, 57)
    actual = element_1 + element_2

    assert expected == actual


def test_sub():
    """
    Testing sub method
    """

    expected = FieldElement(37, 57)

    element_1 = FieldElement(9, 57)
    element_2 = FieldElement(29, 57)
    actual = element_1 - element_2

    assert expected == actual
