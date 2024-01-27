from src.keyboard import Keyboard
import pytest


@pytest.fixture()
def fixture_class_keyboard():
    return Keyboard('default keyboard', 100, 5)


def test_init(fixture_class_keyboard):
    assert fixture_class_keyboard.name == 'default keyboard'
    assert fixture_class_keyboard.price == 100
    assert fixture_class_keyboard.quantity == 5
    assert fixture_class_keyboard.language == 'EN'


def test_str(fixture_class_keyboard):
    assert str(fixture_class_keyboard) == 'default keyboard'
    assert str(fixture_class_keyboard.language) == 'EN'


def test_change_lang(fixture_class_keyboard):
    fixture_class_keyboard.change_lang()
    assert fixture_class_keyboard.language == 'RU'
    fixture_class_keyboard.change_lang()
    assert fixture_class_keyboard.language == 'EN'
    if fixture_class_keyboard.language == 'EU':
        assert AttributeError
