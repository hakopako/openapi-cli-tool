from src.commands.list import get_list
from src.commands.resolve import get_spec_detail
from src.utils.export import export_json
from src.utils.file_control import load_dict_from_file


def run_bundle(spec_path, filename=None):
    paths = get_list(spec_path)
    if len(paths) == 0 and filename is None:
        return {}
    elif len(paths) > 0 and filename is None:
        header_file = paths[0][2]
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

    for p in paths:
        spec = get_spec_detail(p[0], p[1], p[2])
        if p[1] not in data['paths']:
            data['paths'][p[1]] = {}
        data['paths'][p[1]].update({p[0].lower(): spec})

    return data


def bundle(spec_path, filename=None):
    specs = run_bundle(spec_path, filename)
    export_json(specs)
