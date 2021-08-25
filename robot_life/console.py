import time

from robot_life.runner import get_cell_brightness, basic_run_field
from robot_life.field import Field

# https://www.conwaylife.com/wiki/Plaintext
def to_plaintext(field_history, character_variants = ".*O"):
    characters = []
    maximal_brightness = len(character_variants) - 1
    def _handler(column, row, cell):
        if characters != [] and column == 0:
            characters.append("\n")

        brightness = \
            get_cell_brightness(field_history, column, row, maximal_brightness)
        character = character_variants[brightness]
        characters.append(character)

    field_history[-1].handle_cells(_handler)

    return "".join(characters)

def print_as_plaintext(field_history, character_variants = ".*O"):
    print(to_plaintext(field_history, character_variants))

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
