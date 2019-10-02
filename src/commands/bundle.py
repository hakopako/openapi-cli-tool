from src.commands.list import get_list
from src.utils.resolver import resolver
from src.utils.export import export_json, export_yaml, export_html
from src.utils.file_control import FileControl


def run_bundle(spec_paths, filename=None):
    file_control = FileControl()
    collection = get_list(spec_paths)
    if collection.len() == 0 and filename is None:
        return {}
    elif collection.len() > 0 and filename is None:
        header_file = collection.get()[0].file
    elif filename is not None:
        header_file = filename
    try:
        data = file_control.load_dict_from_file(header_file)
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
        resolved_spec = resolver(route.file, route.spec, file_control)
        data['paths'][route.url].update({route.method.lower(): resolved_spec})

    return data


def bundle(spec_paths, type, filename=None):
    specs = run_bundle(spec_paths, filename)
    if type == 'json':
        export_json(specs)
    elif type == 'yaml':
        export_yaml(specs)
    elif type == 'html':
        export_html(specs)
