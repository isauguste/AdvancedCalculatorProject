import sys
import os

# Added root dir to sys.path so plugins can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from plugins import mod

def test_mod_basic():
    assert mod.run(9, 2) == 1
    assert mod.run(10, 3) == 1

