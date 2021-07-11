class Field:
    def __init__(self, width, height):
        self._cells = [[False] * width] * height

    def for_each_cell(self, handler):
        for y, line in enumerate(self._cells):
            for x, cell in enumerate(line):
                handler(x, y, cell)
