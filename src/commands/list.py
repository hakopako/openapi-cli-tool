import os
from glob import glob
from src.utils.file_control import load_content, read_file
from src.utils.export import export_table


def _sort_paths(paths):
    try:
        paths.sort(lambda x,y: cmp(x[1], y[1]), lambda x,y: cmp(x[0], y[0]))
    except:
        paths.sort(key=lambda x: (x[1], x[0]))


def path_list(path):
    paths = []
    if os.path.isfile(path):
        files = [path]
    else:
        files = [y for x in os.walk(path) for y in glob(os.path.join(x[0], '*.yml')) + glob(os.path.join(x[0], '*.yaml')) + glob(os.path.join(x[0], '*.json'))]
    for file in files:
        _, file_extension = os.path.splitext(file)
        try:
            content = read_file(file)
            spec = load_content(content, file_extension)
            routes = [[m.upper(), p, file] for p in spec['paths'] for m in spec['paths'][p]]
            paths.extend(routes)
        except:
            print('parse error: file=' + file)

    _sort_paths(paths)
    return paths


def list(path):
    paths = path_list(path)
    export_table(paths, ['Method', 'Path', 'File'])
