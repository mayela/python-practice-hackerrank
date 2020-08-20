from weird_not_weird import weird_not_weird
from hypothesis import given, settings
import hypothesis.strategies as st


def test_5_is_weird():
    result = weird_not_weird(5)
    assert result == "Weird"


def test_2_is_not_weird():
    result = weird_not_weird(2)
    assert result == "Not weird"


@given(number=st.integers().filter(lambda x: not x % 2 == 0))
@settings(max_examples=500)
def test_for_multiple_numbers(number):
    expected = "Weird"
    result = weird_not_weird(number)
    assert result == expected
