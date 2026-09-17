import unittest
import utils

class UtilsTest(unittest.TestCase):

    def test_reversed(self):
        self.assertEqual(utils.Utils.reversed(3456), 6543)
        self.assertEqual(utils.Utils.reversed(12345), 54321)
        self.assertEqual(utils.Utils.reversed(111), 111)
        with self.assertRaises(TypeError):
            utils.Utils.reversed("hello")
        with self.assertRaises(TypeError):
            utils.Utils.reversed("1.23")
        
    def test_formatter(self):
        self.assertEqual(utils.Utils.formatter(3), ('0b11', '0o3'))
        self.assertEqual(utils.Utils.formatter(10), ('0b1010', '0o12'))
        self.assertEqual(utils.Utils.formatter(333), ('0b101001101', '0o515'))
        self.assertEqual(utils.Utils.formatter(100), ('0b1100100', '0o144'))
        with self.assertRaises(TypeError):
            utils.Utils.formatter("hello")
        with self.assertRaises(TypeError):
            utils.Utils.formatter("1.23")

if __name__ == '__main__':
    unittest.main()