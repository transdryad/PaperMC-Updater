import requests
import json
import hashlib
import os
import providers

headers = {
    'Content-Type': 'application/json',
    'User-Agent': 'transdryad/PaperMC-Updater/1.0 (viswanathsam@gmail.com)',
}

print("Grabbing server info...")

with open("server.json", "r") as read_file:
    server_info = json.load(read_file)

plugins = server_info["plugins"]
version = server_info["version"]

for x in plugins:
    providers.download(x, version, headers)