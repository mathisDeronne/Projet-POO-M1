from src.farm.soup_factory import SoupFactory, Stock


def test_stock():
    stock = Stock({"POTATO": 0, "LEEK": 0, "TOMATO": 0, "ONION": 0, "ZUCCHINI": 0})
    assert stock.have_potato() is False
    assert stock.have_leek() is False
    assert stock.have_tomato() is False
    assert stock.have_onion() is False
    assert stock.have_zucchini() is False
    assert stock.have_stocks() is False


def test_Soup_factory():
    soup_factory = SoupFactory(
        {
            "days_off": 0,
            "stock": {"POTATO": 0, "LEEK": 0, "TOMATO": 0, "ONION": 0, "ZUCCHINI": 0},
        }
    )
    assert soup_factory.is_open() is True
    assert soup_factory.has_stock() is False
