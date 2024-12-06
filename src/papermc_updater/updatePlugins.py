import json
from .providers import download
import os

headers = {
    'Content-Type': 'application/json',
    'User-Agent': 'transdryad/PaperMC-Updater/1.0 (viswanath.hazel@gmail.com)',
    'accept': 'application/json',
}


def update_plugins(init):
    print("Grabbing server info...")

    with open("server.json", "r") as read_file:
        server_info = json.load(read_file)

    plugins = server_info["plugins"]
    if not os.path.exists("./plugins/update"):
        os.makedirs("./plugins/update")
    if plugins:
        for x in plugins:
            download(x, headers, init)
    else:
        print(
            "No plugins are available to be updated. Either you have no installed plugins or the plugins haven't been properly added to server.json.")
