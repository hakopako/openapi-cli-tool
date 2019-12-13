import os
import unittest
import subprocess
from src.utils.repository import Repository

class TestRepository(unittest.TestCase):

    def _data_provider(self):
        current = os.path.dirname(os.path.abspath(__file__))
        return {
            'spec not found': {
                'input': ['./not-exist-spec-path'],
                'expected': []
            },
            'input multi file': {
                'input': [
                    os.path.join(current, 'resources/multi-file/file1.json'),
                    os.path.join(current, 'resources/multi-file/file2.yaml')
                ],
                'expected': [
                    ['GET', '/follwers', os.path.join(current, 'resources/multi-file/file2.yaml')],
                    ['POST', '/follwers', os.path.join(current, 'resources/multi-file/file2.yaml')],
                    ['PUT', '/follwers', os.path.join(current, 'resources/multi-file/file2.yaml')],
                    ['GET', '/posts', os.path.join(current, 'resources/multi-file/file1.json')],
                    ['POST', '/posts', os.path.join(current, 'resources/multi-file/file1.json')],
                    ['GET', '/users', os.path.join(current, 'resources/multi-file/file1.json')],
                    ['POST', '/users', os.path.join(current, 'resources/multi-file/file1.json')]
                ]
            },
            'input a file path': {
                'input': [os.path.join(current, 'resources/sample.yaml')],
                'expected': [
                    ['PUT', '/avatar', os.path.join(current, 'resources/sample.yaml')],
                    ['POST', '/pets', os.path.join(current, 'resources/sample.yaml')]
                ]
            },
            'input path ref': {
                'input': [os.path.join(current, 'resources/with-path-ref.yaml')],
                'expected': [
                    ['GET', '/with-path-referred', os.path.join(current, 'resources/with-path-ref.yaml')],
                    ['POST', '/with-path-referred', os.path.join(current, 'resources/with-path-ref.yaml')]
                ]
            }
        }


    def test_success_repository(self):
        for key, value in self._data_provider().items():
            repository = Repository(value['input'])
            actual = repository.routes

            self.assertEqual(actual.to_list(), value['expected'], key)
