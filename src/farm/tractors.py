locations = {"FIELD1", "FIELD2", "FIELD3", "FIELD4", "FIELD5", "SOUP_FACTORY"}


class Tractors:
    def __init__(self, data: dict):
        self.location = data["location"]
        self.id = data["id"]

    def id_valid(self) -> bool:
        return (
            isinstance(self.id, int) and not isinstance(self.id, bool) and self.id >= 0
        )

    def is_location_valid(self) -> bool:
        return (
            self.location in locations
            and isinstance(self.location, str)
            and not isinstance(self.location, bool)
        )

    def tractor_valid(self) -> bool:
        return self.id_valid() and self.is_location_valid()
