from math_series import __version__
from math_series.series import fibonacci,lucas,sum_series

def test_version():
    assert __version__ == '0.1.0'


def test_fib():
    expected=34
    actual=fibonacci(9)
    assert expected==actual

def test_lucas():
    expected=76
    actual=lucas(9)
    assert expected==actual

def test_sum_fib():
    expected=34
    actual=sum_series(9)
    assert expected==actual

def test_sum_lucas():
    expected=76
    actual=sum_series(9,2,1)
    assert expected==actual
    
def test_sum_other():
    expected=173
    actual=sum_series(9, 2, 7)
    assert expected==actual