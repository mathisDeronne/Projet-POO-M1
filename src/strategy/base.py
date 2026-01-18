import argparse
from typing import NoReturn

from chronobio.network.client import Client


def strategy_used(client: "PlayerGameClient", game_data: dict, my_farm: dict) -> None:
    if game_data["day"] == 0:
        client.add_command("0 EMPRUNTER 100000")
        client.add_command("0 ACHETER_CHAMP")
        client.add_command("0 ACHETER_CHAMP")
        client.add_command("0 ACHETER_CHAMP")
        client.add_command("0 ACHETER_TRACTEUR")
        client.add_command("0 ACHETER_TRACTEUR")
        client.add_command("0 EMPLOYER")
        client.add_command("0 EMPLOYER")
        client.add_command("1 SEMER PATATE 3")


class PlayerGameClient(Client):
    def __init__(
        self: "PlayerGameClient", server_addr: str, port: int, username: str, strategy
    ) -> None:
        super().__init__(server_addr, port, username, spectator=False)
        self._commands: list[str] = []
        self.strategy = strategy
        self.vente1 = 0

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

            self.strategy(self, game_data, my_farm)
            self.send_commands()

    def add_command(self: "PlayerGameClient", command: str) -> None:
        self._commands.append(command)

    def send_commands(self: "PlayerGameClient") -> None:
        data = {"commands": self._commands}
        print("sending", data)
        self.send_json(data)
        self._commands.clear()


def main(
    username: str, address: str = "localhost", port: int = 16210, strategy=strategy_used
):
    client = PlayerGameClient(address, port, username, strategy)
    client.run()


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
        default=16210,
    )
    parser.add_argument(
        "-u",
        "--username",
        type=str,
        help="name of the user",
        default="unknown",
        required=True,
    )
    args = parser.parse_args()

    main(args.username, args.address, args.port)
