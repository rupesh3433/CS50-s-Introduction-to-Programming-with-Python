from twttr import shorten

def test_shorten_no_vowels():
    assert shorten("Hello") == "Hll"

def test_shorten_only_vowels():
    assert shorten("AEIOUaeiou") == ""

def test_shorten_mixed_case():
    assert shorten("Beautiful") == "Btfl"

def test_shorten_empty_string():
    assert shorten("") == ""

def test_shorten_no_consonants():
    assert shorten("aeiou") == ""

def test_shorten_numbers_and_symbols():
    assert shorten("He110!") == "H110!"
