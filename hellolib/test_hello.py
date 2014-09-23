import os
import unittest

from hellolib import hello

class TestHelloBehavior(unittest.TestCase):

    def setUp(self):
        """ keep track of old hostname and reset it after every test """
        self.old_hostname = None
        if 'HOSTNAME' in os.environ:
            self.old_hostname = os.environ['HOSTNAME']

    def tearDown(self):
        """ reset old hostname after every test """
        if self.old_hostname:
            os.environ['HOSTNAME'] = self.old_hostname

    def test_anonymous_when_no_hostname(self):
        """ when no hostname is set, hello should be from anonymous """

        # set up
        os.environ['HOSTNAME'] = 'to be able to be deleted'
        del os.environ['HOSTNAME']

        # check assumptions
        self.assertEqual(hello(), "<h1>Hi! I'm Anonymous!</h1>")

    def test_hello(self):
        """ when hostname is set, hello shoudl be from that hostname """

        # set up
        os.environ['HOSTNAME'] = "testhost"

        # check assumptions
        self.assertEqual(hello(), "<h1>Hi! I'm testhost!</h1>")

    def test_can_pass(self):
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
