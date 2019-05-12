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

    def test_scaffold(self):
        original_sysin = sys.stdin
        sys.stdin = StringIO(
            "\n" +  # Please enter title [""]:
            "\n" +  # Please enter version [v1.0]:
            "\n" +  # Please enter license [Apache 2.0]:
            "\n" +  # Please enter server url [http://example.com]:
            "/users\n" +  # Please enter path [/]:
            "get\n" +  # Please enter method for /users [get|post|put|delete|head|option|trace]
            "\n" +  # Please enter description for get /users [""]:
            "\n" +  # Please enter response code for get \users [200]:
            "succeed to register a new user\n" +  # Please enter response description for 200:
            "application/json\n" +  # Please enter response content-type for get /users [application/json]:
            "\n" +  # Add more response for %s %s ? Y/n [n]:
            "\n"  # Add more request method for %s ? Y/n [n]:
        )
        acutual = scaffold()
        sys.stdin = original_sysin
        expected_str = read_file('tests/resources/expected-default-output.json')
        expected = json.loads(expected_str)

        self.assertEqual(acutual, expected, 'default input')
