import json
from random import randint as rint
from time import sleep

from stock import *
from sources import importer

plugins = list(importer.__get_module_names_in_dir("../plugins"))
for i in range(len(stock_plugins)):
    plugins.append(stock_plugins[i])
importer.do("../plugins", globals())
print(plugins)
print(globals())
CONFIG = "../config.json"


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
    print(f"Welcome to {PD_NAME} v{VERSION}!")


def selector_screen(plugins: list, PD_NAME, VERSION) -> None:
    selector_active = True
    while selector_active:
        p = 0
        for i in range(len(plugins)):
            print(f'{i + 1}: {plugins[i]}')
            p = i + 2
        print(f'{p}: exit {PD_NAME} v{VERSION}')
        selected = input('Select a plugin to run: ')
        if selected.isdigit():
            if int(selected) - 1 < len(plugins):
                func = globals()[plugins[int(selected) - 1]].script
                func()
            else:
                print(f'Thank you for using {PD_NAME} v{VERSION}!')
                exit()
        else:
            print('Input only integers!')
            continue



def main() -> None:
    config = initialize(CONFIG)
    PD_NAME = config["PD_NAME"]
    dev_mode = config["dev_mode"]
    VERSION = config["VERSION"]
    print(plugins)
    if dev_mode:
        print(f"< {PD_NAME} config:")
        for k in config.keys():
            print(f"<< {k} = {config[k]}")
    title_screen(PD_NAME, VERSION)
    selector_screen(plugins, PD_NAME, VERSION)


if __name__ == '__main__':
    main()
