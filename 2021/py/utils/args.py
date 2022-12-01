import argparse
import logging
from dataclasses import dataclass

@dataclass(frozen=True)
class Config:
    log_level: str

def get_args() -> Config:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--log-level",
        default=logging.getLevelName(logging.WARNING),
        choices=logging._nameToLevel.keys(),
        help="Log level"
    )

    args = parser.parse_args()

    return Config(args.log_level.upper())
