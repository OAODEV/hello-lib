import os
import unittest

from hellolib import hello

class TestHelloBehavior(unittest.TestCase):

    def setUp(self):
        self.old_hostname = None
        if 'HOSTNAME' in os.environ:
            self.old_hostname = os.environ['HOSTNAME']
        os.environ['HOSTNAME'] = "testhost"

    def tearDown(self):
        if self.old_hostname:
            os.environ['HOSTNAME'] = self.old_hostname

    def test_hello(self):
        self.assertEqual(hello(), "<h1>Hi! I'm testhost!</h1>")

    def test_can_pass(self):
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
