from src.farm.soup_factory import SoupFactory
from src.farm.field import Field
from src.farm.employees import Employee


def strategy(client, game_data: dict, my_farm: dict):
    soup_factory = SoupFactory(my_farm["soup_factory"])
    field_1 = Field(my_farm["fields"][1])
    field_2 = Field(my_farm["fields"][2])
    day = game_data["day"]

    if day == 0:
        for _ in range(2):
            client.add_command("0 ACHETER_CHAMP")
        for _ in range(11):
            client.add_command("0 EMPLOYER")
        client.add_command("1 SEMER PATATE 1")
        client.add_command("2 ARROSER 1")
        client.add_command("3 ARROSER 1")
        client.add_command("4 ARROSER 1")
        client.add_command("5 ARROSER 1")
        client.add_command("6 ARROSER 1")
        client.add_command("7 ARROSER 1")
        client.add_command("8 ARROSER 1")
        client.add_command("9 ARROSER 1")
        client.add_command("10 ARROSER 1")
        client.add_command("11 ARROSER 1")
    if day == 1:
        client.add_command("0 VENDRE 1")
    if day == 2:
        client.add_command("1 SEMER PATATE 2")
        client.add_command("2 ARROSER 2")
        client.add_command("3 ARROSER 2")
        client.add_command("4 ARROSER 2")
        client.add_command("5 ARROSER 2")
        client.add_command("6 ARROSER 2")
        client.add_command("7 ARROSER 2")
        client.add_command("8 ARROSER 2")
        client.add_command("9 ARROSER 2")
        client.add_command("10 ARROSER 2")
        client.add_command("11 ARROSER 2")
    if day == 3:
        client.add_command("0 VENDRE 2")
    if day == 4:
        client.add_command("1 SEMER PATATE 1")
        client.add_command("2 ARROSER 1")
        client.add_command("3 ARROSER 1")
        client.add_command("4 ARROSER 1")
        client.add_command("5 ARROSER 1")
        client.add_command("6 ARROSER 1")
        client.add_command("7 ARROSER 1")
        client.add_command("8 ARROSER 1")
        client.add_command("9 ARROSER 1")
        client.add_command("10 ARROSER 1")
        client.add_command("11 ARROSER 1")
    if day == 5:
        client.add_command("0 VENDRE 1")
    if day == 6:
        client.add_command("1 SEMER PATATE 2")
        client.add_command("2 ARROSER 2")
        client.add_command("3 ARROSER 2")
        client.add_command("4 ARROSER 2")
        client.add_command("5 ARROSER 2")
        client.add_command("6 ARROSER 2")
        client.add_command("7 ARROSER 2")
        client.add_command("8 ARROSER 2")
        client.add_command("9 ARROSER 2")
        client.add_command("10 ARROSER 2")
        client.add_command("11 ARROSER 2")
    if day == 7:
        client.add_command("0 VENDRE 2")
    if day == 8:
        client.add_command("1 SEMER PATATE 1")
        client.add_command("2 ARROSER 1")
        client.add_command("3 ARROSER 1")
        client.add_command("4 ARROSER 1")
        client.add_command("5 ARROSER 1")
        client.add_command("6 ARROSER 1")
        client.add_command("7 ARROSER 1")
        client.add_command("8 ARROSER 1")
        client.add_command("9 ARROSER 1")
        client.add_command("10 ARROSER 1")
        client.add_command("11 ARROSER 1")
    if day == 9:
        client.add_command("0 VENDRE 1")
    if day == 10:
        client.add_command("1 SEMER PATATE 2")
        client.add_command("2 ARROSER 2")
        client.add_command("3 ARROSER 2")
        client.add_command("4 ARROSER 2")
        client.add_command("5 ARROSER 2")
        client.add_command("6 ARROSER 2")
        client.add_command("7 ARROSER 2")
        client.add_command("8 ARROSER 2")
        client.add_command("9 ARROSER 2")
        client.add_command("10 ARROSER 2")
        client.add_command("11 ARROSER 2")
    if day == 11:
        client.add_command("0 VENDRE 2")
    if day == 12:
        client.add_command("1 SEMER PATATE 1")
        client.add_command("2 ARROSER 1")
        client.add_command("3 ARROSER 1")
        client.add_command("4 ARROSER 1")
        client.add_command("5 ARROSER 1")
        client.add_command("6 ARROSER 1")
        client.add_command("7 ARROSER 1")
        client.add_command("8 ARROSER 1")
        client.add_command("9 ARROSER 1")
        client.add_command("10 ARROSER 1")
        client.add_command("11 ARROSER 1")
    if day == 13:
        client.add_command("0 VENDRE 1")
