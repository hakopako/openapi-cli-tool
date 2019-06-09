import os
from glob import glob
from src.utils.file_control import load_dict_from_file
from src.utils.export import export_table
from src.models.route import Route
from src.models.route_collection import RouteCollection


def get_list(path):
    collection = RouteCollection()
    if os.path.isfile(path):
        files = [path]
    else:
        files = [y for x in os.walk(path) for y in glob(os.path.join(x[0], '*.yml')) + glob(os.path.join(x[0], '*.yaml')) + glob(os.path.join(x[0], '*.json'))]
    for file in files:
        try:
            spec = load_dict_from_file(file)
            if 'paths' not in spec or len(spec['paths']) == 0:
                continue
            routes = [Route(m.upper(), p, file, spec['paths'][p][m]) for p in spec['paths'] for m in spec['paths'][p]]
            collection.extend(routes)
        except Exception as e:
            print(e)
            return RouteCollection()

    collection.sort()
    return collection


def list(path):
    routes = get_list(path)
    export_table(routes.to_list(), ['Method', 'Path', 'File'])
