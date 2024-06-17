from bank import value

def test_hello():
    assert value("hello, ram") == 0

def test_hello_case_insensitivity():
    assert value("Hello, ramesh") == 0

def test_first_letter_h():
    assert value("hi, sir! How can i help you?") == 20

def test_if_no_hello_or_h():
    assert value("what's up buddy?") == 100
