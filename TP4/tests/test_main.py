from app.main import count_words, longest_word, contains_word


def test_count_words():
    assert count_words(["a", "b"]) == 2


def test_longest_word():
    assert longest_word(["a", "bb"]) == "bb"


def test_contains_word():
    assert contains_word(["a", "b"], "a") is True
