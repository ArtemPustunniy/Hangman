import logging
import platform
from src.Game.GameLogic import Play

logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)
logger = logging.getLogger(__name__)


def main() -> None:
    logger.info(platform.python_version())
    new_game = Play()
    new_game.start_game()


if __name__ == "__main__":
    main()
