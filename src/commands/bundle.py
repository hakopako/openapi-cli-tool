from src.commands.list import path_list
from src.commands.resolve import get_spec_detail
from src.utils.export import export_json
from src.utils.file_control import get_spec_from_file


def _find_info_from_file(filename):
    data = get_spec_from_file(filename)
    if not isinstance(data, dict):
        data = dict()
    if 'paths' not in data:
        data['paths'] = {}
    return data


def run_bundle(spec_path, filename=None):
    paths = path_list(spec_path)
    data = {}
    if len(paths) > 0 and filename is None:
        data = _find_info_from_file(paths[0][2])
    elif filename is not None:
        data = _find_info_from_file(filename)

    for p in paths:
        spec = get_spec_detail(p[0], p[1], p[2])
        if p[1] not in data['paths']:
            data['paths'][p[1]] = {}
        data['paths'][p[1]].update({p[0].lower(): spec})

    return data


def bundle(spec_path, filename=None):
    specs = run_bundle(spec_path, filename)
    export_json(specs)
