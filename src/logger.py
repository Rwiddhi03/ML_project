import os
import logging


logs_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_dir, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_dir, "app.log")


logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s]: %(lineno)d %(name)s | %(levelname)s - %(message)s",
    level=logging.INFO,
    datefmt="%Y-%m-%d %H:%M:%S"
)

logger = logging.getLogger(__name__)

