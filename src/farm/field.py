class Field:
    def __init__(self, data: int):
        self.content = data["content"]
        self.needed_water = data["needed_water"]
        self.bought = data["bought"]
        self.location = data["location"]

    def is_content_empty(self) -> bool:
        return self.content == "NONE"

    def is_bought(self) -> bool:
        return self.bought is True

    def is_needed_water(self) -> bool:
        return self.needed_water > 0

    def is_location(self) -> bool:
        if not self.location.startswith("FIELD"):
            return False
        try:
            num = int(self.location.replace("FIELD", ""))
        except ValueError:
            return False
        return 1 <= num <= 5
