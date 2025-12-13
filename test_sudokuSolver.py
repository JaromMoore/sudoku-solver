import pytest

from sudokuSolver import getRow, getColumn

SNumberList = [0, 1, 0, 0, 0, 8, 6, 7, 2, 4, 2, 8, 0, 0, 0, 0, 1, 0, 5, 0, 0, 9, 1, 0, 0, 8, 4, 6, 0, 2, 0, 0, 0, 8, 4, 9, 9, 8, 4, 0, 0, 3, 0, 0, 0, 0, 0, 0, 4, 0, 9, 2, 0, 6, 2, 4, 1, 7, 0, 0, 0, 0, 0, 0, 5, 0, 2, 9, 0, 0, 0, 7, 0, 0, 0, 0, 5, 0, 4, 2, 0]

def test_getRow():
    assert getRow(5) == [0, 0, 0, 4, 0, 9, 2, 0, 6]
    assert getRow(0) == [0, 1, 0, 0, 0, 8, 6, 7, 2]
    assert getRow(8) == [0, 0, 0, 0, 5, 0, 4, 2, 0]

def test_getColumn():
    assert getColumn(0) == [0, 4, 5, 6, 9, 0, 2, 0, 0]
    assert getColumn(4) == [0, 0, 1, 0, 0, 0, 0, 9, 5]
    assert getColumn(8) == [2, 0, 4, 9, 0, 6, 0, 7, 0]

pytest.main(["-v", "--tb=line", "-rN", __file__])