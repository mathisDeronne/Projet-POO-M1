from src.farm.field import Field


def strategy(client, game_data: dict, my_farm: dict):
    field_1 = Field(my_farm["fields"][1])
    field_2 = Field(my_farm["fields"][2])
    fields = {
        1: Field(my_farm["fields"][0]),
        2: Field(my_farm["fields"][1]),
    }

    day = game_data["day"]

    if day == 0:
        if not field_1.is_bought():
            client.add_command("0 ACHETER_CHAMP")
        if not field_2.is_bought():
            client.add_command("0 ACHETER_CHAMP")

        for _ in range(11):
            client.add_command("0 EMPLOYER")

    if day % 2 == 0:
        field_id = 1 if (day // 2) % 2 == 0 else 2

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

    else:
        field_id = 1 if ((day - 1) // 2) % 2 == 0 else 2
        field = fields[field_id]

        if field.is_ready_to_sell():
            client.add_command(f"0 VENDRE {field_id}")
