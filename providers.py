import requests
def download(plugin, server_ver, headers):
    #print(plugin)
    name = plugin["name"]
    provider = plugin["provider"]
    url = plugin["url"]
    current_version = plugin["version"]
    id = plugin["id"]
    
    if provider == "modrinth":
        print("Downloading " + name + " from Modrinth.")
        response = requests.get('https://api.modrinth.com/v2/project/' + id, headers=headers)
        response = response.json()
        if server_ver in response["game_versions"]: 
            print("b")
        else:
            print("There is no available version of " + name + " for " + server_ver)