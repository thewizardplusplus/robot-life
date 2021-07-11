import time

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

def run_field(field, population_period=0.1, handler=lambda field: print(to_plaintext(field))):
    previous_time = time.time()
    while True:
        handler(field)

        field = field.populate()

        current_time = time.time()
        elapsed_time = current_time - previous_time
        if elapsed_time < population_period:
            time.sleep(population_period - elapsed_time)

        previous_time = current_time
