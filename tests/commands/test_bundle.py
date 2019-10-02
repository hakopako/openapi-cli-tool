import subprocess
import json
import unittest
from src.commands.bundle import run_bundle


def read_file(file_path):
    r = open(file_path, 'r')
    content = r.read()
    r.close()
    return content


class TestBundle(unittest.TestCase):

    def _data_provider(self):
        spec = subprocess.check_output('find ./tests/resources/spec/folder1', shell=True).split("\n")
        return {
            'spec path not found without header file': {
                'input': [['./not-exist-spec-path'], None],
                'expected': {}
            },
            # 'spec path not found with header file': {
            #     'input': ['./not-exist-spec-path', './tests/resources/spec/template-header.json'],
            #     'expected': json.loads(read_file('./tests/resources/spec/template-header.json'))
            # },
            'spec path without header file': {
                'input': [spec, None],
                'expected': json.loads(read_file('./tests/resources/expected-bundle-auto-header.json'))
            },
            'spec path with header file': {
                'input': [spec, './tests/resources/spec/template-header.json'],
                'expected': json.loads(read_file('./tests/resources/expected-bundle-with-header.json'))
            },
        }

    def test_bundle(self):
        for key, value in self._data_provider().items():
            actual = run_bundle(value['input'][0], value['input'][1])
            self.assertEqual(actual, value['expected'], key)
