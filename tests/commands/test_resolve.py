import os
import json
import unittest
from src.commands.resolve import run_resolve


def read_file(file_path):
    r = open(file_path, 'r')
    content = r.read()
    r.close()
    return content


class TestResolve(unittest.TestCase):

    def _data_provider(self):
        return {
            'spec file not found': {
                'input': ['get', '/cats', './not-exist-spec-path'],
                'expected': []
            },
            'spec path not found': {
                'input': ['get', '/dogs', './tests/resources/spec'],
                'expected': []
            },
            'with ref': {
                'input': ['post', '/cats', './tests/resources/spec'],
                'expected': './tests/resources/expected-resolve-result.json'
            }
        }

    def test_resolve(self):
        for key, value in self._data_provider().items():
            actual = run_resolve(value['input'][0], value['input'][1], value['input'][2])
            if isinstance(value['expected'], str) and os.path.isfile(value['expected']):
                expected_str = read_file(value['expected'])
                expected = json.loads(expected_str)
                self.assertEqual(actual, [expected], key)
            else:
                self.assertEqual(actual, value['expected'], key)
