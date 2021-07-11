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

        self.assertEqual(field._width, 2)
        self.assertEqual(field._height, 3)
        self.assertEqual(field._cell_rows, [
            [False, False],
            [False, False],
            [False, False],
        ])

    def test_init_with_custom_generator(self):
        def _generator(column, row):
            return (column > 0 and row > 0) or row == 2

        field = step_001.Field(2, 3, _generator)

        self.assertEqual(field._width, 2)
        self.assertEqual(field._height, 3)
        self.assertEqual(field._cell_rows, [
            [False, False],
            [False, True ],
            [True,  True ],
        ])

    def test_init_with_random_generator(self):
        random.seed(1) # reset the random generator for the test reproducibility
        def _generator(column, row):
            return random.choice([False, True])

        field = step_001.Field(2, 3, _generator)

        self.assertEqual(field._width, 2)
        self.assertEqual(field._height, 3)
        self.assertEqual(field._cell_rows, [
            [False, False],
            [True,  False],
            [True,  True ],
        ])

    def test_get_neighbors_in_the_center(self):
        field = step_001.Field(5, 5)
        field._cell_rows = [
            [False, False, False, False, False],
            [False, False, True,  False, False],
            [False, False, False, True,  False],
            [False, True,  True,  True,  False],
            [False, False, False, False, False],
        ]

        neighbors = field.get_neighbors(1, 2)

        self.assertEqual(neighbors, 3)

    def test_get_neighbors_in_the_corner(self):
        field = step_001.Field(3, 3)
        field._cell_rows = [
            [True,  False, False],
            [False, True,  True ],
            [False, True,  True ],
        ]

        neighbors = field.get_neighbors(2, 2)

        self.assertEqual(neighbors, 4)

    def test_handle_cells(self):
        cells = []
        def _handler(column, row, cell):
            cells.append((column, row, cell))

        field = step_001.Field(2, 3)
        field._cell_rows = [
            [False, False],
            [True,  False],
            [True,  True ],
        ]
        field.handle_cells(_handler)

        self.assertEqual(cells, [
            (0, 0, False),
            (1, 0, False),
            (0, 1, True),
            (1, 1, False),
            (0, 2, True),
            (1, 2, True),
        ])

    def test_populate_cell_that_will_be_born(self):
        field = step_001.Field(5, 5)
        field._cell_rows = [
            [False, False, False, False, False],
            [False, False, True,  False, False],
            [False, False, False, True,  False],
            [False, True,  True,  True,  False],
            [False, False, False, False, False],
        ]

        next_cell = field.populate_cell(2, 4)

        self.assertTrue(next_cell)

    def test_populate_cell_that_will_survive(self):
        field = step_001.Field(5, 5)
        field._cell_rows = [
            [False, False, False, False, False],
            [False, False, True,  False, False],
            [False, False, False, True,  False],
            [False, True,  True,  True,  False],
            [False, False, False, False, False],
        ]

        next_cell = field.populate_cell(2, 3)

        self.assertTrue(next_cell)

    def test_populate_cell_that_will_die(self):
        field = step_001.Field(5, 5)
        field._cell_rows = [
            [False, False, False, False, False],
            [False, False, True,  False, False],
            [False, False, False, True,  False],
            [False, True,  True,  True,  False],
            [False, False, False, False, False],
        ]

        next_cell = field.populate_cell(1, 3)

        self.assertFalse(next_cell)

    def test_populate(self):
        field = step_001.Field(5, 5)
        field._cell_rows = [
            [False, False, False, False, False],
            [False, False, True,  False, False],
            [False, False, False, True,  False],
            [False, True,  True,  True,  False],
            [False, False, False, False, False],
        ]

        next_field = field.populate()

        self.assertEqual(next_field._width, 5)
        self.assertEqual(next_field._height, 5)
        self.assertEqual(next_field._cell_rows, [
            [False, False, False, False, False],
            [False, False, False, False, False],
            [False, True,  False, True,  False],
            [False, False, True,  True,  False],
            [False, False, True,  False, False],
        ])

    def test_populate_with_not_square_field(self):
        field = step_001.Field(5, 7)
        field._cell_rows = [
            [False, False, False, False, False],
            [False, False, False, False, False],
            [False, False, True,  False, False],
            [False, False, False, True,  False],
            [False, True,  True,  True,  False],
            [False, False, False, False, False],
            [False, False, False, False, False],
        ]

        next_field = field.populate()

        self.assertEqual(next_field._width, 5)
        self.assertEqual(next_field._height, 7)
        self.assertEqual(next_field._cell_rows, [
            [False, False, False, False, False],
            [False, False, False, False, False],
            [False, False, False, False, False],
            [False, True,  False, True,  False],
            [False, False, True,  True,  False],
            [False, False, True,  False, False],
            [False, False, False, False, False],
        ])
