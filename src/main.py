import click
from src.commands.scaffold import scaffold
from src.commands.list import list
from src.commands.resolve import resolve
from src.commands.bundle import bundle


def validate_type(ctx, param, value):
    if value in ['json', 'yaml']:
        return value
    else:
        raise click.BadParameter('type need to be json or yaml.')


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
@click.option('-t', '--type', 'type', default='json', show_default=True, callback=validate_type, help='Export data type. {json|yaml}')
def cmd_resolve(method, path, file_path, type):
    resolve(method, path, file_path, type)


@main.command('bundle', help='Bundle multi-file into one.')
@click.option('-f', '--file', 'file', help='Load common objects such as info and servers from a specific file. Default is a file which is the top of list command result.')
@click.option('-t', '--type', 'type', default='json', show_default=True, callback=validate_type, help='Export data type. {json|yaml}')
@click.argument('file_path')
def cmd_bundle(file, type, file_path):
    bundle(file_path, type, file)


@main.command('scaffold', help='Interactively create a simple OpenAPI Specification.')
def cmd_scaffold():
    scaffold()


if __name__ == '__main__':
    main()
