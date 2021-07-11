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
