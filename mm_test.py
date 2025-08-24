import unittest
from my_math import line_eq, quad_eq

class TestMyMath(unittest.TestCase):
    def test_line_eq(self):
        self.assertEqual(line_eq(1, 2), -2)
        self.assertEqual(line_eq(0, 5), None)

    def test_quad_eq_two_roots(self):
        self.assertListEqual(quad_eq(1, -3, 2), [2.0, 1.0])
        self.assertListEqual(quad_eq(2, 4, -6), [1.0, -3.0])

    def test_quad_eq_one_root(self):
        self.assertListEqual(quad_eq(1, 2, 1), [-1.0])

    def test_quad_eq_no_roots(self):
        self.assertListEqual(quad_eq(1, 0, 1), [])

if __name__ == '__main__':
    unittest.main()