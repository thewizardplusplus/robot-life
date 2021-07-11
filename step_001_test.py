import os.path
import importlib.util
import unittest

# workaround for loading the module from the neighbor file
# without defining the parent module
step_001_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "step_001.py")
step_001_spec = importlib.util.spec_from_file_location("step_001", step_001_path)
step_001 = importlib.util.module_from_spec(step_001_spec)
step_001_spec.loader.exec_module(step_001)

class TestField(unittest.TestCase):
    def test_init(self):
        field = step_001.Field(2, 3)

        self.assertEqual(field._cells, [
            [False, False],
            [False, False],
            [False, False],
        ])
