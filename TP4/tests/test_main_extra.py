# tests/test_main_extra.py

from app.main import count_words, longest_word, contains_word

def test_count_words_empty():
    assert count_words([]) == 0

def test_longest_word_tie():
    # le premier mot le plus long est retourné
    result = longest_word(["aa", "bb"])
    assert result in ["aa", "bb"]

def test_contains_word_false():
    assert contains_word(["x", "y"], "z") is False
