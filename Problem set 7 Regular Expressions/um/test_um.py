from um import count

def test_basic_cases():
    assert count("um") == 1
    assert count("um um") == 2
    assert count("um hello, um k xa um yaar") == 3
    assert count("hello") == 0

def test_case_sensetive():
    assert count("Um") == 1
    assert count("um UM") == 2
    assert count("um hello, UM k xa um yaar") == 3
    assert count("HELLO") == 0

def test_corner_cases():
    assert count("Umumumumum") == 0
    assert count("yummy") == 0
    assert count("um! hello, UMM k xa um yaar") == 2
    assert count("m_um") == 0
