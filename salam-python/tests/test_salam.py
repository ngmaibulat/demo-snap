import unittest
import sys

sys.path.append("../..")

# sys.path.append("./")
from pkg.package1 import salam


class PackageTestCase(unittest.TestCase):
    def test_greet(self):
        msg: str = salam.get_salam()
        self.assertEqual(msg, "Salam Python!")


if __name__ == "__main__":
    unittest.main()
