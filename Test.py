from HW8 import convert_to_miles as convert_to_miles_test

def test(a):
    test_milies = convert_to_miles_test(a)
    test_milies_def = float(a) * 0.6214

    assert test_milies == test_milies_def

test(12)
test(2.023)
test(0)