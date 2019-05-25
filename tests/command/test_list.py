import unittest
from src.command.list import path_list

class TestList(unittest.TestCase):

    def _data_provider(self):
        return {
            'spec not found': {
                'input': './not-exist-spec-path',
                'expected': []
            },
            'input dir path': {
                'input': './tests/resources/spec',
                'expected': [
                    ['PUT', '/avatar', './tests/resources/spec/sample.yml'],
                    ['GET', '/follwers', './tests/resources/spec/folder1/sample2.yml'],
                    ['POST', '/follwers', './tests/resources/spec/folder1/sample2.yml'],
                    ['PUT', '/follwers', './tests/resources/spec/folder1/sample2.yml'],
                    ['POST', '/pets', './tests/resources/spec/sample.yml'],
                    ['GET', '/posts', './tests/resources/spec/folder1/sample.json'],
                    ['POST', '/posts', './tests/resources/spec/folder1/sample.json'],
                    ['GET', '/users', './tests/resources/spec/folder1/sample.json'],
                    ['POST', '/users','./tests/resources/spec/folder1/sample.json']
                ]
            },
            'input file path': {
                'input': './tests/resources/spec/sample.yml',
                'expected': [
                    ['PUT', '/avatar', './tests/resources/spec/sample.yml'],
                    ['POST', '/pets', './tests/resources/spec/sample.yml']
                ]
            }
        }

    def test_list(self):
        for key, value in self._data_provider().items ():
            actual = path_list(value['input'])
            self.assertEqual(actual, value['expected'], key)
