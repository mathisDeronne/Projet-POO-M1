def strategy(client, game_data: dict, my_farm: dict):
    # employees assigned to fields
    three_and_four = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    five = [15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
    day = game_data["day"]

    if day == 0:
        client.add_command("0 EMPRUNTER 100000")
        for _ in range(5):
            client.add_command("0 ACHETER_CHAMP")
        for _ in range(25):
            client.add_command("0 EMPLOYER")
        client.add_command("1 SEMER PATATE 3")

        for employee in range(10):
            client.add_command(f"{three_and_four[employee]} ARROSER 3")
        client.add_command("14 SEMER PATATE 5")
        for employee in range(10):
            client.add_command(f"{five[employee]} ARROSER 5")

    if day == 2:
        client.add_command("13 CUISINER")

    if day == 4:
        client.add_command("1 SEMER POIREAU 4")
        for employee in range(10):
            client.add_command(f"{three_and_four[employee]} ARROSER 4")
        client.add_command("0 ACHETER_TRACTEUR")
        client.add_command("0 ACHETER_TRACTEUR")
        client.add_command("12 STOCKER 3 1")
    
    if day == 5:
        client.add_command("25 STOCKER 5 2")
