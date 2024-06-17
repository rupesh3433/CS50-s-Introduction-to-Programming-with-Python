from plates import is_valid

def test_length():
    assert is_valid("AA") == True
    assert is_valid("A") == False
    assert is_valid("AAAAAAA") == False

def test_start_with_letters():
    assert is_valid("AA") == True
    assert is_valid("2AA") == False

def test_valid_characters():
    assert is_valid("AAA") == True
    assert is_valid("AA_A") == False

def test_number_placement():
    assert is_valid("AA123") == True
    assert is_valid("AAA021") == False
    assert is_valid("AA12A3") == False

def test_is_valid():
    assert is_valid("AA") == True
    assert is_valid("AAA123") == True
    assert is_valid("A12345") == False
    assert is_valid("AA_123") == False
    assert is_valid("A01234") == False

