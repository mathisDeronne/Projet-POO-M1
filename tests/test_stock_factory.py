from pytest import fixture, mark
from src.farm.stock_factory import Stock


@fixture
def base_stock_data():
    return {
        "POTATO": 2000,
        "LEEK": 0,
        "TOMATO": 2000,
        "ONION": 0,
        "ZUCCHINI": 0,
    }


def test_base_stock(base_stock_data):
    stock = Stock(base_stock_data)
    assert stock.have_potato() is True
    assert stock.have_leek() is False
    assert stock.have_tomato() is True
    assert stock.have_onion() is False
    assert stock.have_zucchini() is False
    assert stock.have_stocks() is True


@mark.parametrize(
    "value, expected",
    [
        (2000, True),
        (+300, True),
        (0, False),
        (-0, False),
        (10.00, False),
        (-100, False),
        (-100.0, False),
        ("1000", False),
        ("test", False),
    ],
)
def test_stock_potato(base_stock_data, value, expected):
    base_stock_data["POTATO"] = value
    field = Stock(base_stock_data)
    assert field.have_potato() is expected


@mark.parametrize(
    "value, expected",
    [
        (2000, True),
        (+300, True),
        (0, False),
        (-0, False),
        (10.00, False),
        (-100, False),
        (-100.0, False),
        ("1000", False),
        ("test", False),
    ],
)
def test_stock_leek(base_stock_data, value, expected):
    base_stock_data["LEEK"] = value
    field = Stock(base_stock_data)
    assert field.have_leek() is expected


@mark.parametrize(
    "value, expected",
    [
        (2000, True),
        (+300, True),
        (0, False),
        (-0, False),
        (10.00, False),
        (-100, False),
        (-100.0, False),
        ("1000", False),
        ("test", False),
    ],
)
def test_stock_tomato(base_stock_data, value, expected):
    base_stock_data["TOMATO"] = value
    field = Stock(base_stock_data)
    assert field.have_tomato() is expected


@mark.parametrize(
    "value, expected",
    [
        (2000, True),
        (+300, True),
        (0, False),
        (-0, False),
        (10.00, False),
        (-100, False),
        (-100.0, False),
        ("1000", False),
        ("test", False),
    ],
)
def test_stock_onion(base_stock_data, value, expected):
    base_stock_data["ONION"] = value
    field = Stock(base_stock_data)
    assert field.have_onion() is expected


@mark.parametrize(
    "value, expected",
    [
        (2000, True),
        (+300, True),
        (0, False),
        (-0, False),
        (10.00, False),
        (-100, False),
        (-100.0, False),
        ("1000", False),
        ("test", False),
    ],
)
def test_stock_zucchini(base_stock_data, value, expected):
    base_stock_data["ZUCCHINI"] = value
    field = Stock(base_stock_data)
    assert field.have_zucchini() is expected
