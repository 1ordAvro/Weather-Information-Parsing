import logging

class My_logger:
    def __init__(self):
        self.formatter = logging.Formatter("%(levelname)s:%(asctime)s:%(name)s:%(message)s")

        self.info_logger = logging.getLogger("info")
        self.critical_logger = logging.getLogger("critical")
        self.error_logger = logging.getLogger("error")

        for logger, filename, level in [
            (self.info_logger,"fetched_info.log", logging.INFO),
            (self.critical_logger, "fetched_critical.log", logging.CRITICAL),
            (self.error_logger, "fetched_exception.log", logging.ERROR)
        ]:
            logger.setLevel(level)
            handler = logging.FileHandler(filename)
            handler.setFormatter(self.formatter)
            logger.addHandler(handler)

    def log_info(self, msg):
        self.info_logger.info(msg)

    def log_critical(self, msg):
        self.critical_logger.critical(msg)

    def log_exception(self, msg):
        self.error_logger.exception(msg)