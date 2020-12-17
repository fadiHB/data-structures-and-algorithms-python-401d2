from data_structures_and_algorithms.data_structures.multi_bracket_validation.multi_bracket_validation import isBalanced

def test_True():
    actual = isBalanced('{{[()]}}')
    expected = True
    assert actual == expected

def test_False():
    actual = isBalanced('{{()]}}')
    expected = False
    assert actual == expected
