import pytest
from mystatistics import average


@pytest.mark.parametrize(
    "ns, expected",
    [
        ([1, 2, 3], 2),
        ([1, 2, 3, 4], 2.5),
        ([1, 2, 3, 4, 5], 3),
        ([0.1, 0.1, 0.1], 0.1),
    ],
)
def test_average(ns, expected):
    assert average(ns) == pytest.approx(expected)
