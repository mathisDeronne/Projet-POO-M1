class Field:
    def __init__(self, data: dict):
        self.content = data["content"]
        self.needed_water = data["needed_water"]
        self.bought = data["bought"]
        self.location = data["location"]

    def is_content_empty(self) -> bool:
        if not isinstance(self.location, str):
            return False
        else:
            return self.content == "NONE"

    def is_bought(self) -> bool:
        return self.bought == True  # noqa: E712

    def is_needed_water(self) -> bool:
        if not isinstance(self.needed_water, int):
            return False
        else:
            return self.needed_water > 0

    def is_location_valid(self) -> bool:
        if not isinstance(self.location, str):
            return False
        if not self.location.startswith("FIELD"):
            return False
        try:
            num = int(self.location.replace("FIELD", ""))
        except ValueError:
            return False
        return 1 <= num <= 5
