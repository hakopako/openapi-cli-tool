import click
from src.commands.scaffold import scaffold
from src.commands.list import list
from src.commands.resolve import resolve
from src.commands.bundle import bundle


def validate_resolve_type(ctx, param, value):
    if value in ['json', 'yaml']:
        return value
    else:
        raise click.BadParameter('type need to be json or yaml.')


def validate_bundle_type(ctx, param, value):
    if value in ['json', 'yaml', 'html']:
        return value
    else:
        raise click.BadParameter('type need to be json, yaml or html.')


@click.group()
def main():
    pass


@main.command('list', help='List up API paths in a file or directory.')
@click.argument('file_paths', nargs=-1, type=click.Path(exists=True))
def cmd_list(file_paths):
    list(file_paths)


@main.command('resolve', help='Display `$ref` resolved API specification.')
@click.argument('method')
@click.argument('path')
@click.argument('file_paths', nargs=-1, type=click.Path(exists=True))
@click.option('-t', '--type', 'type', default='json', show_default=True, callback=validate_resolve_type, help='Export data type. {json|yaml}')
def cmd_resolve(method, path, file_paths, type):
    resolve(method, path, file_paths, type)


@main.command('bundle', help='Bundle multiple files into one.')
@click.option('-f', '--file', 'file', help='Load common objects such as info and servers from a specific file. Default is a file which is the top of list command result.')
@click.option('-t', '--type', 'type', default='json', show_default=True, callback=validate_bundle_type, help='Export data type. {json|yaml|html}')
@click.argument('file_paths', nargs=-1, type=click.Path(exists=True))
def cmd_bundle(file, type, file_paths):
    bundle(file_paths, type, file)


@main.command('scaffold', help='Interactively create a simple OpenAPI Specification.')
def cmd_scaffold():
    scaffold()


if __name__ == '__main__':
    main()
