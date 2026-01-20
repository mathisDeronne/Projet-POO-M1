from src.farm.field import Field
from src.farm.soup_factory import SoupFactory


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
    LEGUMES = ["PATATE", "POIREAU", "TOMATE", "OIGNON", "COURGETTE"]
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
        plant_index = day // 2
        legume = LEGUMES[plant_index % len(LEGUMES)]

        client.add_command(f"1 SEMER {legume} {field_id}")
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

    else:
        field_id = 1 if ((day - 1) // 2) % 2 == 0 else 2
        field = fields[field_id]

        if field.is_ready_to_sell():
            client.add_command(f"0 VENDRE {field_id}")

    if day == 5:
        field_id = 3
        plant_index = day // 2
        legume = LEGUMES[plant_index % len(LEGUMES)]
        client.add_command(f"14 SEMER {legume} {field_id}")
        client.add_command(f"15 ARROSER {field_id}")
        client.add_command(f"16 ARROSER {field_id}")
        client.add_command(f"17 ARROSER {field_id}")
        client.add_command(f"18 ARROSER {field_id}")
        client.add_command(f"19 ARROSER {field_id}")
        client.add_command(f"20 ARROSER {field_id}")
        client.add_command(f"21 ARROSER {field_id}")
        client.add_command(f"22 ARROSER {field_id}")
        client.add_command(f"23 ARROSER {field_id}")
        client.add_command(f"24 ARROSER {field_id}")

    if day >= 10 and day % 2 == 0:
        field_id = 3
        plant_index = day // 2
        legume = LEGUMES[plant_index % len(LEGUMES)]
        client.add_command(f"14 SEMER {legume} {field_id}")
        client.add_command(f"15 ARROSER {field_id}")
        client.add_command(f"16 ARROSER {field_id}")
        client.add_command(f"17 ARROSER {field_id}")
        client.add_command(f"18 ARROSER {field_id}")
        client.add_command(f"19 ARROSER {field_id}")
        client.add_command(f"20 ARROSER {field_id}")
        client.add_command(f"21 ARROSER {field_id}")
        client.add_command(f"22 ARROSER {field_id}")
        client.add_command(f"23 ARROSER {field_id}")
        client.add_command(f"24 ARROSER {field_id}")

    if field_3.is_ready_to_sell():
        client.add_command("12 STOCKER 3 1")

    if soup_factory.made_soup():
        client.add_command("13 CUISINER")
