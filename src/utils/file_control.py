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
