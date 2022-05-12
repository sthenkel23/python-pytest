from random import choices


def unity(s: str = "Hello World!") -> str:
    return s


def fruit():
    fruits = ['apple', 'banana', 'orange']
    return choices(fruits)[0]
