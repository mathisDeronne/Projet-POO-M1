from src.farm.tractors import Tractors

locations = {"FIELD1", "FIELD2", "FIELD3", "FIELD4", "FIELD5", "SOUP_FACTORY"}


class Employee:
    def __init__(self, data: dict):
        self.id = data["id"]
        self.location = data["location"]
        self.tractor = Tractors(data["tractor"])
        self.salary = data["salary"]

    def id_valid(self) -> bool:
        return (
            isinstance(self.id, int) and not isinstance(self.id, bool) and self.id >= 0
        )

        )

    def is_salary(self) -> bool:
        return (
            isinstance(self.salary, int)
            and not isinstance(self.salary, bool)
            and self.salary >= 0
        )

    def is_tractor(self) -> bool:
        return self.tractor.tractor_valid()
