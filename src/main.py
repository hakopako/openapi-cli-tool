import argparse
from scaffold import scaffold

def main():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('command', choices=['scaffold'])

    args = parser.parse_args()
    if args.command == 'scaffold':
        scaffold()


if __name__ == "__main__":
    main()
