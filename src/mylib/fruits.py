from random import choices


def random_fruit():
    """_summary_

    :return: _description_
    :rtype: _type_
    """
    fruits = ["apple", "banana", "orange"]
    return choices(fruits)[0]
