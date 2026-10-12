from fahrenheit_to_celsius import fahrenheit_to_celsius

def test_freezing_point():
    assert fahrenheit_to_celsius(32) == 0

test_freezing_point()

def test_boiling_point():
   assert fahrenheit_to_celsius(212) == 100

test_boiling_point()

