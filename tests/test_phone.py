import pytest
from src.phone import Phone


@pytest.fixture
def fixture_class_phone():
    return Phone('iphone', 1200, 3, 2)


def test_init(fixture_class_phone):
    assert fixture_class_phone.name == 'iphone'
    assert fixture_class_phone.price == 1200
    assert fixture_class_phone.quantity == 3
    assert fixture_class_phone.number_of_sim == 2


def test_str_and_repr(fixture_class_phone):
    assert str(fixture_class_phone) == 'iphone'
    assert repr(fixture_class_phone) == "Phone('iphone', 1200, 3, 2)"
