from src.farm.soup_factory import SoupFactory
from src.farm.field import Field


# a voir si faut mettre dans SoupFactory ??
def made_soup(my_farm: dict) -> bool:
    soup_factory = SoupFactory(my_farm["soup_factory"])
    if soup_factory.is_open() and soup_factory.has_stock():
        return True


# a voir si faut mettre dans Field ??
def watered(my_farm: dict) -> int:
    results = {}
    for fram_data in my_farm["fields"]:
        field = Field(fram_data)

        if field.is_location_valid() and field.is_bought() and field.is_needed_water():
            results[field.location] = field.needed_water

    return results


def watered_field_1(my_farm: dict) -> int:
    field = Field(my_farm["fields"][0])
    if field.is_location_valid() and field.is_bought() and field.is_needed_water():
        return field.needed_water


def strategy(client, game_data: dict, my_farm: dict):
    if made_soup(my_farm):
        client.add_command("1 CUISINER")
