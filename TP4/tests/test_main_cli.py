from app.main import count_words, longest_word, contains_word


def test_main_logic():
    sample = ["Python", "CI/CD", "GitHub", "Actions"]
    assert count_words(sample) == 4
    assert longest_word(sample) == "Actions"
    assert contains_word(sample, "GitHub") is True
