import time

import mindstorms
import mindstorms.control

from robot_life.configuration import *
from robot_life.field import Field
from robot_life.running import run_field
from robot_life.serializing_for_robot import to_light_matrix

hub = mindstorms.MSHub()
while True:
    field = Field(FIELD_WIDTH, FIELD_HEIGHT, Field.random_generator)
    run_field(
        field=field,
        handler=lambda field_history: \
            to_light_matrix(
                lambda column, row, brightness: \
                    hub.light_matrix.set_pixel(column, row, int(brightness)),
                field_history,
                BRIGHTNESS_LEVEL_COUNT,
            ),
        population_period=POPULATION_PERIOD * 1_000_000_000,
        timer=time.time_ns,
        sleeper=lambda delay: \
            mindstorms.control.wait_for_seconds(delay / 1_000_000_000),
    )
