from src.farm.stock_factory import Stock


class SoupFactory:
    def __init__(self, data: dict):
        self.days_off = data["days_off"]
        self.stock = Stock(data["stock"])

    def is_open(self) -> bool:
        return (
            isinstance(self.days_off, int)
            and not isinstance(self.days_off, bool)
            and self.days_off == 0
        )

    def has_stock(self) -> bool:
        return self.stock.have_stocks()

    def made_soup(self) -> bool:
        return self.is_open() and self.has_stock()
