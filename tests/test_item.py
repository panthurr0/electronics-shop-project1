import pytest
from src.item import Item


@pytest.fixture
def fixture_class_item():
    return Item("Смартфон", 10000, 20)


@pytest.fixture
def fixture_class_item_2():
    return Item('Ноутбук', 100, 666)


def test_check_len_item_all_if_len_zero():
    assert len(Item.all) == 0


def test_check_len_item_all_if_len_one(fixture_class_item):
    assert len(Item.all) == 1


def test_init_object_item(fixture_class_item):
    assert fixture_class_item.name == "Смартфон"
    assert fixture_class_item.price == 10000
    assert fixture_class_item.quantity == 20


def test_sum_total_price(fixture_class_item, fixture_class_item_2):
    assert fixture_class_item.calculate_total_price() == 10000 * 20
    assert fixture_class_item_2.calculate_total_price() == 100 * 666


def test_pay_rate(fixture_class_item, fixture_class_item_2):
    fixture_class_item.pay_rate = 0.5
    fixture_class_item.apply_discount()

    assert fixture_class_item.price == 10000 * 0.5
    assert fixture_class_item_2.price == 100
    assert fixture_class_item.pay_rate == 0.5


def test_item_all(fixture_class_item, fixture_class_item_2):
    for value in Item.all:
        assert isinstance(value, object)


def test_name(fixture_class_item):
    fixture_class_item.name = 'Планшет'

    assert fixture_class_item.name == 'Планшет'


def string_to_number():
    assert Item.string_to_number('82,34') == 82
    assert Item.string_to_number(80) == 80


