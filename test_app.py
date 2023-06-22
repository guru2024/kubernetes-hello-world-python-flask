from app import change

def change(amount):
    quarters = amount // 0.25
    nickels = (amount - quarters * 0.25) // 0.05
    pennies = (amount - quarters * 0.25 - nickels * 0.05) // 0.01
    return [
        {'quantity': quarters, 'coin': 'quarters'},
        {'quantity': nickels, 'coin': 'nickels'},
        {'quantity': pennies, 'coin': 'pennies'},
    ]

def test_change():
    quarters = 5
    nickels = 1
    pennies = 4
    expected_result = [
        {'quantity': quarters, 'coin': 'quarters'},
        {'quantity': nickels, 'coin': 'nickels'},
        {'quantity': pennies, 'coin': 'pennies'},
    ]
    assert expected_result == change(1.34)

if __name__ == '__main__':
    test_change()
