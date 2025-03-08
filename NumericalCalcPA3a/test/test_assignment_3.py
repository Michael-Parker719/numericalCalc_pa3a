import unittest
from ..main import assignment_3


class TestNumericalMethods(unittest.TestCase):
    def test_euler_method(self):
        result = assignment_3.euler_method(assignment_3.f, 0, 1, 2, 10)
        # Compare to expected result for Euler method
        self.assertAlmostEqual(result, 1.2446380979332121, places=7)

    def test_runge_kutta_method(self):
        result = assignment_3.runge_kutta_method(assignment_3.f, 0, 1, 2, 10)
        # Compare to expected result for Runge-Kutta method
        self.assertAlmostEqual(result, 1.251316587879806, places=7)


if __name__ == '__main__':
    unittest.main()
