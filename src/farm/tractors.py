locations = {"FIELD1", "FIELD2", "FIELD3", "FIELD4", "FIELD5", "SOUP_FACTORY"}


class Tractors:
    def __init__(self, data: dict):
        self.location = data["location"]
        self.id = data["id"]

    def id_is(self) -> bool:
        return (
            isinstance(self.id, int) and not isinstance(self.id, bool) and self.id > 0
        )

    # a réparé
    def is_location_valid(self) -> bool:
        if (
            not isinstance(self.location, str)
            or isinstance(self.location, bool)
            or not self.location in locations
        ):
            return False
        try:
            num = int(self.location.replace("FIELD", ""))
        except ValueError:
            return False
        return 1 <= num <= 5
