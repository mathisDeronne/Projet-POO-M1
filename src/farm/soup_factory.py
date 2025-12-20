class Stock:
    def __init__(self, data: dict):
        self.potato = data["POTATO"]
        self.leek = data["LEEK"]
        self.tomato = data["TOMATO"]
        self.onion = data["ONION"]
        self.zucchini = data["ZUCCHINI"]

    def have_potato(self) -> bool:
        return self.potato > 0

    def have_leek(self) -> bool:
        return self.leek > 0

    def have_tomato(self) -> bool:
        return self.tomato > 0

    def have_onion(self) -> bool:
        return self.onion > 0

    def have_zucchini(self) -> bool:
        return self.zucchini > 0

    def have_stocks(self) -> bool:
        return (
            self.have_potato()
            or self.have_leek()
            or self.have_tomato()
            or self.have_onion()
            or self.have_zucchini()
        )


class SoupFactory:
    def __init__(self, data: dict):
        self.days_off = data["days_off"]
        self.stock = Stock(data["stock"])

    def is_open(self) -> bool:
        return self.days_off == 0

    def has_stock(self) -> bool:
        return self.stock.have_stocks()
