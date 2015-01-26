import os
import unittest

from hellolib import hello

class TestHelloBehavior(unittest.TestCase):

    def setUp(self):
        """ keep track of old hostname and reset it after every test """
        self.old_hostname = None
        if 'message' in os.environ:
            self.old_hostname = os.environ['message']

    def tearDown(self):
        """ reset old hostname after every test """
        if self.old_hostname:
            os.environ['message'] = self.old_hostname

    def test_unsure_when_no_greeting(self):
        """ when no greeting is set, should be unsure """

        # set up
        os.environ['greeting'] = 'to be able to be deleted'
        del os.environ['greeting']

        # check assumptions
        self.assertEqual(hello(), "Hi! I'm not sure what to say. :(")

    def test_hello(self):
        """ when greeting is set, hello should be from that message """

        # set up
        os.environ['greeting'] = "testmessage"

        # check assumptions
        self.assertEqual(hello(), "testmessage")

    def test_can_pass(self):
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
