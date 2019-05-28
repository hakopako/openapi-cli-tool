import unittest
from src.commands.list import path_list

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
                    ['POST', '/cats', './tests/resources/spec/ref_sample.yml'],
                    ['GET', '/follwers', './tests/resources/spec/folder1/sample2.yaml'],
                    ['POST', '/follwers', './tests/resources/spec/folder1/sample2.yaml'],
                    ['PUT', '/follwers', './tests/resources/spec/folder1/sample2.yaml'],
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
