import unittest

from robot_life.field import Field
from robot_life.runner import basic_run_field

class TestBasicRunField(unittest.TestCase):
    def test_basic_run_field(self):
        initial_field = Field.from_cell_rows([
            [False, False, False, False, False, False, False, False, False],
            [False, True,  False, False, False, False, False, False, False],
            [False, True,  False, False, False, False, False, False, False],
            [False, True,  False, False, False, False, False, False, False],
            [False, False, False, True,  True,  False, False, False, False],
            [False, False, False, True,  False, True,  False, False, False],
            [False, False, False, False, False, True,  False, False, False],
            [False, False, False, False, False, True,  True,  False, False],
            [False, False, False, False, False, False, False, False, False],
        ])

        field_history = []
        def _handler(field):
            field_history.append(field)

        basic_run_field(initial_field, _handler)

        self.assertEqual(field_history, [
            Field.from_cell_rows([
                [False, False, False, False, False, False, False, False, False],
                [False, True,  False, False, False, False, False, False, False],
                [False, True,  False, False, False, False, False, False, False],
                [False, True,  False, False, False, False, False, False, False],
                [False, False, False, True,  True,  False, False, False, False],
                [False, False, False, True,  False, True,  False, False, False],
                [False, False, False, False, False, True,  False, False, False],
                [False, False, False, False, False, True,  True,  False, False],
                [False, False, False, False, False, False, False, False, False],
            ]),
            Field.from_cell_rows([
                [False, False, False, False, False, False, False, False, False],
                [False, False, False, False, False, False, False, False, False],
                [True,  True,  True,  False, False, False, False, False, False],
                [False, False, True,  False, False, False, False, False, False],
                [False, False, True,  True,  True,  False, False, False, False],
                [False, False, False, True,  False, True,  False, False, False],
                [False, False, False, False, False, True,  False, False, False],
                [False, False, False, False, False, True,  True,  False, False],
                [False, False, False, False, False, False, False, False, False],
            ]),
            Field.from_cell_rows([
                [False, False, False, False, False, False, False, False, False],
                [False, True,  False, False, False, False, False, False, False],
                [False, True,  True,  False, False, False, False, False, False],
                [False, False, False, False, False, False, False, False, False],
                [False, False, True,  False, True,  False, False, False, False],
                [False, False, True,  True,  False, True,  False, False, False],
                [False, False, False, False, False, True,  False, False, False],
                [False, False, False, False, False, True,  True,  False, False],
                [False, False, False, False, False, False, False, False, False],
            ]),
            Field.from_cell_rows([
                [False, False, False, False, False, False, False, False, False],
                [False, True,  True,  False, False, False, False, False, False],
                [False, True,  True,  False, False, False, False, False, False],
                [False, True,  True,  True,  False, False, False, False, False],
                [False, False, True,  False, True,  False, False, False, False],
                [False, False, True,  True,  False, True,  False, False, False],
                [False, False, False, False, False, True,  False, False, False],
                [False, False, False, False, False, True,  True,  False, False],
                [False, False, False, False, False, False, False, False, False],
            ]),
            Field.from_cell_rows([
                [False, False, False, False, False, False, False, False, False],
                [False, True,  True,  False, False, False, False, False, False],
                [True,  False, False, False, False, False, False, False, False],
                [False, False, False, False, False, False, False, False, False],
                [False, False, False, False, True,  False, False, False, False],
                [False, False, True,  True,  False, True,  False, False, False],
                [False, False, False, False, False, True,  False, False, False],
                [False, False, False, False, False, True,  True,  False, False],
                [False, False, False, False, False, False, False, False, False],
            ]),
            Field.from_cell_rows([
                [False, False, False, False, False, False, False, False, False],
                [False, True,  False, False, False, False, False, False, False],
                [False, True,  False, False, False, False, False, False, False],
                [False, False, False, False, False, False, False, False, False],
                [False, False, False, True,  True,  False, False, False, False],
                [False, False, False, True,  False, True,  False, False, False],
                [False, False, False, False, False, True,  False, False, False],
                [False, False, False, False, False, True,  True,  False, False],
                [False, False, False, False, False, False, False, False, False],
            ]),
            Field.from_cell_rows([
                [False, False, False, False, False, False, False, False, False],
                [False, False, False, False, False, False, False, False, False],
                [False, False, False, False, False, False, False, False, False],
                [False, False, False, False, False, False, False, False, False],
                [False, False, False, True,  True,  False, False, False, False],
                [False, False, False, True,  False, True,  False, False, False],
                [False, False, False, False, False, True,  False, False, False],
                [False, False, False, False, False, True,  True,  False, False],
                [False, False, False, False, False, False, False, False, False],
            ]),
        ])

    def test_basic_run_field_with_stable_pattern(self):
        initial_field = Field.from_cell_rows([
            [False, False, False, False],
            [False, True,  True,  False],
            [False, True,  True,  False],
            [False, False, False, False],
        ])

        field_history = []
        def _handler(field):
            field_history.append(field)

        basic_run_field(initial_field, _handler)

        self.assertEqual(field_history, [
            Field.from_cell_rows([
                [False, False, False, False],
                [False, True,  True,  False],
                [False, True,  True,  False],
                [False, False, False, False],
            ]),
        ])

    def test_basic_run_field_with_oscillator(self):
        initial_field = Field.from_cell_rows([
            [False, False, False, False, False],
            [False, False, True,  False, False],
            [False, False, True,  False, False],
            [False, False, True,  False, False],
            [False, False, False, False, False],
        ])

        field_history = []
        def _handler(field):
            field_history.append(field)

        basic_run_field(initial_field, _handler)

        self.assertEqual(field_history, [
            Field.from_cell_rows([
                [False, False, False, False, False],
                [False, False, True,  False, False],
                [False, False, True,  False, False],
                [False, False, True,  False, False],
                [False, False, False, False, False],
            ]),
            Field.from_cell_rows([
                [False, False, False, False, False],
                [False, False, False, False, False],
                [False, True,  True,  True,  False],
                [False, False, False, False, False],
                [False, False, False, False, False],
            ]),
        ])

    def test_basic_run_field_with_low_history_capacity(self):
        initial_field = Field.from_cell_rows([
            [False, False, False, False, False],
            [False, False, True,  False, False],
            [False, False, True,  False, False],
            [False, False, True,  False, False],
            [False, False, False, False, False],
        ])

        field_history = []
        def _handler(field):
            field_history.append(field)
            if len(field_history) == 5:
                raise RuntimeError("stop")

        with self.assertRaisesRegex(RuntimeError, "stop"):
            basic_run_field(initial_field, _handler, maximal_history_capacity=1)

        self.assertEqual(field_history, [
            Field.from_cell_rows([
                [False, False, False, False, False],
                [False, False, True,  False, False],
                [False, False, True,  False, False],
                [False, False, True,  False, False],
                [False, False, False, False, False],
            ]),
            Field.from_cell_rows([
                [False, False, False, False, False],
                [False, False, False, False, False],
                [False, True,  True,  True,  False],
                [False, False, False, False, False],
                [False, False, False, False, False],
            ]),
            Field.from_cell_rows([
                [False, False, False, False, False],
                [False, False, True,  False, False],
                [False, False, True,  False, False],
                [False, False, True,  False, False],
                [False, False, False, False, False],
            ]),
            Field.from_cell_rows([
                [False, False, False, False, False],
                [False, False, False, False, False],
                [False, True,  True,  True,  False],
                [False, False, False, False, False],
                [False, False, False, False, False],
            ]),
            Field.from_cell_rows([
                [False, False, False, False, False],
                [False, False, True,  False, False],
                [False, False, True,  False, False],
                [False, False, True,  False, False],
                [False, False, False, False, False],
            ]),
        ])
