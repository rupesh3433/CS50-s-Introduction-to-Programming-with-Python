import pytest
from working import convert

def test_basic_conversions():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("11 AM to 1 PM") == "11:00 to 13:00"
    assert convert("12 PM to 12 AM") == "12:00 to 00:00"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"

def test_conversions_with_minutes():
    assert convert("9:15 AM to 5:45 PM") == "09:15 to 17:45"
    assert convert("11:59 AM to 1:01 PM") == "11:59 to 13:01"
    assert convert("12:30 PM to 12:30 AM") == "12:30 to 00:30"
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"

def test_edge_cases():
    assert convert("1 AM to 1 PM") == "01:00 to 13:00"
    assert convert("1 PM to 1 AM") == "13:00 to 01:00"
    assert convert("11:59 PM to 12:01 AM") == "23:59 to 00:01"
    assert convert("12:00 PM to 12:00 AM") == "12:00 to 00:00"

def test_invalid_input():
    with pytest.raises(ValueError):
        convert("8:60 AM to 4:60 PM")
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00 PM")
    with pytest.raises(ValueError):
        convert("13:00 PM to 14:00 PM")
    with pytest.raises(ValueError):
        convert("11:00 PM to 11:60 PM")
