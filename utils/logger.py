import logging
from tqdm import tqdm


class TqdmLoggingHandler(logging.Handler):
    def __init__(self, level=logging.NOTSET):
        super().__init__(level)

    def emit(self, record):
        try:
            msg = self.format(record)
            tqdm.write(msg)
            self.flush()
        except Exception:
            self.handleError(record)


def get_logger(task_log_file="task.log", mode='a'):
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # 配置日志格式
    formatter = logging.Formatter(
        fmt="%(asctime)s.%(msecs)03d %(levelname)-8s \
  [%(filename)s %(funcName)s: %(lineno)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # 添加适配 tqdm 的 stream 处理器
    stream_handler = TqdmLoggingHandler()
    stream_handler.setLevel(logging.DEBUG)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    # 添加日志文件处理器
    logfile_handler = logging.FileHandler(task_log_file, mode=mode)
    logfile_handler.setLevel(logging.INFO)
    logfile_handler.setFormatter(formatter)
    logger.addHandler(logfile_handler)

    return logger
