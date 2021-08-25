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

        field_histories = []
        def _handler(field_history):
            field_histories.append(field_history.copy())

        basic_run_field(initial_field, _handler)

        wanted_field_histories = [
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
        ]
        self.assertEqual(field_histories, [
            wanted_field_histories[:1],
            wanted_field_histories[:2],
            wanted_field_histories[:3],
            wanted_field_histories[:4],
            wanted_field_histories[:5],
            wanted_field_histories[:6],
            wanted_field_histories,
        ])

    def test_basic_run_field_with_stable_pattern(self):
        initial_field = Field.from_cell_rows([
            [False, False, False, False],
            [False, True,  True,  False],
            [False, True,  True,  False],
            [False, False, False, False],
        ])

        field_histories = []
        def _handler(field_history):
            field_histories.append(field_history.copy())

        basic_run_field(initial_field, _handler)

        self.assertEqual(field_histories, [[
            Field.from_cell_rows([
                [False, False, False, False],
                [False, True,  True,  False],
                [False, True,  True,  False],
                [False, False, False, False],
            ]),
        ]])

    def test_basic_run_field_with_oscillator(self):
        initial_field = Field.from_cell_rows([
            [False, False, False, False, False],
            [False, False, True,  False, False],
            [False, False, True,  False, False],
            [False, False, True,  False, False],
            [False, False, False, False, False],
        ])

        field_histories = []
        def _handler(field_history):
            field_histories.append(field_history.copy())

        basic_run_field(initial_field, _handler)

        wanted_field_histories = [
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
        ]
        self.assertEqual(field_histories, [
            wanted_field_histories[:1],
            wanted_field_histories,
        ])

    def test_basic_run_field_with_low_history_capacity(self):
        initial_field = Field.from_cell_rows([
            [False, False, False, False, False],
            [False, False, True,  False, False],
            [False, False, True,  False, False],
            [False, False, True,  False, False],
            [False, False, False, False, False],
        ])

        field_histories = []
        def _handler(field_history):
            field_histories.append(field_history.copy())
            if len(field_histories) == 5:
                raise RuntimeError("stop")

        with self.assertRaisesRegex(RuntimeError, "stop"):
            basic_run_field(initial_field, _handler, maximal_history_capacity=1)

        wanted_field_histories = [
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
        ]
        self.assertEqual(field_histories, [
            [wanted_field_histories[0]],
            [wanted_field_histories[1]],
            [wanted_field_histories[0]],
            [wanted_field_histories[1]],
            [wanted_field_histories[0]],
        ])
