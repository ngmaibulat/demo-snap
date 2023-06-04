import unittest
import sys

# sys.path.append('..')

from pkg.package1 import get_salam

msg: str = get_salam()
print(msg)
