Legume = {"POTATO", "LEEK", "TOMATO", "ONION", "ZUCCHINI"}


class Field:
    def __init__(self, data: dict):
        self.content = data["content"]
        self.needed_water = data["needed_water"]
        self.bought = data["bought"]
        self.location = data["location"]

    def is_content_empty(self) -> bool:
        return self.content == "NONE"

    def is_content_full(self) -> bool:
        return self.content in Legume

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

    def watered_field_1(my_farm: dict) -> bool:
        field = Field(my_farm["fields"][0])
        return (
            field.is_location_valid()
            and field.is_bought()
            and field.is_content_full()
            and field.is_needed_water()
        )

    def watered_field_2(my_farm: dict) -> bool:
        field = Field(my_farm["fields"][1])
        return (
            field.is_location_valid()
            and field.is_bought()
            and field.is_content_full()
            and field.is_needed_water()
        )

    def watered_field_3(my_farm: dict) -> bool:
        field = Field(my_farm["fields"][2])
        return (
            field.is_location_valid()
            and field.is_bought()
            and field.is_content_full()
            and field.is_needed_water()
        )

    def watered_field_4(my_farm: dict) -> bool:
        field = Field(my_farm["fields"][3])
        return (
            field.is_location_valid()
            and field.is_bought()
            and field.is_content_full()
            and field.is_needed_water()
        )

    def watered_field_5(my_farm: dict) -> bool:
        field = Field(my_farm["fields"][4])
        return (
            field.is_location_valid()
            and field.is_bought()
            and field.is_content_full()
            and field.is_needed_water()
        )
