def strategy(client, game_data: dict, my_farm: dict):
    if game_data["day"] == 0:
        client.add_command("0 EMPRUNTER 100000")
        client.add_command("0 ACHETER_CHAMP")
        client.add_command("0 EMPLOYER")
        client.add_command("1 SEMER PATATE 1")
    elif my_farm["fields"][0]["content"] != "NONE":
        if my_farm["fields"][0]["needed_water"] > 0:
            client.add_command("1 ARROSER 1")
        elif game_data["day"] >= client.vente1:
            client.add_command("0 VENDRE 1")
            client.vente1 = game_data["day"] + 2
    elif game_data["day"] >= client.vente1:
        client.add_command("1 SEMER PATATE 1")
