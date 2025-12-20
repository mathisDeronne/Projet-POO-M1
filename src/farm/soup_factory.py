class Stock:
    def __init__(self, data: int):
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


class Soup_factory:
    def __init__(self, data: int):
        self.days_off = data["days_off"]
        self.stock = Stock(data["stock"])

    def have_days_off(self) -> bool:
        return self.days_off == 0

    def stocks(self) -> bool:
        return (
            self.stock.have_potato()
            or self.stock.have_leek()
            or self.stock.have_tomato()
            or self.stock.have_onion()
            or self.stock.have_zucchini()
        )
