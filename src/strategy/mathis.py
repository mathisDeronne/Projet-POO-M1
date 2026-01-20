from src.farm.field import Field
from src.farm.soup_factory import SoupFactory
group1 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
group2 = [15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
group3 = [27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
cooks = [13, 25, 38, 40]

def strategy(client, game_data: dict, my_farm: dict):
    ABS = 0 # Anti Blocking System
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
    
    LEGUMES = ["PATATE", "POIREAU", "TOMATE", "OIGNON", "COURGETTE"]

    day = game_data["day"]

    if day == 0:
        client.add_command("0 EMPRUNTER 100000")
        ABS = 1
        for _ in range (2):
            client.add_command("0 ACHETER_TRACTEUR")
        for _ in range(5):
            client.add_command("0 ACHETER_CHAMP")

        for _ in range(40):
            client.add_command("0 EMPLOYER")

        for cook in cooks:
            client.add_command(f"{cook} CUISINER")
        client.add_command("39 CUISINER")
    if day % 2 == 0:
        field_id = 1 if (day // 2) % 2 == 0 else 2
        plant_index = day // 2
        legume = LEGUMES[plant_index % len(LEGUMES)]

        client.add_command(f"1 SEMER {legume} {field_id}")
        ABS = 1
        for employee in group1:
            client.add_command(f"{employee} ARROSER {field_id}")
            ABS = 1
    else:
        field_id = 1 if ((day - 1) // 2) % 2 == 0 else 2
        field = fields[field_id]

        if field.is_ready_to_sell():
            client.add_command(f"0 VENDRE {field_id}")
            ABS = 1

    if day % 2 == 0 and day > 6:
        legume = LEGUMES[plant_index % len(LEGUMES)]

        client.add_command(f"39 SEMER {legume} 5")
        ABS = 1
    elif day %2 != 0 and day > 6:
        client.add_command("39 CUISINER")
        ABS = 1

    if day == 1:
        ABS = 1
        client.add_command("14 SEMER PATATE 3")
        for employees in group2:
            client.add_command(f"{employees} ARROSER 3")

        client.add_command("26 SEMER PATATE 4")
        for employee in group3:
            client.add_command(f"{employee} ARROSER 4")

    if day == 5:
        client.add_command("37 STOCKER 4 2")

    if day >= 5 and day % 2 == 0:
        field_id = 3
        plant_index = day // 2
        legume = LEGUMES[plant_index % len(LEGUMES)]
        client.add_command(f"14 SEMER {legume} {field_id}")
        ABS = 1
        for employee in group2:
            client.add_command(f"{employee} ARROSER {field_id}")

    if day >= 6 and day % 2 == 0:
        field_id = 4
        plant_index = day // 2
        legume = LEGUMES[plant_index % len(LEGUMES)]
        client.add_command(f"26 SEMER {legume} {field_id}")
        ABS = 1
        for employee in group3:
            client.add_command(f"{employee} ARROSER {field_id}")

    if field_3.is_ready_to_sell():
        client.add_command("12 STOCKER 3 1")
        ABS = 1

    if day >= 10 and field_4.is_ready_to_sell():
        client.add_command("37 STOCKER 4 2")

    if soup_factory.made_soup() and day >= 7:
        for cook in cooks:
            client.add_command(f"{cook} CUISINER")
            ABS = 1

    if ABS == 0:
            client.add_command("0 EMPRUNTER 0")