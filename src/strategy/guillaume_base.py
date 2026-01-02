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
