import os
from glob import glob
from src.utils.file_control import FileControl
from src.utils.export import export_table
from src.utils.resolver import resolve_once
from src.models.route import Route
from src.models.route_collection import RouteCollection


def get_list(paths):
    file_control = FileControl()
    collection = RouteCollection()
    files = [p for p in paths if os.path.isfile(p)]
    for file in files:
        try:
            contents = file_control.load_dict_from_file(file)
            if 'paths' not in contents or len(contents['paths']) == 0:
                continue
            for path, spec in contents['paths'].items():
                if '$ref' in spec:
                    spec = resolve_once(file, spec, file_control)
                for method in spec:
                    collection.add(
                        Route(
                            method.upper(),
                            path,
                            file,
                            spec[method]
                        )
                    )
        except Exception as e:
            print(e)
            return RouteCollection()
    collection.sort()
    return collection


def list(paths):
    routes = get_list(paths)
    export_table(routes.to_list(), ['Method', 'Path', 'File'])
