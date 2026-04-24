from main import add, multiply

# existing tests
def test_add():
    assert add(2, 3) == 5

def test_multiply():
    assert multiply(3, 4) == 12

# -----------------------
# EDGE CASE TESTS
# -----------------------

def test_add_zero():
    assert add(0, 5) == 5
    assert add(0, 0) == 0

def test_add_negative():
    assert add(-2, -3) == -5
    assert add(-2, 5) == 3

def test_multiply_zero():
    assert multiply(0, 10) == 0

def test_multiply_negative():
    assert multiply(-2, 3) == -6
    assert multiply(-2, -3) == 6

def test_large_numbers():
    assert add(1000000, 2000000) == 3000000
    assert multiply(1000, 2000) == 2000000