import argparse

import paper


#import paper
#import updatePlugins
def create():
    return


def update():
    paper.download()


def plugin_update():
    return


def install():
    return


parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(help='help with subcommands')

parser_create = subparsers.add_parser("create", help="download a server for the first time and make a config and a startup file")
parser_create.set_defaults(func=create)

parser_update = subparsers.add_parser("update", help="update the papermc jar file and the startup script")
parser_update.set_defaults(func=update())

parser_plugin_update = subparsers.add_parser("update-plugins", help="update all currently installed plugins from their IDs in the config file")
parser_plugin_update.set_defaults(func=plugin_update)

parser_install = subparsers.add_parser("install", help="download the specified plugin and install it in the server")
#parser_install.add_argument()
parser_install.set_defaults(func=install)

args = parser.parse_args()
