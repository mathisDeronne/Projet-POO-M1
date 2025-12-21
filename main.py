from src.stratégie.base import main as run_client
from src.stratégie.damien_bloucle2 import strategy as strategy_used

if __name__ == "__main__":
    run_client(
        username="Les potes âgés",
        address="127.0.0.1",
        port=12345,
        strategy=strategy_used,
    )
