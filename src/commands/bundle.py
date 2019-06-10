from src.commands.list import get_list
from src.utils.resolver import resolver
from src.utils.export import export_json, export_yaml
from src.utils.file_control import load_dict_from_file


def run_bundle(spec_path, filename=None):
    collection = get_list(spec_path)
    if collection.len() == 0 and filename is None:
        return {}
    elif collection.len() > 0 and filename is None:
        header_file = collection.get()[0].file
    elif filename is not None:
        header_file = filename
    try:
        data = load_dict_from_file(header_file)
        if isinstance(data, dict):
            data['paths'] = {}
            data.pop('components', None)
        else:
            raise Exception('Parse Error: ' + header_file)
    except Exception as e:
        print(e)
        return {}

    for route in collection.get():
        if route.url not in data['paths']:
            data['paths'][route.url] = {}
        resolved_spec = resolver(route.file, route.spec)
        data['paths'][route.url].update({route.method.lower(): resolved_spec})

    return data


def bundle(spec_path, type, filename=None):
    specs = run_bundle(spec_path, filename)
    if type == 'json':
        export_json(specs)
    elif type == 'yaml':
        export_yaml(specs)
