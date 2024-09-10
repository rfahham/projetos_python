import pytest
from arquivo import Fruit

@pytest.fixture()
def my_fruit():
    return Fruit("apple")

@pytest.fixture()
def fruit_basket(my_fruit):
    return [Fruit("banana"), my_fruit]
    
def test_my_fruit_in_basket(my_fruit, fruit_basket):
    assert my_fruit in fruit_basket