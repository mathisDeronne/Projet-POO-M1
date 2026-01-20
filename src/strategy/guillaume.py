from src.farm.field import Field
from src.farm.soup_factory import SoupFactory
group1 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
group2 = [15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
cooks = [13, 25,]

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
        client.add_command("0 EMPRUNTER 1000")
        ABS = 1
        for _ in range(3):
            client.add_command("0 ACHETER_CHAMP")

        for _ in range(55):
            client.add_command("0 EMPLOYER")

        client.add_command("13 SEMER PATATE 5")
        client.add_command("25 SEMER PATATE 5")
        client.add_command("38 SEMER PATATE 5")
        client.add_command("39 SEMER PATATE 5")
        client.add_command("40 SEMER PATATE 5")
        client.add_command("53 SEMER PATATE 5")
        client.add_command("54 SEMER PATATE 5")
        client.add_command("55 SEMER PATATE 5")
        client.add_command("0 ACHETER_TRACTEUR")
        client.add_command("0 ACHETER_TRACTEUR")
        client.add_command("0 ACHETER_TRACTEUR")
        for cook in cooks:
            client.add_command(f"{cook} CUISINER")
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

    if day == 1:
        client.add_command("14 SEMER PATATE 3")
        client.add_command("15 ARROSER 3")
        client.add_command("16 ARROSER 3")
        client.add_command("17 ARROSER 3")
        client.add_command("18 ARROSER 3")
        client.add_command("19 ARROSER 3")
        client.add_command("20 ARROSER 3")
        client.add_command("21 ARROSER 3")
        client.add_command("22 ARROSER 3")
        client.add_command("23 ARROSER 3")
        client.add_command("24 ARROSER 3")

        client.add_command("26 SEMER PATATE 4")
        client.add_command("27 ARROSER 4")
        client.add_command("28 ARROSER 4")
        client.add_command("29 ARROSER 4")
        client.add_command("30 ARROSER 4")
        client.add_command("31 ARROSER 4")
        client.add_command("32 ARROSER 4")
        client.add_command("33 ARROSER 4")
        client.add_command("34 ARROSER 4")
        client.add_command("35 ARROSER 4")
        client.add_command("36 ARROSER 4")

    if day == 1:
        client.add_command("14 SEMER PATATE 3")
        client.add_command("15 ARROSER 3")
        client.add_command("16 ARROSER 3")
        client.add_command("17 ARROSER 3")
        client.add_command("18 ARROSER 3")
        client.add_command("19 ARROSER 3")
        client.add_command("20 ARROSER 3")
        client.add_command("21 ARROSER 3")
        client.add_command("22 ARROSER 3")
        client.add_command("23 ARROSER 3")
        client.add_command("24 ARROSER 3")

        client.add_command("26 SEMER PATATE 4")
        client.add_command("27 ARROSER 4")
        client.add_command("28 ARROSER 4")
        client.add_command("29 ARROSER 4")
        client.add_command("30 ARROSER 4")
        client.add_command("31 ARROSER 4")
        client.add_command("32 ARROSER 4")
        client.add_command("33 ARROSER 4")
        client.add_command("34 ARROSER 4")
        client.add_command("35 ARROSER 4")
        client.add_command("36 ARROSER 4")

        client.add_command("41 SEMER PATATE 5")
        client.add_command("42 ARROSER 5")
        client.add_command("43 ARROSER 5")
        client.add_command("44 ARROSER 5")
        client.add_command("45 ARROSER 5")
        client.add_command("46 ARROSER 5")
        client.add_command("47 ARROSER 5")
        client.add_command("48 ARROSER 5")
        client.add_command("49 ARROSER 5")
        client.add_command("50 ARROSER 5")
        client.add_command("51 ARROSER 5")

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

    if day == 7:
        client.add_command("52 STOCKER 5 3")

    if day == 7:
        client.add_command("52 STOCKER 5 3")

    if day >= 6 and day % 2 == 0:
        field_id = 4
        plant_index = day // 2
        legume = LEGUMES[plant_index % len(LEGUMES)]
        client.add_command(f"14 SEMER {legume} {field_id}")
        ABS = 1
        for employee in group2:
            client.add_command(f"{employee} ARROSER {field_id}")

    if day >= 10 and day % 2 == 0:
        field_id = 5
        plant_index = day // 2
        legume = LEGUMES[plant_index % len(LEGUMES)]
        client.add_command(f"41 SEMER {legume} {field_id}")
        client.add_command(f"42 ARROSER {field_id}")
        client.add_command(f"43 ARROSER {field_id}")
        client.add_command(f"44 ARROSER {field_id}")
        client.add_command(f"45 ARROSER {field_id}")
        client.add_command(f"46 ARROSER {field_id}")
        client.add_command(f"47 ARROSER {field_id}")
        client.add_command(f"48 ARROSER {field_id}")
        client.add_command(f"49 ARROSER {field_id}")
        client.add_command(f"50 ARROSER {field_id}")
        client.add_command(f"51 ARROSER {field_id}")

    if day >= 10 and day % 2 == 0:
        field_id = 5
        plant_index = day // 2
        legume = LEGUMES[plant_index % len(LEGUMES)]
        client.add_command(f"41 SEMER {legume} {field_id}")
        client.add_command(f"42 ARROSER {field_id}")
        client.add_command(f"43 ARROSER {field_id}")
        client.add_command(f"44 ARROSER {field_id}")
        client.add_command(f"45 ARROSER {field_id}")
        client.add_command(f"46 ARROSER {field_id}")
        client.add_command(f"47 ARROSER {field_id}")
        client.add_command(f"48 ARROSER {field_id}")
        client.add_command(f"49 ARROSER {field_id}")
        client.add_command(f"50 ARROSER {field_id}")
        client.add_command(f"51 ARROSER {field_id}")

    if field_3.is_ready_to_sell():
        client.add_command("12 STOCKER 3 1")
        ABS = 1

    if day >= 10 and field_4.is_ready_to_sell():
        client.add_command("37 STOCKER 4 2")

    if day >= 10 and field_4.is_ready_to_sell():
        client.add_command("37 STOCKER 4 2")

    if day >= 10 and field_5.is_ready_to_sell():
        client.add_command("52 STOCKER 5 3")

    if soup_factory.made_soup():
        client.add_command("13 CUISINER")
        client.add_command("25 CUISINER")
        client.add_command("38 CUISINER")
        client.add_command("39 CUISINER")
        client.add_command("40 CUISINER")
        client.add_command("53 CUISINER")
        client.add_command("54 CUISINER")
        client.add_command("55 CUISINER")
