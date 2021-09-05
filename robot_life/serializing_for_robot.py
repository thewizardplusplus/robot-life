from robot_life.running import get_cell_brightness

def to_light_matrix(set_pixel, field_history, brightness_level_count):
    maximal_brightness = brightness_level_count - 1
    def _handler(column, row, cell):
        brightness = \
            get_cell_brightness(field_history, column, row, maximal_brightness)
        brightness_percent = brightness / maximal_brightness * 100
        set_pixel(column, row, brightness_percent)

    field_history[-1].handle_cells(_handler)
