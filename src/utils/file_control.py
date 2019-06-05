import os
import json
import yaml


def read_file(file_path):
    r = open(file_path, 'r')
    content = r.read()
    r.close()
    return content


def load_content(content, file_extension):
    try:
        return json.loads(content) if file_extension == 'json' else yaml.safe_load(content)
    except:
        return ''


def get_spec_from_file(file_path):
    _, file_extension = os.path.splitext(file_path)
    content = read_file(file_path)
    spec = load_content(content, file_path)
    return spec
