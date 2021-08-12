import unittest

from robot_life.field import Field
from robot_life.console import to_plaintext

class TestToPlaintext(unittest.TestCase):
    def test_to_plaintext(self):
        field = Field.from_cell_rows([
            [False, False, False, False, False],
            [False, False, True,  False, False],
            [False, False, False, True,  False],
            [False, True,  True,  True,  False],
            [False, False, False, False, False],
        ])

        result = to_plaintext(field)

        self.assertEqual(
            result,
            ".....\n" +
            "..O..\n" +
            "...O.\n" +
            ".OOO.\n" +
            ".....",
        )

    def test_to_plaintext_with_not_square_field(self):
        field = Field.from_cell_rows([
            [False, False, False, False, False],
            [False, False, False, False, False],
            [False, False, True,  False, False],
            [False, False, False, True,  False],
            [False, True,  True,  True,  False],
            [False, False, False, False, False],
            [False, False, False, False, False],
        ])

        result = to_plaintext(field)

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
