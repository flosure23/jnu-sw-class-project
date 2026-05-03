import unittest
from hypothesis import given, strategies as st
from number_utils import safe_average

class TestSafeAverage(unittest.TestCase):
    @given(
        st.integers(min_value=-1000000, max_value=1000000),
        st.integers(min_value=-1000000, max_value=1000000)
    )
    def test_average_between_two_values(self, a, b):
        result = safe_average(a, b)
        self.assertTrue(min(a, b) <= result <= max(a, b))

if __name__ == "__main__":
    unittest.main(verbosity=2)