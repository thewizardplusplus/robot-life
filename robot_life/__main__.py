import argparse

from robot_life.field import Field
from robot_life.running import run_field
from robot_life.serializing_for_console import to_plaintext

parser = argparse.ArgumentParser(
    prog="python3 -m robot_life",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
)
# the width of terminal VT100 by default
parser.add_argument("-W", "--width", type=int, default=80, help="field width")
# the height of terminal VT100 by default
parser.add_argument("-H", "--height", type=int, default=24, help="field height")
parser.add_argument("-P", "--period",
    type=float, default=0.1, help="population period")
parser.add_argument("-C", "--capacity",
    type=float, default=1_000_000, help="maximal history capacity")
parser.add_argument("-V", "--variants",
    default=".:*#O", help="character variants")

args = parser.parse_args()

field = Field(args.width, args.height, Field.random_generator)
run_field(
    field=field,
    handler=lambda field_history: \
        print(to_plaintext(field_history, args.variants)),
    population_period=args.period,
    maximal_history_capacity=args.capacity,
)
