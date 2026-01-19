from src.farm.field import Field
from src.farm.soup_factory import SoupFactory


def strategy(client, game_data: dict, my_farm: dict):
    field_3 = Field(my_farm["fields"][2])
    soup_factory = SoupFactory(my_farm["soup_factory"])
    fields = [Field(f) for f in my_farm["fields"]]
    day = game_data["day"]

    if day == 0:
        client.add_command("0 EMPRUNTER 100000")

        for field in fields:
            if not field.is_bought():
                client.add_command("0 ACHETER_CHAMP")

        for _ in range(13):
            client.add_command("0 EMPLOYER")
        client.add_command("13 SEMER PATATE 5")

        client.add_command("0 ACHETER_TRACTEUR")
        return

    cycle_day = (day - 1) % 21

    if cycle_day in (0, 5, 10):
        client.add_command("1 SEMER PATATE 3")
        for i in range(2, 12):
            client.add_command(f"{i} ARROSER 3")

    if field_3.is_ready_to_sell():
        client.add_command("12 STOCKER 3 1")

    if soup_factory.made_soup():
        client.add_command("13 CUISINER")
