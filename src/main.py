"""OpenAPI CLI Tool

Usage:
  openapi-cli-tool list <spec-path>
  openapi-cli-tool resolve <method> <path> <spec-path>
  openapi-cli-tool scaffold

Options:
  -h --help     Show help.
  --version     Show version.

"""
from docopt import docopt
from src.commands.scaffold import scaffold
from src.commands.list import list
from src.commands.resolve import resolve

def main():
    arguments = docopt(__doc__, version='OpenAPI CLI Tool 0.1')
    if arguments['scaffold']:
        scaffold()
    elif arguments['list']:
        list(arguments['<spec-path>'])
    elif arguments['resolve']:
        resolve(arguments['<method>'], arguments['<path>'], arguments['<spec-path>'])

if __name__ == '__main__':
    main()
