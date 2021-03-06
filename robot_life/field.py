import random

class Field:
    @staticmethod
    def random_generator(column, row):
        return random.getrandbits(8) < 128

    @staticmethod
    def from_cell_rows(cell_rows):
        for cell_row in cell_rows[1:]:
            if len(cell_row) != len(cell_rows[0]):
                raise RuntimeError("rows have different length")

        width = len(cell_rows[0]) if len(cell_rows) != 0 else 0
        height = len(cell_rows)

        def _generator(column, row):
            return cell_rows[row][column]

        return Field(width, height, _generator)

    def __init__(self, width, height, generator=lambda column, row: False):
        self._width = width
        self._height = height

        self._cell_rows = []
        for row in range(height):
            cell_row = []
            for column in range(width):
                cell = generator(column, row)
                cell_row.append(cell)

            self._cell_rows.append(cell_row)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def get_cell(self, column, row):
        return self._cell_rows[row][column]

    def get_neighbors(self, column, row):
        neighbors = 0
        for row_offset in [-1, 0, 1]:
            for column_offset in [-1, 0, 1]:
                if column_offset == 0 and row_offset == 0:
                    continue

                transformed_column = column + column_offset
                transformed_row = row + row_offset

                # wrap the coordinates to simulate a toroidal field
                transformed_column = \
                    (transformed_column + self._width) % self._width
                transformed_row = \
                    (transformed_row + self._height) % self._height

                cell = self.get_cell(transformed_column, transformed_row)
                if cell:
                    neighbors += 1

        return neighbors

    def handle_cells(self, handler):
        for row in range(self._height):
            for column in range(self._width):
                cell = self.get_cell(column, row)
                handler(column, row, cell)

    def populate_cell(self, column, row):
        cell = self.get_cell(column, row)
        neighbors = self.get_neighbors(column, row)

        will_be_born = not cell and neighbors == 3
        will_survive = cell and (neighbors == 2 or neighbors == 3)

        return will_be_born or will_survive

    def populate(self):
        next_field = Field(self._width, self._height)
        def _next_field_filler(column, row, cell):
            next_cell = self.populate_cell(column, row)
            next_field._cell_rows[row][column] = next_cell

        self.handle_cells(_next_field_filler)

        return next_field
