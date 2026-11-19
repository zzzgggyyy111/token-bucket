import pytest

from net import token_bucket as mod

CASES = [
    ('refill', [[0, 0], 10, 1, 5], [5, 10], False),
    ('refill', [[4, 0], 10, 1, 5], [5, 10], False),
    ('allow', [[0, 0], 1, 10, 1, 5], [True, [4, 10]], False),
    ('allow', [[5, 0], 1, 10, 1, 5], [True, [4, 10]], False),
    ('retry_after', [[0, 0], 2, 1], 2.0, True),
    ('consume', [[3, 0], 1], [2, 0], False),
    ('bucket_key', ['u', '/a'], 'u:/a', False),
    ('retry_after', [[0, 0], 1, 0], -1.0, True),
    ('refill', [[0, 0], 0, 1, 5], [0, 0], False),
    ('allow', [[1, 0], 2, 0, 1, 5], [False, [1, 0]], False),
    ('retry_after', [[1, 0], 3, 2], 1.0, True),
    ('consume', [[0, 0], 1], [0.0, 0], True),
    ('bucket_key', ['', ''], ':', False),
    ('allow', [[5, 0], 5, 0, 1, 5], [True, [0, 0]], False),
    ('refill', [[5, 0], 10, 1, 5], [5, 10], False),
]


@pytest.mark.parametrize("func_name,args,expected,approx", CASES)
def test_token_bucket_contract(func_name, args, expected, approx):
    func = getattr(mod, func_name)
    result = func(*args)
    if approx:
        assert result == pytest.approx(expected)
    else:
        assert result == expected
