from pytest import fixture, mark  # type: ignore
from src.farm.soup_factory import SoupFactory
from unittest.mock import Mock


@fixture
def data_soupfactory():
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


def test_soup_factory(data_soupfactory):
    soup_factory = SoupFactory(data_soupfactory)
    assert soup_factory.is_open() is True
    assert soup_factory.has_stock() is True
    assert soup_factory.made_soup() is True


@mark.parametrize(
    "days_off, expected",
    [
        (0, True),
        (-0, True),
        (+0, True),
        (0.0, False),
        (+0.0, False),
        (-0.0, False),
        (5, False),
        ("0", False),
        (+0.1, False),
        (-0.1, False),
        ("test", False),
        ("zero", False),
        (True, False),
        (False, False),
    ],
)
def test_days_off(data_soupfactory, days_off, expected):
    data_soupfactory["days_off"] = days_off
    soup_factory = SoupFactory(data_soupfactory)
    assert soup_factory.is_open() is expected


def test_has_stock():
    soup_factory = SoupFactory.__new__(SoupFactory)
    soup_factory.stock = Mock()
    soup_factory.stock.have_stocks.return_value = True
    assert soup_factory.has_stock() is True
    soup_factory.stock.have_stocks.return_value = False
    assert soup_factory.has_stock() is False


@mark.parametrize(
    "is_open, has_stock, expected",
    [
        (True, True, True),
        (True, False, False),
        (False, True, False),
        (False, False, False),
    ],
)
def test_made_soup(is_open, has_stock, expected):
    soup_factory = SoupFactory.__new__(SoupFactory)
    soup_factory.is_open = Mock(return_value=is_open)
    soup_factory.has_stock = Mock(return_value=has_stock)
    assert soup_factory.made_soup() is expected
