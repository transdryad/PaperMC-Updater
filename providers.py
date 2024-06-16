import requests
import hash


def download(plugin, server_ver, headers):
    global response
    name = plugin["name"]
    provider = plugin["provider"]
    plugin_id = plugin["id"]

    if provider == "modrinth":
        print("Downloading " + name + " from Modrinth...")
        response = requests.get('https://api.modrinth.com/v2/project/' + plugin_id, headers=headers, allow_redirects=True)
        response = response.json()
        if server_ver in response["game_versions"]:
            params = {
                'game_versions': '["' + server_ver + '"]',
                'loaders': '["paper", "spigot", "bukkit"]'
            }
            versions = requests.get('https://api.modrinth.com/v2/project/' + plugin_id + "/version", params=params,
                                    headers=headers, allow_redirects=True)
            versions = versions.json()
            expected_hash = versions[0]["files"][0]["hashes"]["sha512"]
            url = versions[0]["files"][0]["url"]
            filename = versions[0]["files"][0]["filename"]
            filename = "./plugins/update/" + filename

            response = requests.get(url)
            with open(filename, 'wb') as f:
                f.write(response.content)

            new_hash = hash.hasher(filename, 512)

            if not new_hash == str(expected_hash):
                print("Bad hash, incorrect or unexpected file. Please Manually check the file.")
        else:
            print("There is no available version of " + name + " for " + server_ver + ". Sorry")

    elif provider == "github":
        print("Downloading " + name + " from Github...")
        response = requests.get("https://api.github.com/repos/" + plugin_id + "/releases", headers=headers, allow_redirects=True)
        releases = response.json()
        release = releases[0]  # Is a dictionary
        filename = release["assets"][0]["name"]
        filename = "./plugins/update/" + filename
        download_url = release["assets"][0]["browser_download_url"]

        new_file = requests.get(download_url)
        with open(filename, 'wb') as f:
            f.write(new_file.content)
    elif provider == "spigot":
        print("Downloading " + name + " from Spigot...")
        filename = "./plugins/update/" + name + ".jar"
        response = requests.get("https://api.spiget.org/v2/resources/" + plugin_id + "/download", headers=headers,
                                allow_redirects=True)
        with open(filename, 'wb') as f:
            f.write(response.content)
    elif provider == "geyser":
        print("Downloading " + name + " from the GeyserMC website...")
        filename = "./plugins/update/" + name + "-Spigot.jar"
        if id == "geyser":
            response = requests.get(
                "https://download.geysermc.org/v2/projects/geyser/versions/latest/builds/latest/downloads/spigot",
                headers=headers, allow_redirects=True)
        if id == "floodgate":
            response = requests.get(
                "https://download.geysermc.org/v2/projects/floodgate/versions/latest/builds/latest/downloads/spigot",
                headers=headers, allow_redirects=True)
        with open(filename, 'wb') as f:
            f.write(response.content)
