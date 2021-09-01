from robot_life.runner import get_cell_brightness

# https://www.conwaylife.com/wiki/Plaintext
def to_plaintext(field_history, character_variants = ".oO"):
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
