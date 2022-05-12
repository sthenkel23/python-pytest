from src.mylib.fruits import random_fruit


def test_random_fruit():
    assert random_fruit() in ["apple", "banana", "orange"]