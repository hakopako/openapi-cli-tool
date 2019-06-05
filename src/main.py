import click
from src.commands.scaffold import scaffold
from src.commands.list import list
from src.commands.resolve import resolve
from src.commands.bundle import bundle


@click.group()
def main():
    pass


@main.command('list', help='List up APIs in a specific file or directory.')
@click.argument('file_path', type=click.Path(exists=True))
def cmd_list(file_path):
    list(file_path)


@main.command('resolve', help='Display `$ref` resolved API specification.')
@click.argument('method')
@click.argument('path')
@click.argument('file_path')
def cmd_resolve(method, path, file_path):
    resolve(method, path, file_path)


@main.command('bundle', help='Bundle multi-file into one.')
@click.option('-f', '--file', 'file', help='load common objects from file.')
@click.argument('file_path')
def cmd_bundle(file, file_path):
    bundle(file_path, file)


@main.command('scaffold', help='Interactively create a simple OpenAPI Specification.')
def cmd_scaffold():
    scaffold()


if __name__ == '__main__':
    main()
