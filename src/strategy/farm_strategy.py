from src.farm.soup_factory import SoupFactory
from src.farm.field import Field


def semer(client, worker_id, field_id, legume):
    client.add_command(f"{worker_id} SEMER {legume} {field_id}")


def arroser_groupe(client, workers, field_id):
    for w in workers:
        client.add_command(f"{w} ARROSER {field_id}")


def planter_et_arroser(client, semeur, arroseurs, field_id, legume):
    semer(client, semeur, field_id, legume)
    arroser_groupe(client, arroseurs, field_id)


GROUPES_CHAMPS = {
    1: {"semeur": 1, "arroseurs": range(2, 12)},
    3: {"semeur": 14, "arroseurs": range(15, 25)},
    4: {"semeur": 26, "arroseurs": range(27, 37)},
    5: {"semeur": 41, "arroseurs": range(42, 52)},
}

GROUPES_CUISINE = [13, 25, 38, 39, 40, 53, 54, 55, 56]


def strategy(client, game_data: dict, my_farm: dict):
    soup_factory = SoupFactory(my_farm["soup_factory"])
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

    LEGUMES = ["PATATE", "POIREAU", "TOMATE", "OIGNON", "COURGETTE"]
    LEGUMES2 = ["COURGETTE", "PATATE", "POIREAU", "TOMATE", "OIGNON"]
    LEGUMES3 = ["OIGNON", "COURGETTE", "PATATE", "POIREAU", "TOMATE"]

    ABS = 0  # Anti Blocking System

    day = game_data["day"]
    plant_index = day // 2

    if day == 0:
        client.add_command("0 EMPRUNTER 100000")
        ABS = False
        for field in fields.values():
            if not field.is_bought():
                client.add_command("0 ACHETER_CHAMP")

        for _ in range(56):
            client.add_command("0 EMPLOYER")

        client.add_command("0 ACHETER_TRACTEUR")
        client.add_command("0 ACHETER_TRACTEUR")
        client.add_command("0 ACHETER_TRACTEUR")

        for w in GROUPES_CUISINE:
            client.add_command(f"{w} CUISINER")

    if day % 2 == 0:
        field_id = 1 if (day // 2) % 2 == 0 else 2
        legume = LEGUMES[plant_index % len(LEGUMES)]
        g1 = GROUPES_CHAMPS[1]
        planter_et_arroser(client, g1["semeur"], g1["arroseurs"], field_id, legume)
        ABS = 1

    else:
        field_id = 1 if ((day - 1) // 2) % 2 == 0 else 2
        field = fields[field_id]

        if field.is_ready_to_sell():
            client.add_command(f"0 VENDRE {field_id}")
            ABS = 1

    if day == 1:
        g3 = GROUPES_CHAMPS[3]
        planter_et_arroser(client, g3["semeur"], g3["arroseurs"], 3, "PATATE")

        g4 = GROUPES_CHAMPS[4]
        planter_et_arroser(client, g4["semeur"], g4["arroseurs"], 4, "PATATE")

        g5 = GROUPES_CHAMPS[5]
        planter_et_arroser(client, g5["semeur"], g5["arroseurs"], 5, "PATATE")

    if day == 5:
        client.add_command("37 STOCKER 4 2")
        ABS = 1

    if day >= 5 and day % 2 == 0:
        legume = LEGUMES[plant_index % len(LEGUMES)]
        g = GROUPES_CHAMPS[3]
        planter_et_arroser(client, g["semeur"], g["arroseurs"], 3, legume)
        ABS = 1

    if day == 7:
        client.add_command("52 STOCKER 5 3")
        ABS = 1

    if day >= 6 and day % 2 == 0:
        legume = LEGUMES2[plant_index % len(LEGUMES2)]
        g = GROUPES_CHAMPS[4]
        planter_et_arroser(client, g["semeur"], g["arroseurs"], 4, legume)
        ABS = 1

    if day >= 10 and day % 2 == 0:
        legume = LEGUMES3[plant_index % len(LEGUMES3)]
        g = GROUPES_CHAMPS[5]
        planter_et_arroser(client, g["semeur"], g["arroseurs"], 5, legume)
        ABS = 1

    if field_3.is_ready_to_sell():
        client.add_command("12 STOCKER 3 1")
        ABS = 1

    if day >= 10 and field_4.is_ready_to_sell():
        client.add_command("37 STOCKER 4 2")
        ABS = 1

    if day >= 10 and field_5.is_ready_to_sell():
        client.add_command("52 STOCKER 5 3")
        ABS = 1

    if day >= 6 and soup_factory.made_soup():
        for w in GROUPES_CUISINE:
            client.add_command(f"{w} CUISINER")
        ABS = 1

    if not ABS:
        client.add_command("0 EMPRUNTER 0")
