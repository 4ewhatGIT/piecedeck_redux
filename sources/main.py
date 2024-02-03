import json
from random import randint as rint
from time import sleep

import importer

importer.do("../plugins", globals())

CONFIG = "config.json"


def initialize(config: str) -> dict:
    with open(config, "r") as file:
        config = json.load(file)
    return config


def title_screen(PD_NAME, VERSION) -> None:
    print("Loading", end='')
    i = 0
    target = 3
    while i < target:
        if rint(0, 2) == 0:
            i += 1
            print(".", end='')
            sleep(rint(2, 10) / 10)
        sleep(0.2)
    print()
    print(f"Welcome to {PD_NAME} version {VERSION}!")


def selector_screen(modules: list) -> None:
    selector_active = True
    while selector_active:
        pass


def main() -> None:
    config = initialize(CONFIG)
    PD_NAME = config["PD_NAME"]
    dev_mode = config["dev_mode"]
    VERSION = config["VERSION"]
    if dev_mode:
        print(f"< {PD_NAME} config:")
        for k in config.keys():
            print(f"<< {k} = {config[k]}")
    title_screen(PD_NAME, VERSION)
