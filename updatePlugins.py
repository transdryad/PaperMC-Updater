import json
import providers

headers = {
    'Content-Type': 'application/json',
    'User-Agent': 'transdryad/PaperMC-Updater/1.0 (viswanath.hazel@gmail.com)',
    'accept': 'application/json',
}


def update():
    print("Grabbing server info...")

    with open("server.json", "r") as read_file:
        server_info = json.load(read_file)

    plugins = server_info["plugins"]
    version = server_info["version"]

    if plugins:
        for x in plugins:
            providers.download(x, version, headers)
    else:
        print(
            "No plugins are available to be updated. Either you have no installed plugins or the plugins haven't been properly added to server.json")
