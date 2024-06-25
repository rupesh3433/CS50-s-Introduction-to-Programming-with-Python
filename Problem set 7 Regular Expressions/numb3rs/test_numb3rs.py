from numb3rs import validate

def test_negative():
    assert validate("-1.255.249.123") == False
    assert validate("250.249.-36.123") == False
    assert validate("255.-45.249.123") == False
    assert validate("255.249.34.-5") == False

def test_minimum():
    assert validate("0.0.0.0") == True

def test_maximum():
    assert validate("255.255.255.255") == True

def test_positive_wrong():
    assert validate("256.255.255.255") == False
    assert validate("255.256.255.255") == False
    assert validate("255.255.256.255") == False
    assert validate("255.255.255.256") == False

def test_positive_right():
    assert validate("25.255.255.250") == True
    assert validate("255.45.255.2") == True
    assert validate("33.255.255.243") == True
    assert validate("5.6.7.8") == True
