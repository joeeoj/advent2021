import pytest

from src.day02.part01 import main as main_part01
from src.day02.part02 import main as main_part02


def test_part01_ans():
    assert main_part01() == 1947824


def test_part02_ans():
    assert main_part02() == 1813062561
