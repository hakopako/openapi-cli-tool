from src.commands.list import get_list
from src.utils.resolver import resolver
from src.utils.export import export_json, export_yaml
from src.utils.file_control import FileControl


def run_resolve(method, path, spec_paths):
    file_control = FileControl()
    collection = get_list(spec_paths)
    specs = [resolver(route.file, route.spec, file_control) for route in collection.get() if route.method == method.upper() and route.url == path]
    return specs


def resolve(method, path, spec_paths, type):
    specs = run_resolve(method, path, spec_paths)
    if type == 'json':
        export_json(specs)
    elif type == 'yaml':
        export_yaml(specs)
    if len(specs) > 1:
        print("\nWARNING: multiple specifications found for " + method + ' ' + path)
