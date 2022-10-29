import unittest
from merge import Concatenation

class TestConcatenation(unittest.TestCase):
    def setUp(self):
        self.s = Concatenation()
    # Тест прохода по всем if
    def test_concat01(self):
        self.assertEqual(self.s.concat(5, 5), 10)
    def test_concat02(self):
        self.assertEqual(self.s.concat(0, "5"), 5)
    def test_concat03(self):
        self.assertEqual(self.s.concat("5", 0), 5)
    def test_concat04(self):
        self.assertEqual(self.s.concat("100", "100"), 200)
    def test_concat05(self):
        self.assertEqual(self.s.concat("foo", "bar"), "foobar")

    # Граничные значения
    def test_concat11(self):
        self.assertEqual(self.s.concat(0, 0), 0)
    def test_concat12(self):
        self.assertEqual(self.s.concat(1, 242424240000000000000000000000000), 242424240000000000000000000000001)
    def test_concat13(self):
        self.assertEqual(self.s.concat(-2000, 2000), 0)
    def test_concat14(self):
        self.assertEqual(self.s.concat(-10,-10),-20)

        # Ломаем
    def test_concat21(self):
        self.assertEqual(self.s.concat(0.002, 0.001), 0.003)
    def test_concat22(self):
        self.assertEqual(self.s.concat(0.0, 0), 0)
    def test_concat23(self):
        self.assertEqual(self.s.concat(0.0, 1), 1)
    def test_concat24(self):
        self.assertEqual(self.s.concat(.0, 0), 0)
    def test_concat25(self):
        self.assertEqual(self.s.concat(.0, 1), 1)
    def test_concat26(self):
        self.assertEqual(self.s.concat("", 0), "0")
    def test_concat27(self):
        self.assertEqual(self.s.concat("", "foo"), "foo")
    def test_concat28(self):
        self.assertEqual(self.s.concat(1.2E+1, 1.1), 13.1)
    def test_concat29(self):
        self.assertEqual(self.s.concat([1], 4), 5)
    def test_concat30(self):
        self.assertEqual(self.s.concat(["foo"], 4), "foo4")
    def test_concat31(self):
        self.assertEqual(self.s.concat([1,2,3], 4), "??")

if __name__ == '__main__':
    unittest.main()
