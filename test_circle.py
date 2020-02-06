import unittest
from teamcity import is_running_under_teamcity
from teamcity.unittestpy import TeamcityTestRunner

from circles import circle_area

from math import pi


class TestcircleArea(unittest.TestCase):
    def test_area(self):
        # test areas when radious is >=0
        self.assertAlmostEqual(circle_area(1), pi)
        self.assertAlmostEqual(circle_area(2.1), pi * 2.1 ** 2)
        self.assertAlmostEqual(circle_area(10), pi * 10 ** 2)
        self.assertAlmostEqual(circle_area(3), pi * 3 ** 2)
        self.assertAlmostEqual(circle_area(7), pi * 7 ** 2)

    def test_area1(self):
        # test areas when radious is >=0
        self.assertAlmostEqual(circle_area(0), 3) # on purpose so it fails


if __name__ == '__main__':
    if is_running_under_teamcity():
        runner = TeamcityTestRunner()
    else:
        runner = unittest.TextTestRunner()
    unittest.main(testRunner=runner)

