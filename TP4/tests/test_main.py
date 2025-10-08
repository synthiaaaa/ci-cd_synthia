# tests/test_main.py

from app.main import count_words, longest_word, contains_word

def test_count_words_basic():
    assert count_words(["hello", "world"]) == 2

def test_longest_word_basic():
    assert longest_word(["hi", "hello"]) == "hello"

def test_contains_word_basic():
    assert contains_word(["python", "ci"], "python") is True
    assert contains_word(["python", "ci"], "java") is False
