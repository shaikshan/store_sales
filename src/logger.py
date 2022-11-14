import logging

from datetime import datetime
import os
from src.constants import get_current_time_stamp

LOG_DIR = 'logs'

LOG_FILE_NAME = get_current_time_stamp()

os.makedirs(LOG_DIR,exist_ok=True)

LOG_FILE_PATH = os.path.join(LOG_DIR,LOG_FILE_NAME)


logging.basicConfig(filename=LOG_FILE_PATH,
                    filemode='w',
                    format='[%(asctime)s]^;%(levelname)s^;%(lineno)s^;%(filename)s^;%(funcName)s()^;%(message)s',
                    level=logging.INFO
                    )

