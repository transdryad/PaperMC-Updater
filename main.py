import argparse
import json
import os

import paper
import flags
import updatePlugins


# import updatePlugins
def create():
    print("creating the server...")
    info = paper.download()
    print(info)
    filename = info[0]
    version = info[1]
    memory_limit = int(input("Enter the amount of memory the server should have, in GB: "))
    flags.make_script(memory_limit, filename)
    os.system("chmod a+x " + "start.sh")
    with open("base.json", "r") as read_file:
        data = json.load(read_file)
    data["memory"] = memory_limit
    data["version"] = version
    with open("server.json", "w") as write_file:
        json.dump(data, write_file, indent=4)
    with open("eula.txt", "w") as eula_file:
        eula_file.write("eula=true")


def update():
    print("updating server file...")


def plugin_update():
    print("updating server plugins...")
    updatePlugins.update()


def install():
    print("installing")


parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(title="subcommands", help='help with subcommands', required=True)

parser_create = subparsers.add_parser("create",
                                      help="download a server for the first time and make a config and a startup file")
parser_create.set_defaults(func=create)

parser_update = subparsers.add_parser("update", help="update the papermc jar file and the startup script")
parser_update.set_defaults(func=update)

parser_plugin_update = subparsers.add_parser("update-plugins",
                                             help="update all currently installed plugins from their IDs in the config file")
parser_plugin_update.set_defaults(func=plugin_update)

parser_install = subparsers.add_parser("install", help="download the specified plugin and install it in the server")
#parser_install.add_argument("test")
parser_install.set_defaults(func=install)

args = parser.parse_args()
args.func()
