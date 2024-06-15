import requests
import hashlib
def download(plugin, server_ver, headers):
    #print(plugin)
    name = plugin["name"]
    provider = plugin["provider"]
    id = plugin["id"]
    
    if provider == "modrinth":
        print("Downloading " + name + " from Modrinth...")
        response = requests.get('https://api.modrinth.com/v2/project/' + id, headers=headers)
        response = response.json()
        if server_ver in response["game_versions"]:
            params = {
                'game_versions': '["' + server_ver + '"]'
            }
            versions = requests.get('https://api.modrinth.com/v2/project/' + id + "/version",params=params, headers=headers)
            versions = versions.json()
            hash = versions[0]["files"][0]["hashes"]["sha512"]
            url = versions[0]["files"][0]["url"]
            filename = versions[0]["files"][0]["filename"]
            
            response = requests.get(url,)
            
            with open(filename, 'wb') as f:
                f.write(response.content)
            
            file = filename # Location of the file (can be set a different way)
            BLOCK_SIZE = 131072 # The size of each read from the file

            file_hash = hashlib.sha512() # Create the hash object, can use something other than `.sha256()` if you wish
            with open(file, 'rb') as f: # Open the file to read it's bytes
                fb = f.read(BLOCK_SIZE) # Read from the file. Take in the amount declared above
                while len(fb) > 0: # While there is still data being read from the file
                    file_hash.update(fb) # Update the hash
                    fb = f.read(BLOCK_SIZE) # Read the next block from the file

            print("Hash of the downloaded file: " + str(file_hash.hexdigest())) # Get the hexadecimal digest of the hash

            if str(file_hash.hexdigest()) == str(hash):
                print("Hash OK")
            else:
                print("Bad hash, incorrect or unexpected file. Please Manually check the file.")
        else:
            print("There is no available version of " + name + " for " + server_ver + ". Sorry")