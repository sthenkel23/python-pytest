import pytest
from time import sleep
from src.mylib.fruits import random_fruit


@pytest.mark.xdist_group(name="group")
def test_random_fruit_no_fixture():
    assert random_fruit() in ["apple", "banana", "orange"]


@pytest.mark.xdist_group(name="slow_group1")
@pytest.mark.skip(reason="too slow")
def test_random_fruit_slow():
    sleep(3)
    assert random_fruit() in ["apple", "banana", "orange"]
