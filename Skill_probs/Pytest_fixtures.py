import pytest


@pytest.fixture
def input_natural():
    num = 10
    return num


def test_sum_of_natural(input_natural):
    s = 0
    for i in range(1, input_natural+1):
        s += i
    print("Sum:", sum)
    assert s > 0


@pytest.mark.parametrize("num, factorial", [(1, 1), (2, 2), (5, 120)])
def test_factorials(num, factorial):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    assert fact == factorial


@pytest.mark.parametrize("num, factor", [(3, 2), (6, 4), (12, 6)])
def test_factors(num, factor):
    count = 2
    for i in range(2, num):
        if num % i == 0:
            count += 1
    assert count == factor
