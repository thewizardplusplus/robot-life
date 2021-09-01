# robot-life

_**Disclaimer:** LEGO® and MINDSTORMS® is a trademark of the LEGO Group of companies which does not sponsor, authorize or endorse this project._

## Testing

To run the unit tests, use the following command:

```
$ make test
```

## Usage of the Console Version

```
$ python3 -m robot_life -h | --help
$ python3 -m robot_life [options]
```

Options:

- `-h`, `--help` &mdash; show this help message and exit;
- `-W WIDTH`, `--width WIDTH` &mdash; field width (default: `80`);
- `-H HEIGHT`, `--height HEIGHT` &mdash; field height (default: `24`);
- `-P PERIOD`, `--period PERIOD` &mdash; population period (default: `0.1`);
- `-C CAPACITY`, `--capacity CAPACITY` &mdash; maximal history capacity (default: `1000000`);
- `-V VARIANTS`, `--variants VARIANTS` &mdash; character variants (default: `.:*#O`).

## License

The MIT License (MIT)

Copyright &copy; 2021 thewizardplusplus
