import os
import json
import yaml


def load_file(file_path):
    try:
        r = open(file_path, 'r')
        content = r.read()
        r.close()
        return content
    except:
        return ''


class FileControl:

    def __init__(self):
        self.spec_dict = {}

    def load_dict_from_file(self, file_path):
        if file_path in self.spec_dict:
            return self.spec_dict[file_path]
        try:
            r = open(file_path, 'r')
            content = r.read()
            r.close()
            _, file_extension = os.path.splitext(file_path)
            spec = ""
            if not os.path.exists(file_path):
                raise Exception('Faild not found.')
            if file_extension == '.json':
                spec = json.loads(content)
            elif file_extension in ['.yaml', '.yml']:
                spec = yaml.safe_load(content)
            else:
                raise Exception('Unknown extension.')
            self.spec_dict[file_path] = spec
            return spec
        except Exception as e:
            raise Exception('File Read Error (' + file_path + '): ' + str(e))
