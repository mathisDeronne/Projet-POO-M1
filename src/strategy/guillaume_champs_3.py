from src.farm.field import Field
from src.farm.soup_factory import SoupFactory


def strategy(client, game_data: dict, my_farm: dict):
    field_3 = Field(my_farm["fields"][2])
    soup_factory = SoupFactory(my_farm["soup_factory"])
    fields = [Field(f) for f in my_farm["fields"]]
    day = game_data["day"]

    if day == 0:
        client.add_command("0 EMPRUNTER 1000")

        for field in fields:
            if not field.is_bought():
                client.add_command("0 ACHETER_CHAMP")

        for _ in range(13):
            client.add_command("0 EMPLOYER")
        client.add_command("13 SEMER PATATE 5")
        client.add_command("0 ACHETER_TRACTEUR")

    if day == 5:
        client.add_command("1 SEMER PATATE 3")
        for i in range(2, 12):
            client.add_command(f"{i} ARROSER 3")
        return

    if day >= 10 and day % 2 == 0:
        field_id = 3
        client.add_command(f"1 SEMER PATATE {field_id}")
        client.add_command(f"2 ARROSER {field_id}")
        client.add_command(f"3 ARROSER {field_id}")
        client.add_command(f"4 ARROSER {field_id}")
        client.add_command(f"5 ARROSER {field_id}")
        client.add_command(f"6 ARROSER {field_id}")
        client.add_command(f"7 ARROSER {field_id}")
        client.add_command(f"8 ARROSER {field_id}")
        client.add_command(f"9 ARROSER {field_id}")
        client.add_command(f"10 ARROSER {field_id}")
        client.add_command(f"11 ARROSER {field_id}")

    if field_3.is_ready_to_sell():
        client.add_command("12 STOCKER 3 1")

    if soup_factory.made_soup():
        client.add_command("13 CUISINER")
