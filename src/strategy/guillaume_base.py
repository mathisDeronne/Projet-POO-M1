from src.farm.soup_factory import SoupFactory
from src.farm.field import Field
from src.farm.employees import Employee


def strategy(client, game_data: dict, my_farm: dict):
    soup_factory = SoupFactory(my_farm["soup_factory"])
    field = Field(my_farm["fields"][1])
    day = game_data["day"]

    ## Jour 1
    # j'achette champs 1 et 2
    # j'achette 6 employer
    # emplyer 1 qui plante
    # les 5 emplyer suivant qui arrose
    ## jour 2
    # les 5 emplyer arrose
    # je vend le champs 1
    ## jour 3
    # emplyer 1 vas au champs 2 est plante
    # les 5 emplyer se déplace au champs 2 est arrose
    ## jour 4
    # les 5 emplyer arrose
    # je vend le champs 2
    ## jour 5
    # emplyer 1 vas au champs 1 est plante
    # les 5 emplyer se déplace au champs 1 est arrose
    ## jour 6
    # les 5 emplyer arrose
    # je vend le champs 1
    ## ...

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
