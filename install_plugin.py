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
    plugin = {"name": name, "provider": provider, "id": identifier}
    if plugin in server_info["plugins"]:
        print("You may not install multiple copies of the same plugin!")
        return
    server_info["plugins"].append(plugin)
    with open("server.json", "w") as write_file:
        json.dump(server_info, write_file, indent=4)
    providers.download(plugin, headers, True)
