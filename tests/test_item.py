import pytest
from src.item import Item
from src.phone import Phone
from tests.test_phone import fixture_class_phone


@pytest.fixture
def fixture_class_item():
    return Item('Смартфон', 10000, 20)


@pytest.fixture
def fixture_class_item_2():
    return Item('Ноутбук', 100, 34)


# @pytest.fixture
# def fixture_class_phone():
#     return Phone('iphone', 1200, 3, 2)


def test_check_len_item_all_if_len_zero():
    assert len(Item.all) == 0


def test_check_len_item_all_if_len_one(fixture_class_item):
    assert len(Item.all) == 1


def test_init_object_item(fixture_class_item):
    assert fixture_class_item.name == 'Смартфон'
    assert fixture_class_item.price == 10000
    assert fixture_class_item.quantity == 20


def test_sum_total_price(fixture_class_item, fixture_class_item_2):
    assert fixture_class_item.calculate_total_price() == 10000 * 20
    assert fixture_class_item_2.calculate_total_price() == 100 * 34


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


def test_str_and_repr():
    item1 = Item('Ноутбук', 52000, 3)
    assert str(item1) == 'Ноутбук'
    assert repr(item1) == "Item('Ноутбук', 52000, 3)"


def test_add(fixture_class_item, fixture_class_item_2, fixture_class_phone):
    phone1 = Phone('iphone_12', 500, 0, 1)
    assert fixture_class_phone + phone1 == 3
    assert fixture_class_item + fixture_class_phone == 23
    assert fixture_class_item + fixture_class_item_2 == 54
    if phone1.number_of_sim == 0:
        assert ValueError
