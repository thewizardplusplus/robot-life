import unittest

from robot_life.field import Field
from robot_life.running import get_cell_brightness, run_field

class TestGetCellBrightness(unittest.TestCase):
    def test_with_alive_cell_in_last_population(self):
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

        brightness = get_cell_brightness(field_history, 1, 2, 2)

        self.assertEqual(brightness, 2)

    def test_with_alive_cell_in_previous_population(self):
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

        brightness = get_cell_brightness(field_history, 2, 1, 2)

        self.assertEqual(brightness, 1)

    def test_with_dead_cell(self):
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

        brightness = get_cell_brightness(field_history, 2, 2, 2)

        self.assertEqual(brightness, 0)

class TestRunField(unittest.TestCase):
    def test_basic(self):
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

        run_field(initial_field, _handler)

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

    def test_with_stable_pattern(self):
        initial_field = Field.from_cell_rows([
            [False, False, False, False],
            [False, True,  True,  False],
            [False, True,  True,  False],
            [False, False, False, False],
        ])

        field_histories = []
        def _handler(field_history):
            field_histories.append(field_history.copy())

        run_field(initial_field, _handler)

        self.assertEqual(field_histories, [[
            Field.from_cell_rows([
                [False, False, False, False],
                [False, True,  True,  False],
                [False, True,  True,  False],
                [False, False, False, False],
            ]),
        ]])

    def test_with_oscillator(self):
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

        run_field(initial_field, _handler)

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

    def test_with_low_history_capacity(self):
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
            run_field(initial_field, _handler, maximal_history_capacity=1)

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

    def test_with_delay_check_and_elapsed_time_less_than_population_period(self):
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

        time = 1_000_000
        def _timer():
            nonlocal time
            time += 0.025
            return time

        delays = []
        def _sleeper(delay):
            delays.append(delay)

        run_field(initial_field, _handler, timer=_timer, sleeper=_sleeper)

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
        self.assertEqual(len(delays), 1)
        if len(delays) == 1:
            self.assertAlmostEqual(delays[0], 0.075)

    def test_with_delay_check_and_elapsed_time_greater_than_population_period(self):
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

        time = 1_000_000
        def _timer():
            nonlocal time
            time += 0.25
            return time

        def _sleeper(delay):
            raise RuntimeError("should not be called")

        run_field(initial_field, _handler, timer=_timer, sleeper=_sleeper)

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
