from src.farm.field import Field
from src.farm.soup_factory import SoupFactory
group1 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
group2 = [15, 16, 17, 18, 19, 20, 21, 22, 23, 24]

def strategy(client, game_data: dict, my_farm: dict):
    field_1 = Field(my_farm["fields"][0])
    field_2 = Field(my_farm["fields"][1])
    field_3 = Field(my_farm["fields"][2])
    field_4 = Field(my_farm["fields"][3])
    field_5 = Field(my_farm["fields"][4])
    fields = {
        1: field_1,
        2: field_2,
        3: field_3,
        4: field_4,
        5: field_5,
    }
    soup_factory = SoupFactory(my_farm["soup_factory"])
    fields = [Field(f) for f in my_farm["fields"]]

    day = game_data["day"]

    if day == 0:
        client.add_command("0 EMPRUNTER 1000")
        for field in fields:
            if not field.is_bought():
                client.add_command("0 ACHETER_CHAMP")

        for _ in range(24):
            client.add_command("0 EMPLOYER")

        client.add_command("13 SEMER PATATE 5")
        client.add_command("0 ACHETER_TRACTEUR")

    if day % 2 == 0:
        field_id = 1 if (day // 2) % 2 == 0 else 2

        client.add_command(f"1 SEMER PATATE {field_id}")
        client.add_command(f"{group1} ARROSER {field_id}")
    else:
        field_id = 1 if ((day - 1) // 2) % 2 == 0 else 2
        field = fields[field_id]

        if field.is_ready_to_sell():
            client.add_command(f"0 VENDRE {field_id}")

    if day == 5:
        field_id = 3
        client.add_command(f"14 SEMER PATATE {field_id}")
        client.add_command(f"{group2} ARROSER {field_id}")

    if day >= 10 and day % 2 == 0:
        field_id = 3
        client.add_command(f"14 SEMER PATATE {field_id}")
        client.add_command(f"{group2} ARROSER {field_id}")

    if field_3.is_ready_to_sell():
        client.add_command("12 STOCKER 3 1")

    if soup_factory.made_soup():
        client.add_command("13 CUISINER")
