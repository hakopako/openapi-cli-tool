import os
import json
import yaml
from glob import glob
from tabulate import tabulate

def _read_file(file_path):
    r = open(file_path, 'r')
    content = r.read()
    r.close()
    return content


def _load_content(content, file_extension):
    try:
        return json.loads(content) if file_extension == 'json' else yaml.safe_load(content)
    except:
        return ''


def _sort_paths(paths):
    try:
        paths.sort(lambda x,y: cmp(x[1], y[1]), lambda x,y: cmp(x[0], y[0]))
    except:
        paths.sort(key=lambda x: (x[1], x[0]))


def _export(export_data):
    print(tabulate(export_data, headers=['Method', 'Path', 'File']))


def path_list(path):
    paths = []
    if os.path.isfile(path):
        files = [path]
    else:
        files = [y for x in os.walk(path) for y in glob(os.path.join(x[0], '*.yml')) + glob(os.path.join(x[0], '*.json'))]
    for file in files:
        _, file_extension = os.path.splitext(file)
        content = _read_file(file)
        try:
            spec = _load_content(content, file_extension)
            routes = [[m.upper(), p, file] for p in spec['paths'] for m in spec['paths'][p]]
            paths.extend(routes)
        except:
            print('parse error: file=' + file)

    _sort_paths(paths)
    _export(paths)
    return paths
