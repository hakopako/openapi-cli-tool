import unittest

class TestSample(unittest.TestCase):

    def test_sample(self):
        self.assertEqual('foo'.upper(), 'FOO')

if __name__ == '__main__':
    unittest.main()