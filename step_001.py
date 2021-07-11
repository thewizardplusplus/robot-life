class Field:
    def __init__(self, width, height, generator=lambda x, y: False):
        self._cells = []
        for y in range(height):
            line = []
            for x in range(width):
                cell = generator(x, y)
                line.append(cell)

            self._cells.append(line)

    def for_each_cell(self, handler):
        for y, line in enumerate(self._cells):
            for x, cell in enumerate(line):
                handler(x, y, cell)
