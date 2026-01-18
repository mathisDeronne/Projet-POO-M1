from pytest import fixture, mark  # type: ignore
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
    stock = Stock(base_stock_data)
    assert stock.have_potato() is expected


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
    stock = Stock(base_stock_data)
    assert stock.have_leek() is expected


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
    stock = Stock(base_stock_data)
    assert stock.have_tomato() is expected


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
    stock = Stock(base_stock_data)
    assert stock.have_onion() is expected


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
    stock = Stock(base_stock_data)
    assert stock.have_zucchini() is expected


@mark.parametrize(
    "vegetable, value, expected",
    [
        ("POTATO", 2000, True),
        ("POTATO", 0, False),
        ("LEEK", 100, True),
        ("LEEK", 0, False),
        ("TOMATO", 300, True),
        ("TOMATO", -50, False),
        ("ONION", 10, True),
        ("ONION", 0, False),
        ("ZUCCHINI", 5, True),
        ("ZUCCHINI", "test", False),
        ("POTATO", "2000", False),
    ],
)
def test_have_stocks(base_stock_data, vegetable, value, expected):
    for vegetables in base_stock_data:
        base_stock_data[vegetables] = 0

    base_stock_data[vegetable] = value
    stock = Stock(base_stock_data)
    assert stock.have_stocks() is expected
