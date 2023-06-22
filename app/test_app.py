from app import change

import pytest

def test_change():
    expected_result = [{5: 'quarters'}, {1: 'nickels'}, {4: 'pennies'}]
    assert expected_result == change(1.34)

if __name__ == '__main__':
    pytest.main()
