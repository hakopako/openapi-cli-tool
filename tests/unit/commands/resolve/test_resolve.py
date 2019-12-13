import os
import yaml
import subprocess
import unittest
from src.commands.resolve import run_resolve


def read_file(file_path):
    r = open(file_path, 'r')
    content = r.read()
    r.close()
    return yaml.safe_load(content)


class TestResolve(unittest.TestCase):

    def _data_provider(self):
        current = os.path.dirname(os.path.abspath(__file__))
        return {
            'spec not found': {
                'input': {
                    'method': 'get', 
                    'path': '/cats', 
                    'files': ['./not-exist-spec-path']
                },
                'expected': []
            },
            'find a spec': {
                'input': {
                    'method': 'post', 
                    'path': '/pets', 
                    'files': [os.path.join(current, 'resources/inputs/find-a-spec.yaml')]
                },
                'expected': os.path.join(current, 'resources/expected/find-a-spec.yaml')
            },
            'duplicated spec': {
                'input': {
                    'method': 'post', 
                    'path': '/pets', 
                    'files': [
                        os.path.join(current, 'resources/inputs/duplicated-spec-1.yaml'),
                        os.path.join(current, 'resources/inputs/duplicated-spec-2.yaml')
                    ]
                },
                'expected': os.path.join(current, 'resources/expected/duplicated-spec.yaml')
            }
        }

    def test_resolve(self):
        for key, value in self._data_provider().items():
            actual = run_resolve(
                value['input']['method'], 
                value['input']['path'], 
                value['input']['files']
            )
            if isinstance(value['expected'], str) and os.path.isfile(value['expected']):
                expected = read_file(value['expected'])
                self.assertEqual(actual, expected, key)
            else:
                self.assertEqual(actual, value['expected'], key)
