import os
import unittest
import sys
import json

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO
from src.sample import scaffold


def read_file(file_path):
    r = open(file_path, 'r')
    content = r.read()
    r.close()
    return content


class TestSample(unittest.TestCase):

    def test_sample(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def __data_provider(self):
        return {
            'default input': {
                'input':
                    "\n" +  # Please enter title [""]:
                    "\n" +  # Please enter version [v1.0]:
                    "\n" +  # Please enter license [Apache 2.0]:
                    "\n" +  # Please enter server url [http://example.com]:
                    "/users\n" +  # Please enter path [/]:
                    "get\n" +  # Please enter method for /users [get|post|put|delete|head|option|trace]
                    "\n" +  # Please enter description for get /users [""]:
                    "\n" +  # Please enter response code for get /users [200]:
                    "succeed to return all users info\n" +  # Please enter response description for 200:
                    "application/json\n" +  # Please enter response content-type for get /users [application/json]:
                    "\n" +  # Add more response for get /users ? Y/n [n]:
                    "\n",  # Add more request method for /users ? Y/n [n]:
                'expected': 'tests/resources/expected-default-output.json'
            },
            'multiple response input': {
                'input':
                    "\n" +  # Please enter title [""]:
                    "\n" +  # Please enter version [v1.0]:
                    "\n" +  # Please enter license [Apache 2.0]:
                    "\n" +  # Please enter server url [http://example.com]:
                    "/users\n" +  # Please enter path [/]:
                    "get\n" +  # Please enter method for /users [get|post|put|delete|head|option|trace]
                    "\n" +  # Please enter description for get /users [""]:
                    "\n" +  # Please enter response code for get /users [200]:
                    "succeed to return all users info\n" +  # Please enter response description for 200:
                    "application/json\n" +  # Please enter response content-type for get /users [application/json]:
                    "Y\n" +  # Add more response for get /users ? Y/n [n]:
                    "400\n" +  # Please enter response code for get /users [200]:
                    "failed to return all users infon\n" +  # Please enter response description for 200:
                    "application/json\n" +  # Please enter response content-type for get /users [application/json]:
                    "\n" +  # Add more response for get /users ? Y/n [n]:
                    "Y\n" +  # Add more request method for /users ? Y/n [n]:
                    "post\n" +  # Please enter method for /users [get|post|put|delete|head|option|trace]
                    "\n" +  # Please enter description for post /users [""]:
                    "\n" +  # Please enter response code for post /users [200]:
                    "succeed to register a new user\n" +  # Please enter response description for 200:
                    "application/json\n" +  # Please enter response content-type for post /users [application/json]:
                    "Y\n" +  # Add more response for %s %s ? Y/n [n]:
                    "400\n" +  # Please enter response code for get /users [200]:
                    "failed to register a new user\n" +  # Please enter response description for 200:
                    "application/json\n" +  # Please enter response content-type for post /users [application/json]:
                    "\n" +  # Add more response for post /users ? Y/n [n]:
                    "\n",  # Add more request method for /users ? Y/n [n]:
                'expected': 'tests/resources/expected-multiple-response-output.json'
            }
        }

    def test_scaffold(self):
        original_sysin = sys.stdin
        for key, value in self.__data_provider().items():
            sys.stdin = StringIO(value['input'])
            actual = scaffold()
            expected_str = read_file(value['expected'])
            expected = json.loads(expected_str)
            self.assertEqual(actual, expected, key)
        sys.stdin = original_sysin
