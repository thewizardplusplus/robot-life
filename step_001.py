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

    def get_neighbors(self, x, y):
        neighbors = 0
        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue

                # wrap the coordinates to simulate a toroidal field
                wrapped_x = (x + dx + self._width) % self._width
                wrapped_y = (y + dy + self._height) % self._height

                cell = self._cells[wrapped_y][wrapped_x]
                if cell:
                    neighbors += 1

        return neighbors

    def handle_cells(self, handler):
        for y in range(self._height):
            for x in range(self._width):
                cell = self._cells[y][x]
                handler(x, y, cell)

    def populate(self):
        next_field = Field(self._width, self._height)
        def _next_field_filler(x, y, cell):
            neighbors = self.get_neighbors(x, y)
            will_be_born = not cell and neighbors == 3
            will_survive = cell and (neighbors == 2 or neighbors == 3)
            next_field._cells[y][x] = will_be_born or will_survive

        self.handle_cells(_next_field_filler)
        return next_field
