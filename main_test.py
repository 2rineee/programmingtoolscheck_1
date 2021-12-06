import unittest
from main import print_hi_erin, print_hi_you, print_hi_classmate


class MyTestCase(unittest.TestCase):
    def test_print_hi_erin(self):
        name='erin'
        self.assertEqual(print_hi_erin(), f"Hi, erin")

    def test_print_hi_you(self):
        self.assertEqual(print_hi_you(), f"")

    def test_print_hi_(self):
        self.assertEqual(,"")



if __name__ == '__main__':
    unittest.main()