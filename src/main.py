"""OpenAPI CLI Tool

Usage:
  openapi-cli-tool list <spec-path>
  openapi-cli-tool search <keyword> <spec-path>
  openapi-cli-tool find <method> <path> <spec-path>
  openapi-cli-tool scaffold

Options:
  -h --help     Show this screen.
  --version     Show version.
  --speed=<kn>  Speed in knots [default: 10].
  --moored      Moored (anchored) mine.
  --drifting    Drifting mine.

"""
from docopt import docopt
from command.scaffold import scaffold
from command.list import path_list

def main():
    arguments = docopt(__doc__, version='OpenAPI CLI Tool 0.1')
    if arguments['scaffold']:
        scaffold()
    elif arguments['list']:
        path_list(arguments['<spec-path>'])
    elif arguments['search']:
        pass

if __name__ == '__main__':
    main()
