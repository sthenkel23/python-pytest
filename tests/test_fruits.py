import pytest
from time import sleep
from src.mylib.fruits import Fruit, random_fruit


@pytest.fixture
def fruit_bowl():
    return [Fruit("apple"), Fruit("banana"), Fruit("orange")]

@pytest.mark.xdist_group(name="group")
def test_random_fruit_no_fixture():
    assert random_fruit() in ["apple", "banana", "orange"]

@pytest.mark.xdist_group(name="group")
def test_random_fruit_fixture(fruit_bowl):
    assert (
        fruit_bowl[0].my_fruit
        or fruit_bowl[1].my_fruit
        or fruit_bowl[2].my_fruit in random_fruit()
    )


@pytest.mark.xdist_group(name="slow_group1")
@pytest.mark.skip(reason="too slow")
def test_random_fruit_slow():
    sleep(3)
    assert random_fruit() in ["apple", "banana", "orange"]