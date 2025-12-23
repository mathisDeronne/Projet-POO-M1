from pytest import fixture, mark
from src.farm.soup_factory import SoupFactory


@fixture
def base_soup_factory_data():
    return {
        "days_off": 0,
        "stock": {
            "POTATO": 0,
            "LEEK": 2000,
            "TOMATO": 0,
            "ONION": 2000,
            "ZUCCHINI": 0,
        },
    }


def test_base_soup_factory(base_soup_factory_data):
    soup_factory = SoupFactory(base_soup_factory_data)
    assert soup_factory.is_open() is True
    assert soup_factory.has_stock() is True


@mark.parametrize(
    "days_off, expected",
    [
        (0, True),
        (-0, True),
        (+0, True),
        (5, False),
        ("0", False),
        (0.0, False),
        (+0.0, False),
        (-0.0, False),
    ],
)
def test_days_off(base_soup_factory_data, days_off, expected):
    base_soup_factory_data["days_off"] = days_off
    soup_factory = SoupFactory(base_soup_factory_data)
    assert soup_factory.is_open() is expected


@mark.parametrize(
    "Legume, value, expected",
    [
        ("POTATO", 2000, True),
        ("LEEK", 100, True),
        ("TOMATO", 300, True),
        ("ONION", 100, True),
        ("ZUCCHINI", 5, True),
        ("POTATO", 0, False),
        ("LEEK", 0, False),
        ("TOMATO", -500, False),
        ("ONION", 0, False),
        ("ZUCCHINI", "test", False),
        ("POTATO", "2000", False),
        ("TOMATO", 400.0, False),
        ("ONION", +1000.0, False),
        ("ZUCCHINI", -200.0, False),
    ],
)
def test_have_stock(base_soup_factory_data, vegetable, value, expected):
    for vegetables in base_soup_factory_data["stock"]:
        base_soup_factory_data["stock"][vegetables] = 0

    base_soup_factory_data["stock"][vegetable] = value
    soup_factory = SoupFactory(base_soup_factory_data)
    assert soup_factory.has_stock() is expected
