import logging


def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    if not logger.handlers:
        handler = logging.StreamHandler()
        handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter(
            "\033[97m%(asctime)s | %(name)s | %(levelname)s | %(message)s\033[0m"
        )

        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.propagate = False

    return logger
