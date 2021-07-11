class Field:
    def __init__(self, width, height, generator=lambda x, y: False):
        self._width = width
        self._height = height

        self._cells = []
        for y in range(height):
            line = []
            for x in range(width):
                cell = generator(x, y)
                line.append(cell)

            self._cells.append(line)

    def handle_cells(self, handler):
        for y in range(self._height):
            for x in range(self._width):
                cell = self._cells[y][x]
                handler(x, y, cell)
