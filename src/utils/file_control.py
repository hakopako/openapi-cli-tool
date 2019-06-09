import os
import json
import yaml


def load_dict_from_file(file_path):
    try:
        r = open(file_path, 'r')
        content = r.read()
        r.close()
        _, file_extension = os.path.splitext(file_path)
        if not os.path.exists(file_path):
            raise Exception('Faild not found.')
        if file_extension == '.json':
            return json.loads(content)
        elif file_extension in ['.yaml', '.yml']:
            return yaml.safe_load(content)
        else:
            raise Exception('Unknown extension.')
    except Exception as e:
        raise Exception('File Read Error (' + file_path + '): ' + str(e))
