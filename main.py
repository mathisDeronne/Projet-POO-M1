from src.strategy.base import main as run_client
from src.strategy.damien_bloucle2 import strategy as strategy_used
import argparse

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
    args = parser.parse_args()

    run_client(
        username="Les potes âgés",
        address=args.address,
        port=args.port,
        strategy=strategy_used,
    )
