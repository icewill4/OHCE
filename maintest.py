import unittest
from main import *


class Test_TestMain(unittest.TestCase):
    def test_main_helloWorld(self):
        self.assertEqual(helloWorld(), "Hello world")
