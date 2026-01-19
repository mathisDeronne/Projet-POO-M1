from src.farm.field import Field


def strategy(client, game_data: dict, my_farm: dict):
    fields = [Field(f) for f in my_farm["fields"]]
    day = game_data["day"]

    if day == 0:
        client.add_command("0 EMPRUNTER 100000")

        for field in fields:
            if not field.is_bought():
                client.add_command("0 ACHETER_CHAMP")

        for _ in range(24):
            client.add_command("0 EMPLOYER")

        client.add_command("0 ACHETER_TRACTEUR")
        client.add_command("0 ACHETER_TRACTEUR")
        return

    cycle_day = (day - 1) % 21

    if cycle_day in (0, 9, 12):
        client.add_command("1 SEMER PATATE 5")
        for i in range(2, 12):
            client.add_command(f"{i} ARROSER 5")

    if cycle_day in (7, 11):
        client.add_command("12 STOCKER 5 1")

    if cycle_day == 13:
        client.add_command("13 CUISINER")
