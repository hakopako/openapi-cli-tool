from src.commands.list import get_list
from src.utils.file_control import load_dict_from_file
from src.utils.resolver import resolver
from src.utils.export import export_json


def get_spec_detail(method, path, sepc_file):
    spec = load_dict_from_file(sepc_file)
    spec = spec['paths'][path][method.lower()]
    spec = resolver(sepc_file, spec)
    return spec


def run_resolve(method, path, spec_path):
    paths = get_list(spec_path)
    specs = [get_spec_detail(p[0], p[1], p[2]) for p in paths if p[0] == method.upper() and p[1] == path]
    return specs


def resolve(method, path, spec_path):
    specs = run_resolve(method, path, spec_path)
    for s in specs:
        export_json(s)
    if len(specs) > 1:
        print("\nWARNING: multiple specifications found for " + p[0] + ' ' + p[1])
