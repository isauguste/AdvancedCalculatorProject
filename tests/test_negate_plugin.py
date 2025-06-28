import sys
import os

# Added root dir to sys.path so plugins can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from plugins import negate

def test_negate_basic():
    assert negate.run(-8, 0) == 8
    assert negate.run(5, 0) == -5
    assert negate.run(0, 0) == 0

