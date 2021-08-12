import argparse

from robot_life.console import run_random_field

parser = argparse.ArgumentParser(
    prog="python3 -m robot_life",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
)
parser.add_argument("-W", "--width", type=int, default=80, help="field width")
parser.add_argument("-H", "--height", type=int, default=24, help="field height")
parser.add_argument("-P", "--period",
    type=float, default=0.1, help="population period")
parser.add_argument("-C", "--capacity",
    type=float, default=1_000_000, help="maximal history capacity")

args = parser.parse_args()

run_random_field(args.width, args.height, args.period, args.capacity)
