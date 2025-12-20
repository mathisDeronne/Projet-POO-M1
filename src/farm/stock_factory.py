class Stock:
    def __init__(self, data: dict):
        self.potato = data["POTATO"]
        self.leek = data["LEEK"]
        self.tomato = data["TOMATO"]
        self.onion = data["ONION"]
        self.zucchini = data["ZUCCHINI"]

    def have_potato(self) -> bool:
        if not isinstance(self.potato, int):
            return False
        else:
            return self.potato > 0

    def have_leek(self) -> bool:
        if not isinstance(self.leek, int):
            return False
        else:
            return self.leek > 0

    def have_tomato(self) -> bool:
        if not isinstance(self.tomato, int):
            return False
        else:
            return self.tomato > 0

    def have_onion(self) -> bool:
        if not isinstance(self.onion, int):
            return False
        else:
            return self.onion > 0

    def have_zucchini(self) -> bool:
        if not isinstance(self.zucchini, int):
            return False
        else:
            return self.zucchini > 0

    def have_stocks(self) -> bool:
        return (
            self.have_potato()
            or self.have_leek()
            or self.have_tomato()
            or self.have_onion()
            or self.have_zucchini()
        )
