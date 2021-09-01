import unittest

from robot_life.field import Field
from robot_life.console import to_plaintext

class TestToPlaintext(unittest.TestCase):
    def test_basic(self):
        field = Field.from_cell_rows([
            [False, False, False, False, False],
            [False, False, True,  False, False],
            [False, False, False, True,  False],
            [False, True,  True,  True,  False],
            [False, False, False, False, False],
        ])

        result = to_plaintext([field])

        self.assertEqual(
            result,
            ".....\n" +
            "..O..\n" +
            "...O.\n" +
            ".OOO.\n" +
            ".....",
        )

    def test_with_not_square_field_when_width_less_than_height(self):
        field = Field.from_cell_rows([
            [False, False, False, False, False],
            [False, False, False, False, False],
            [False, False, True,  False, False],
            [False, False, False, True,  False],
            [False, True,  True,  True,  False],
            [False, False, False, False, False],
            [False, False, False, False, False],
        ])

        result = to_plaintext([field])

        self.assertEqual(
            result,
            ".....\n" +
            ".....\n" +
            "..O..\n" +
            "...O.\n" +
            ".OOO.\n" +
            ".....\n" +
            ".....",
        )

    def test_with_not_square_field_when_width_greater_than_height(self):
        field = Field.from_cell_rows([
            [False, False, False, False, False, False, False],
            [False, False, False, True,  False, False, False],
            [False, False, False, False, True,  False, False],
            [False, False, True,  True,  True,  False, False],
            [False, False, False, False, False, False, False],
        ])

        result = to_plaintext([field])

        self.assertEqual(
            result,
            ".......\n" +
            "...O...\n" +
            "....O..\n" +
            "..OOO..\n" +
            ".......",
        )

    def test_with_previous_field(self):
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

        result = to_plaintext(field_history, ".oO")

        self.assertEqual(
            result,
            ".....\n" +
            "..o..\n" +
            ".O.O.\n" +
            ".oOO.\n" +
            "..O..\n" +
            ".....",
        )
