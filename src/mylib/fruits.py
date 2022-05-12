from random import choices


class Fruit:
    def __init__(self, name):
        self.my_fruit = name


def unity(s: str = "Hello World!") -> str:
    """_summary_

    :param s: _description_, defaults to "Hello World!"
    :type s: str, optional
    :return: _description_
    :rtype: str
    """
    return s


def random_fruit():
    """_summary_

    :return: _description_
    :rtype: _type_
    """
    fruits = ["apple", "banana", "orange"]
    return choices(fruits)[0]
