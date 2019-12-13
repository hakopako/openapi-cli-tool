import os
import yaml
import unittest
from src.commands.bundle import run_bundle


def read_file(file_path):
    r = open(file_path, 'r')
    content = r.read()
    r.close()
    return yaml.safe_load(content)


class TestBundle(unittest.TestCase):

    def _data_provider(self):
        current = os.path.dirname(os.path.abspath(__file__))
        return {
            'spec path without header file': {
                'input': {
                    'files': [
                        os.path.join(current, 'resources/inputs/file1.json'),
                        os.path.join(current, 'resources/inputs/file2.yaml'),
                    ],
                    'header': None
                },
                'expected': os.path.join(current, 'resources/expected/without-header.yaml')
            },
            'spec path with header file': {
                'input': {
                    'files': [
                        os.path.join(current, 'resources/inputs/file1.json'),
                        os.path.join(current, 'resources/inputs/file2.yaml'),
                    ],
                    'header': os.path.join(current, 'resources/inputs/template-header.yaml')
                },
                'expected': os.path.join(current, 'resources/expected/with-header.yaml')
            },
        }

    def test_bundle(self):
        for key, value in self._data_provider().items():
            actual = run_bundle(value['input']['files'], value['input']['header'])
            expected = read_file(value['expected'])
            self.assertEqual(actual, expected, key)
