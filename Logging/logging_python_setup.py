import os
war_file_path = os.path.join("../logs/war/war.log")
recession_file_path = os.path.join("../logs/recession/recession.log")

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {"format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"},
    },
    "handlers": {
        "war_file": {
            "class": "logging.FileHandler",
            "filename": war_file_path,
            "formatter": "standard",
            "level": "INFO",
        },
        "recession_file": {
                    "class": "logging.FileHandler",
                    "filename": recession_file_path,
                    "formatter": "standard",
                    "level": "INFO",
                },
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "standard",
            "level": "INFO",
        },
    },
    "loggers": {
        "war_logger": {
            "handlers": ["war_file","console"],
            "level": "DEBUG",
            "propagate": False,
        },
        "recession_logger": {
            "handlers": ["recession_file","console"],
            "level": "DEBUG",
            "propagate": False,
        },
    },
}