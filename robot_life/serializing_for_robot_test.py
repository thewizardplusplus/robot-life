import unittest

from robot_life.field import Field
from robot_life.serializing_for_robot import to_light_matrix

class TestToLightMatrix(unittest.TestCase):
    def test_basic(self):
        pixels = []
        def _set_pixel(column, row, brightness_percent):
            pixels.append((column, row, brightness_percent))

        field_history = [
            Field.from_cell_rows([
                [False, False, False, False, False],
                [False, False, True,  False, False],
                [False, False, False, True,  False],
                [False, True,  True,  True,  False],
                [False, False, False, False, False],
                [False, False, False, False, False],
            ]),
            Field.from_cell_rows([
                [False, False, False, False, False],
                [False, False, False, False, False],
                [False, True,  False, True,  False],
                [False, False, True,  True,  False],
                [False, False, True,  False, False],
                [False, False, False, False, False],
            ]),
        ]

        result = to_light_matrix(_set_pixel, field_history, 3)

        self.assertEqual(pixels, [
            (0, 0, 0), (1, 0,   0), (2, 0,   0), (3, 0,   0), (4, 0, 0),
            (0, 1, 0), (1, 1,   0), (2, 1,  50), (3, 1,   0), (4, 1, 0),
            (0, 2, 0), (1, 2, 100), (2, 2,   0), (3, 2, 100), (4, 2, 0),
            (0, 3, 0), (1, 3,  50), (2, 3, 100), (3, 3, 100), (4, 3, 0),
            (0, 4, 0), (1, 4,   0), (2, 4, 100), (3, 4,   0), (4, 4, 0),
            (0, 5, 0), (1, 5,   0), (2, 5,   0), (3, 5,   0), (4, 5, 0),
        ])
