import unittest
import task3


class TestTypeMethods(unittest.TestCase):

    def test_fun(self):
        self.assertEqual(task3.fun(4, 5), 1)
