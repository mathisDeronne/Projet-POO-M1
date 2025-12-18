import argparse
from typing import NoReturn

from chronobio.network.client import Client


class PlayerGameClient(Client):
    def __init__(
        self: "PlayerGameClient", server_addr: str, port: int, username: str
    ) -> None:
        super().__init__(server_addr, port, username, spectator=False)
        self._commands: list[str] = []

    def run(self: "PlayerGameClient") -> NoReturn:
        while True:
            game_data = self.read_json()
            for farm in game_data["farms"]:
                if farm["name"] == self.username:
                    my_farm = farm
                    break
            else:
                raise ValueError(f"My farm is not found ({self.username})")
            print(my_farm)

            if game_data["day"] == 0:
                self.add_command("0 EMPRUNTER 100000")
                self.add_command("0 ACHETER_CHAMP")
                self.add_command("0 ACHETER_CHAMP")
                self.add_command("0 ACHETER_CHAMP")
                self.add_command("0 ACHETER_CHAMP")
                self.add_command("0 ACHETER_CHAMP")
                self.add_command("0 EMPLOYER")
                self.add_command("0 EMPLOYER")
                self.add_command("0 EMPLOYER")
                self.add_command("0 EMPLOYER")
                self.add_command("0 EMPLOYER")
                self.add_command("0 EMPLOYER")
                self.add_command("0 EMPLOYER")
                self.add_command("0 EMPLOYER")
                self.add_command("0 EMPLOYER")
                self.add_command("0 EMPLOYER")
                self.add_command("0 EMPLOYER")
                self.add_command("1 SEMER PATATE 1")
                self.add_command("2 ARROSER 1")
                self.add_command("3 ARROSER 1")
                self.add_command("4 ARROSER 1")
                self.add_command("5 ARROSER 1")
                self.add_command("6 ARROSER 1")
                self.add_command("7 ARROSER 1")
                self.add_command("8 ARROSER 1")
                self.add_command("9 ARROSER 1")
                self.add_command("10 ARROSER 1")
                self.add_command("11 ARROSER 1")


            if game_data["day"] == 1 :
                self.add_command("0 EMPLOYER")
                self.add_command("1 SEMER POIREAU 2")
                self.add_command("2 ARROSER 2")
                self.add_command("3 ARROSER 2")
                self.add_command("4 ARROSER 2")
                self.add_command("5 ARROSER 2")
                self.add_command("6 ARROSER 2")
                self.add_command("7 ARROSER 2")
                self.add_command("8 ARROSER 2")
                self.add_command("9 ARROSER 2")
                self.add_command("10 ARROSER 2")
                self.add_command("11 ARROSER 2")
                self.add_command("0 ACHETER_TRACTEUR")
                self.add_command("12 STOCKER 1 1")
                
                
            
            if game_data["day"] == 2 :
                self.add_command("1 SEMER TOMATE 3")
                self.add_command("2 ARROSER 3")
                self.add_command("3 ARROSER 3")
                self.add_command("4 ARROSER 3")
                self.add_command("5 ARROSER 3")
                self.add_command("6 ARROSER 3")
                self.add_command("7 ARROSER 3")
                self.add_command("8 ARROSER 3")
                self.add_command("9 ARROSER 3")
                self.add_command("10 ARROSER 3")
                self.add_command("11 ARROSER 3")
                self.add_command("0 VENDRE 2")

            if game_data["day"] == 60 :
                self.add_command("1 SEMER COURGETTE 4")
                self.add_command("2 ARROSER 4")
                self.add_command("3 ARROSER 4")
                self.add_command("4 ARROSER 4")
                self.add_command("5 ARROSER 4")
                self.add_command("6 ARROSER 4")
                self.add_command("7 ARROSER 4")
                self.add_command("8 ARROSER 4")
                self.add_command("9 ARROSER 4")
                self.add_command("10 ARROSER 4")
                self.add_command("11 ARROSER 4")
                self.add_command("12 CUISINER")

            if game_data["day"] == 61 :
                self.add_command("1 SEMER OIGNON 5")
                self.add_command("2 ARROSER 5")
                self.add_command("3 ARROSER 5")
                self.add_command("4 ARROSER 5")
                self.add_command("5 ARROSER 5")
                self.add_command("6 ARROSER 5")
                self.add_command("7 ARROSER 5")
                self.add_command("8 ARROSER 5")
                self.add_command("9 ARROSER 5")
                self.add_command("10 ARROSER 5")
                self.add_command("11 ARROSER 5")
                self.add_command("0 ARROSER 5")
                self.add_command("0 LICENCIER 1")
                self.add_command("0 LICENCIER 2")
                self.add_command("0 LICENCIER 3")
                self.add_command("0 LICENCIER 4")
                self.add_command("0 LICENCIER 5")
                self.add_command("0 LICENCIER 6")
                self.add_command("0 LICENCIER 7")
                self.add_command("0 LICENCIER 8")
                self.add_command("0 LICENCIER 9")
                self.add_command("0 LICENCIER 10")
                self.add_command("0 LICENCIER 11")
                self.add_command("0 LICENCIER 12")

                





            self.send_commands()

    def add_command(self: "PlayerGameClient", command: str) -> None:
        self._commands.append(command)

    def send_commands(self: "PlayerGameClient") -> None:
        data = {"commands": self._commands}
        print("sending", data)
        self.send_json(data)
        self._commands.clear()

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Game client.")

    parser.add_argument(
        "-a",
        "--address",
        type=str,
        help="name of server on the network",
        default="localhost",
    )
    parser.add_argument(
        "-p",
        "--port",
        type=int,
        help="location where server listens",
        default=12345,
    )
    parser.add_argument(
        "-u",
        "--username",
        type=str,
        help="name of the user",
        default="coucou",
        required=True,
    )
    args = parser.parse_args()

    client = PlayerGameClient(args.address, args.port, args.username).run()

    """
    & C:/Users/admin/PyCharmMiscProject/venv/Scripts/python.exe "c:/Users/admin/Desktop/ynov/projet chronobio/Projet-POO-M1/local_base.py" -a localhost -p 12345 -u tot 
    """

