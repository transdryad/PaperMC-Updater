import requests
import hash
import os
import json

URL_BASE = 'https://api.papermc.io'

HEADERS = {
    'Content-Type': 'application/json',
    'User-Agent': 'transdryad/PaperMC-Updater/1.0 (viswanathsam@gmail.com)',
    'accept': 'application/json',
}

print("Querying version list from PaperMC...")

versions = requests.get(URL_BASE + '/v2/projects/paper', headers=HEADERS)

versions = versions.json()
ver_list = versions.get("versions")
print("Current Version list for PaperMC:")
print(ver_list)

selected_version = input("Choose a version: ")

builds = requests.get(URL_BASE + '/v2/projects/paper/versions/' + selected_version, headers=HEADERS)
builds = builds.json()
build_list = builds.get("builds")
build = build_list[-1]
print("Latest Build: " + str(build))

build_info = requests.get(URL_BASE + "/v2/projects/paper/versions/" + selected_version + "/builds/" + str(build),
                          headers=HEADERS)
build_info = build_info.json()
build_info = build_info.get("downloads")
build_info = build_info.get("application")
filename = build_info["name"]

print("File to download: " + filename)

sha256 = build_info["sha256"]

print("Downloading...")

response = requests.get(
    URL_BASE + "/v2/projects/paper/versions/" + selected_version + "/builds/" + str(build) + "/downloads/" + filename, )

with open(filename, 'wb') as f:
    f.write(response.content)

# Hash it to be sure nothing funky happened on the way.

new_hash = hash.hasher(filename, 256)
print("Hash of the downloaded file: " + new_hash)  # Get the hexadecimal digest of the hash

if new_hash == str(sha256):
    print("Hash OK")
else:
    print("Bad hash, incorrect or unexpected file. Exiting.")
    exit()

os.system("chmod a+x " + filename)

with open("server.json", "r") as read_file:
    data = json.load(read_file)

data["version"] = selected_version

with open("server.json", "w") as write_file:
    json.dump(data, write_file, indent=4)

print("Now go change your server startup script and delete the old server jar.")
