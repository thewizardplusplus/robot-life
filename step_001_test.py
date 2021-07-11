import os.path
import importlib.util
import unittest
import random

# workaround for loading the module from the neighbor file
# without defining the parent module
step_001_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "step_001.py")
step_001_spec = importlib.util.spec_from_file_location("step_001", step_001_path)
step_001 = importlib.util.module_from_spec(step_001_spec)
step_001_spec.loader.exec_module(step_001)

class TestField(unittest.TestCase):
    def test_init_with_default_generator(self):
        field = step_001.Field(2, 3)

        self.assertEqual(field._cells, [
            [False, False],
            [False, False],
            [False, False],
        ])

    def test_init_with_custom_generator(self):
        field = step_001.Field(2, 3, lambda x, y: (x > 0 and y > 0) or y == 2)

        self.assertEqual(field._cells, [
            [False, False],
            [False, True],
            [True, True],
        ])

    def test_init_with_random_generator(self):
        random.seed(1) # reset the random generator for the test reproducibility

        field = step_001.Field(2, 3, lambda x, y: random.choice([False, True]))

        self.assertEqual(field._cells, [
            [False, False],
            [True, False],
            [True, True],
        ])

    def test_for_each_cell(self):
        cells = []

        field = step_001.Field(2, 3)
        field.for_each_cell(lambda x, y, cell: cells.append((x, y, cell)))

        self.assertEqual(cells, [
            (0, 0, False),
            (1, 0, False),
            (0, 1, False),
            (1, 1, False),
            (0, 2, False),
            (1, 2, False),
        ])
