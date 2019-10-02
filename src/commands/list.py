import os
from glob import glob
from src.utils.file_control import FileControl
from src.utils.export import export_table
from src.models.route import Route
from src.models.route_collection import RouteCollection


def get_list(paths):
    file_control = FileControl()
    collection = RouteCollection()
    files = [p for p in paths if os.path.isfile(p)]
    for file in files:
        try:
            spec = file_control.load_dict_from_file(file)
            if 'paths' not in spec or len(spec['paths']) == 0:
                continue
            routes = [Route(m.upper(), p, file, spec['paths'][p][m]) for p in spec['paths'] for m in spec['paths'][p]]
            collection.extend(routes)
        except Exception as e:
            print(e)
            return RouteCollection()

    collection.sort()
    return collection


def list(paths):
    routes = get_list(paths)
    export_table(routes.to_list(), ['Method', 'Path', 'File'])
