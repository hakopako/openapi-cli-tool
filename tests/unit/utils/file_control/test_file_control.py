import os
import unittest
from src.utils.file_control import FileControl


class TestFileControl(unittest.TestCase):

    def _success_data_provider(self):
        current = os.path.dirname(os.path.abspath(__file__))
        return {
            'input yaml extension': {
                'input': os.path.join(current, 'resources/file.yaml'),
                'expected': {'message': 'ok'}
            },
            'input yml extension': {
                'input': os.path.join(current, 'resources/file.yml'),
                'expected': {'message': 'ok'}
            },
            'input json extension': {
                'input': os.path.join(current, 'resources/file.json'),
                'expected': {'message': 'ok'}
            }
        }

    def _exception_data_provider(self):
        current = os.path.dirname(os.path.abspath(__file__))
        return {
            'file not found': {
                'input': './not-exist-spec-path'
            },
            'input txt extension': {
                'input': os.path.join(current, 'resources/file.txt')
            }
        }

    def test_success_file_control(self):
        for key, value in self._success_data_provider().items():
            file_control = FileControl()
            actual = file_control.load_dict_from_file(value['input'])
            self.assertEqual(actual, value['expected'], key)

    @unittest.skip("need to be fixed")
    def test_exception_file_control(self):
        for key, value in self._exception_data_provider().items():
            file_control = FileControl()
            self.assertRaises(Exception, file_control.load_dict_from_file(value['input']))
