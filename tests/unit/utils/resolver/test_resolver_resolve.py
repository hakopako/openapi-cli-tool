import os
import yaml
import unittest
from src.utils.resolver import resolver


class TestResolverResolve(unittest.TestCase):

    def read_file(self, file_path):
        r = open(file_path, 'r')
        content = r.read()
        r.close()
        return yaml.safe_load(content)

    def _success_data_provider(self):
        current = os.path.dirname(os.path.abspath(__file__))
        return {
            'escape characters': {
                'input': os.path.join(current, 'resources/inputs/escape_characters.yaml'),
                'expected': os.path.join(current, 'resources/expected/escape_characters.yaml')
            },
            'nested reference': {
                'input': os.path.join(current, 'resources/inputs/nested_reference.yaml'),
                'expected': os.path.join(current, 'resources/expected/nested_reference.yaml')
            },
            'local components': {
                'input': os.path.join(current, 'resources/inputs/local_components.yaml'),
                'expected': os.path.join(current, 'resources/expected/local_components.yaml')
            },
            'remote components': {
                'input': os.path.join(current, 'resources/inputs/remote_components.yaml'),
                'expected': os.path.join(current, 'resources/expected/remote_components.yaml')
            },
            'remote file': {
                'input': os.path.join(current, 'resources/inputs/remote_file.yaml'),
                'expected': os.path.join(current, 'resources/expected/remote_file.yaml')
            },

            # 'url file': {
            #     'input': os.path.join(current, 'resources/file.txt'),
            #     'expected': ''
            # },
            # 'url components': {
            #     'input': os.path.join(current, 'resources/file.txt'),
            #     'expected': ''
            # }
        }

    def _exception_data_provider(self):
        current = os.path.dirname(os.path.abspath(__file__))
        return {
            'ref not found': {
                'input': os.path.join(current, 'resources/file.yaml')
            }
        }

    def test_success_resolve(self):
        for key, value in self._success_data_provider().items():
            input_spec = self.read_file(value['input'])
            actual = resolver(value['input'], input_spec)
            expected = self.read_file(value['expected'])
            self.assertEqual(actual, expected, key)


    @unittest.skip("need to be fixed")
    def test_exception_resolve(self):
        for key, value in self._exception_data_provider().items():
            self.assertRaises(Exception, resolver(value['input']))
