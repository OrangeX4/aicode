from utils.logger import get_logger
import os

logger = get_logger(os.path.join(os.path.dirname(__file__), "task.log"))

logger.info("yes")
