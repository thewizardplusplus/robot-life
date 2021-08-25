import time

from robot_life.runner import basic_run_field
from robot_life.field import Field

# https://www.conwaylife.com/wiki/Plaintext
def to_plaintext(field_history):
    characters = []
    def _handler(column, row, cell):
        if characters != [] and column == 0:
            characters.append("\n")

        previous_cell = field_history[-2].get_cell(column, row) \
            if len(field_history) > 1 else False
        character = "O" if cell \
            else "*" if previous_cell \
            else "."
        characters.append(character)

    field_history[-1].handle_cells(_handler)

    return "".join(characters)

def print_as_plaintext(field_history):
    print(to_plaintext(field_history))

def run_field(
    field,
    population_period=0.1,
    maximal_history_capacity=1_000_000,
    handler=print_as_plaintext,
):
    basic_run_field(field, handler, population_period, maximal_history_capacity)

# resolution of terminal VT100 by default
def run_random_field(
    width=80,
    height=24,
    population_period=0.1,
    maximal_history_capacity=1_000_000,
    handler=print_as_plaintext,
):
    field = Field(width, height, Field.random_generator)
    run_field(field, population_period, maximal_history_capacity, handler)
