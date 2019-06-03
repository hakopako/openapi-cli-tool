from src.commands.list import path_list
from src.commands.resolve import get_spec_detail
from src.utils.export import export_json

data = {
    'openapi': '3.0.0',
    'info': {'title': '', 'version': '', 'license': {'name': ''}},
    'servers': [{'url': ''}],
    'paths': {}
}


def run_bundle(spec_path):
    paths = path_list(spec_path)
    for p in paths:
        spec = get_spec_detail(p[0], p[1], p[2])
        if p[1] not in data['paths']:
            data['paths'][p[1]] = {}
        data['paths'][p[1]].update({p[0].lower(): spec})
    return data


def update_info_block(title, version, license, server):
    data['info']['title'] = title
    data['info']['version'] = version
    data['info']['license']['name'] = license
    data['servers'] = [{'url': server}]


def bundle(spec_path):
    specs = run_bundle(spec_path)
    export_json(specs)
