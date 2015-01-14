import unittest


class Test_Main(unittest.TestCase):
    def setUp(self):
        ""
        self.a=Solver()

    def test_set1(self):
        ""
        set1="set1.txt"
        self.assertEqual('',self.a.solve(set1))
