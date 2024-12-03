import providers
import json

headers = {
    'Content-Type': 'application/json',
    'User-Agent': 'transdryad/PaperMC-Updater/1.0 (viswanath.hazel@gmail.com)',
    'accept': 'application/json',
}


def install(name, provider, identifier):
    with open("server.json", "r") as read_file:
        server_info = json.load(read_file)
    version = server_info["version"]
    plugin = {"name": name, "provider": provider, "id": identifier}
    server_info["plugins"].append(plugin)
    with open("server.json", "w") as write_file:
        json.dump(server_info, write_file, indent=4)
    providers.download(plugin, version, headers, True)
