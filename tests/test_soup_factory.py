from src.farm.soup_factory import Soup_factory, Stock


def test_stock():
    stock = Stock({"POTATO": 0, "LEEK": 0, "TOMATO": 0, "ONION": 0, "ZUCCHINI": 0})
    assert stock.have_potato() is False
    assert stock.have_leek() is False
    assert stock.have_tomato() is False
    assert stock.have_onion() is False
    assert stock.have_zucchini() is False


def test_Soup_factory():
    soup_factory = Soup_factory(
        {
            "days_off": 0,
            "stock": {"POTATO": 0, "LEEK": 0, "TOMATO": 0, "ONION": 0, "ZUCCHINI": 0},
        }
    )
    assert soup_factory.have_days_off() is True
    assert soup_factory.stocks() is False
