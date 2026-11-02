import unittest
from simulation.minimal import estimate, run


class WLSChecks(unittest.TestCase):
    def test_known_solution(self):
        self.assertAlmostEqual(run()["estimate"], 1.005, places=12)

    def test_exact_measurements(self):
        self.assertAlmostEqual(estimate([1, 2], [3, 6], [1, 4]), 3)

    def test_invalid_input(self):
        for h, z, v in [([], [], []), ([0], [1], [1]),
                        ([1], [1], [0]), ([1], [float("nan")], [1]),
                        ([1, 2], [1], [1])]:
            with self.assertRaises(ValueError):
                estimate(h, z, v)
