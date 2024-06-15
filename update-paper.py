import requests
import json
import hashlib
import os

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

build_info = requests.get(URL_BASE + "/v2/projects/paper/versions/" + selected_version + "/builds/" + str(build), headers=HEADERS)
build_info = build_info.json()
build_info = build_info.get("downloads")
build_info = build_info.get("application")
filename = build_info["name"]

print("File to download: " + filename)

sha256 = build_info["sha256"]

print("Downloading...")

response = requests.get(URL_BASE + "/v2/projects/paper/versions/" + selected_version + "/builds/" + str(build) + "/downloads/" + filename,)

with open(filename, 'wb') as f:
    f.write(response.content)
    
#Hash it to be sure nothing funky happened on the way.

file = filename # Location of the file (can be set a different way)
BLOCK_SIZE = 131072 # The size of each read from the file

file_hash = hashlib.sha256() # Create the hash object, can use something other than `.sha256()` if you wish
with open(file, 'rb') as f: # Open the file to read it's bytes
    fb = f.read(BLOCK_SIZE) # Read from the file. Take in the amount declared above
    while len(fb) > 0: # While there is still data being read from the file
        file_hash.update(fb) # Update the hash
        fb = f.read(BLOCK_SIZE) # Read the next block from the file

print("Hash of the downloaded file: " + str(file_hash.hexdigest())) # Get the hexadecimal digest of the hash

if str(file_hash.hexdigest()) == str(sha256):
    print("Hash OK")
else:
    print("Bad hash, incorrect or unexpected file. Exiting.")
    exit()
    
os.system("chmod a+x " + filename)
print("Now go change your server startup script and delete the old server jar.")