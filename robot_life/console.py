import time

from robot_life.runner import basic_run_field
from robot_life.field import Field

# https://www.conwaylife.com/wiki/Plaintext
def to_plaintext(field):
    characters = []
    def _handler(column, row, cell):
        if characters != [] and column == 0:
            characters.append("\n")

        character = "O" if cell else "."
        characters.append(character)

    field.handle_cells(_handler)

    return "".join(characters)

def print_as_plaintext(field):
    print(to_plaintext(field))

def run_field(field, population_period=0.1, handler=print_as_plaintext):
    basic_run_field(field, handler, population_period)

# resolution of terminal VT100 by default
def run_random_field(
    width=80,
    height=24,
    population_period=0.1,
    handler=print_as_plaintext,
):
    field = Field(width, height, Field.random_generator)
    run_field(field, population_period, handler)
