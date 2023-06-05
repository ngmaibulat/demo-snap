import unittest
import sys

# sys.path.append("..")

from pkg.package1 import salam

msg: str = salam.get_salam()
print(msg)
