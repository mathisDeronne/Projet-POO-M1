Legume = {"POTATO", "LEEK", "TOMATO", "ONION", "ZUCCHINI"}


class Field:
    def __init__(self, data: dict):
        self.content = data["content"]
        self.needed_water = data["needed_water"]
        self.bought = data["bought"]
        self.location = data["location"]

    def is_content_empty(self) -> bool:
        return (
            isinstance(self.content, str)
            and not isinstance(self.content, bool)
            and self.content == "NONE"
        )

    def is_content_full(self) -> bool:
        return (
            isinstance(self.content, str)
            and not isinstance(self.content, bool)
            and self.content in Legume
        )

    def is_bought(self) -> bool:
        return isinstance(self.bought, bool) and self.bought

    def is_needed_water(self) -> bool:
        return (
            isinstance(self.needed_water, int)
            and not isinstance(self.needed_water, bool)
            and self.needed_water > 0
        )

    def is_location_valid(self) -> bool:
        if (
            not isinstance(self.location, str)
            or isinstance(self.location, bool)
            or not self.location.startswith("FIELD")
        ):
            return False
        try:
            num = int(self.location.replace("FIELD", ""))
        except ValueError:
            return False
        return 1 <= num <= 5

    def is_ready_to_sell(self) -> bool:
        return (
            self.is_bought() and self.is_content_full() and not self.is_needed_water()
        )
