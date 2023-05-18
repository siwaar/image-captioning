"""
Common helpers functions to log correctly on console
and files
"""

import logging
import os
import sys
import time
from typing import Optional, Tuple


def setup_logger(
    logger_name: str,
    output_folder: bool = False,
    console_level: int = logging.INFO,
    file_level: int = logging.DEBUG,
) -> Tuple[logging.Logger, Optional[str]]:
    """
    Setup logger for console and
    file output at the same time
    """
    base_path = os.path.join(".output", logger_name.split()[0])
    start_time = time.strftime("%Y%m%d_%H%M%S")

    if output_folder:
        writing_folder = os.path.join(base_path, start_time)
        os.makedirs(writing_folder, exist_ok=True)

    log_folder = os.path.join(base_path, ".logs")
    os.makedirs(log_folder, exist_ok=True)
    log_file = os.path.join(log_folder, f"run_{start_time}.log")

    logger = logging.Logger(logger_name)
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setFormatter(formatter)
    stream_handler.setLevel(console_level)
    logger.addHandler(stream_handler)

    file_handler = logging.FileHandler(filename=log_file)
    file_handler.setFormatter(formatter)
    file_handler.setLevel(file_level)
    logger.addHandler(file_handler)

    return logger, (writing_folder if output_folder else None)
