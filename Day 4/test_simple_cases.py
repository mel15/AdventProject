import pytest

from day4 import IsChristmasTimePart1, IsChristmasTimePart2


@pytest.mark.parametrize("xmas_test",
                         [
                             ["XMAS"],
                             ["SAMX"],
                             ['X.\n', 'M.\n', 'A.\n', 'S.\n', 'A.'],
                             ['.X\n', '.M\n', '.A\n', '.S\n', 'A.'],
                             ['S.\n', 'A.\n', 'M.\n', 'X.\n', 'A.'],
                             ['.S\n', '.A\n', '.M\n', '.X\n', 'A.'],
                             ['X...\n', '.M..\n', '..A.\n', '...S\n', 'A...'],
                             ['S...\n', '.A..\n', '..M.\n', '...X\n', 'A...'],
                             ['...S\n', '..A.\n', '.M..\n', 'X...\n', 'A...'],
                             ['...X\n', '..M.\n', '.A..\n', 'S...\n', 'A...']
                         ]
                         )
def test_xmas(xmas_test):
    assert IsChristmasTimePart1(xmas_test) == 1


@pytest.mark.parametrize("xmas_test",
                         [
                             ['M.S\n', '.A.\n', 'M.S'],
                             ['M.M\n', '.A.\n', 'S.S'],
                             ['S.M\n', '.A.\n', 'S.M'],
                             ['S.S\n', '.A.\n', 'M.M'],
                             ['.S.S.\n', '..A..\n', '.M.M.'],
                             ['.....\n', '.S.S.\n', '..A..\n', '.M.M.\n', '.....']
                         ]
                         )
def test_xmas_part2(xmas_test):
    assert IsChristmasTimePart2(xmas_test) == 1


@pytest.mark.parametrize("xmas_test",
                         [
                             ['.....\n', '.S.S.\n', '..A..\n', '.M.M.\n', '.....'],
                             ['.M.M.\n', '..A..\n', '.S.S.'],
                             ['.S.M.\n', '..A..\n', '.S.M.'],
                             ['.S.S.\n', '..A..\n', '.M.M.']
                         ]
                         )
def test_xmas_part2(xmas_test):
    assert IsChristmasTimePart2(xmas_test) == 1
