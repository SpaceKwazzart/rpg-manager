import logging
import os
from dotenv import load_dotenv

load_dotenv(
    dotenv_path=os.path.join(
        os.path.dirname(__file__), '../..', '.env'
    )
)

LEVEL_LOGGING = os.getenv('LEVEL_LOGGING')

print(os.path.join(
    os.path.dirname(__file__), '../..', '.env'
))

logger = logging.getLogger('dices_logger')
logger.setLevel(LEVEL_LOGGING)

file_handler = logging.FileHandler('dices.log')
file_handler.setLevel(LEVEL_LOGGING)

console_handler = logging.StreamHandler()
console_handler.setLevel(LEVEL_LOGGING)

formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)
