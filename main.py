from src.strategy.base import main as run_client
from src.strategy.guillaume import strategy as strategy_used
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Game client.")
    parser.add_argument(
        "-a",
        "--address",
        type=str,
        help="name of server on the network",
        default="127.0.0.1",
    )
    parser.add_argument(
        "-p",
        "--port",
        type=int,
        help="location where server listens",
        default=12345,
    )
    args = parser.parse_args()

    run_client(
        username="Les potes âgés",
        address=args.address,
        port=args.port,
        strategy=strategy_used,
    )
