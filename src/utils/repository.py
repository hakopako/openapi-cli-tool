import os
from src.utils.file_control import FileControl
from src.utils.resolver import resolve_once
from src.models.route import Route
from src.models.route_collection import RouteCollection


class Repository:

    def __init__(self, file_path, file_control = FileControl()):
        self.file_control = file_control
        self.routes = self.generate(file_path)

    def _set_from_file(self, collection, file):
        content = self.file_control.load_dict_from_file(file)
        if 'paths' not in content or len(content['paths']) == 0:
            return
        for path, spec in content['paths'].items():
            spec = resolve_once(file, spec, self.file_control)
            for method in spec:
                collection.add(
                    Route(
                        method.upper(), 
                        path, 
                        file, 
                        spec[method]
                    ))

    def generate(self, file_path):
        collection = RouteCollection()
        files = [p for p in file_path if os.path.isfile(p)]
        for file in files:
            try:
                self._set_from_file(collection, file)
            except Exception as e:
                raise Exception(e)
        collection.sort()
        return collection
