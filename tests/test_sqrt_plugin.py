import sys
import os

# Added root dir to sys.path so plugins can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from plugins import sqrt

def test_sqrt_basic():
    assert sqrt.run(25, 0) == 5
    assert sqrt.run(16, 0) == 4
    assert sqrt.run(0, 0) == 0

