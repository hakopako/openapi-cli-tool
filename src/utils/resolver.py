import os
from src.utils.file_control import read_file, load_content


def _find_reference(link, base_file_path):
    if '#/' in link:
        file_path, item_path = link.split('#/')
        items = item_path.split('/')
    else:
        file_path, items = link, []
    spec_file = base_file_path if file_path == '' else os.path.join(os.path.dirname(base_file_path), file_path)
    _, file_extension = os.path.splitext(spec_file)
    try:
        content = read_file(spec_file)
        spec = load_content(content, file_extension)
        for key in items:
            spec = spec[key]
        return spec, spec_file
    except Exception as e:
        print('Failed to load referance. file=' + base_file_path + ' $ref=' + link)
        return '', spec_file


def resolver(file_path, data):
    if not isinstance(data, dict):
        return data

    for key, value in data.items():
        if key == '$ref':
            new_value, base_file_path = _find_reference(value, file_path)
            data = resolver(base_file_path, new_value)
        else:
            new_value = resolver(file_path, value)
            data[key] = new_value
    return data
