import pytest
from arquivo import Fruit

@pytest.fixture()
def my_fruit():
    return Fruit("apple")

@pytest.fixture()
def fruit_basket(my_fruit):
    return [Fruit("banana"), my_fruit]