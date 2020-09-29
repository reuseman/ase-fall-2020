import calculator as c
import unittest


class TestSubtract(unittest.TestCase):
    def test_subtract_integers_positive(self):
        result = c.subtract(3, 2)
        self.assertEqual(result, 1)

    def test_subtract_integers_negative(self):
        result = c.subtract(-6, -2)
        self.assertEqual(result, -4)

    def test_subtract_integers_pos_neg(self):
        result = c.subtract(4, -2)
        self.assertEqual(result, 6)

    def test_subtract_integers_neg_pos(self):
        result = c.subtract(-6, 3)
        self.assertEqual(result, -9)

    def test_subtract_integers_pos_zero(self):
        result = c.subtract(1, 0)
        self.assertEqual(result, 1)


if __name__ == "__main__":
    unittest.main()
