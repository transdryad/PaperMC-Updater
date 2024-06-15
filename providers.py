import requests
import hash


def download(plugin, server_ver, headers):
    name = plugin["name"]
    provider = plugin["provider"]
    plugin_id = plugin["id"]

    if provider == "modrinth":
        print("Downloading " + name + " from Modrinth...")
        response = requests.get('https://api.modrinth.com/v2/project/' + plugin_id, headers=headers)
        response = response.json()
        if server_ver in response["game_versions"]:
            params = {
                'game_versions': '["' + server_ver + '"]'
            }
            versions = requests.get('https://api.modrinth.com/v2/project/' + plugin_id + "/version", params=params,
                                    headers=headers)
            versions = versions.json()
            expected_hash = versions[0]["files"][0]["hashes"]["sha512"]
            url = versions[0]["files"][0]["url"]
            filename = versions[0]["files"][0]["filename"]
            filename = "./plugins/update/" + filename

            response = requests.get(url)
            with open(filename, 'wb') as f:
                f.write(response.content)

            new_hash = hash.hasher(filename, 512)
            print("Hash of the downloaded file: " + new_hash)  # Get the hexadecimal digest of the hash

            if new_hash == str(expected_hash):
                print("Hash OK")
            else:
                print("Bad hash, incorrect or unexpected file. Please Manually check the file.")
        else:
            print("There is no available version of " + name + " for " + server_ver + ". Sorry")

    elif provider == "github":
        print("Downloading " + name + " from Github...")
        response = requests.get("https://api.github.com/repos/" + plugin_id + "/releases", headers=headers)
        releases = response.json()
        release = releases[0]  # Is a dictionary
        filename = release["assets"][0]["name"]
        filename = "./plugins/update/" + filename
        download_url = release["assets"][0]["browser_download_url"]

        new_file = requests.get(download_url)
        with open(filename, 'wb') as f:
            f.write(new_file.content)
