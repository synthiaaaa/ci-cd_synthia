from app.main import longest_word, contains_word


def test_longest_word_edge_cases():
    assert longest_word(["a", "ab", "abc"]) == "abc"
    assert longest_word([""]) == ""
    assert longest_word([]) == ""


def test_contains_word_edge_cases():
    assert contains_word([], "any") is False
    assert contains_word(["x"], "x") is True
