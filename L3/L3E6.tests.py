import unittest
import L3E6

class TestRegExp(unittest.TestCase):
    def test_year(self):
        # true section
        self.assertTrue(ptrn.search("11.11.1234"))
        self.assertTrue(ptrn.search("11.11.0001"))
        # false section
        self.assertFalse(ptrn.search("11.11.0000"))






if __name__ == '__main__':
    unittest.main()